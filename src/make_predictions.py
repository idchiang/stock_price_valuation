# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 22:03:15 2021

@author: jiang
"""
import numpy as np
import pandas as pd
from src.default import col_sort, default_baseline_assumptions
from src.util import RMSE


# Predict one column according to the assumption
def make_pred_col(assumption, col_true, init_row_idx):
    n = len(col_true)
    col_pred = np.full(n, np.nan, dtype=float)
    if assumption[0] == 'const':
        col_pred[init_row_idx:] = np.full(n - init_row_idx, assumption[1])
    elif assumption[0] == 'last':
        col_pred[init_row_idx:] = col_true[init_row_idx - 1: -1]
    elif assumption[0] == 'avg':
        for i in range(init_row_idx, n):
            col_pred[i] = \
                col_true[i - assumption[1]:i].mean()
    else:
        assert False, 'Prediction method ' + assumption[0] + \
            ' not implimented yet.'
    return col_pred


# Reverse-derive quantities
def derive_quant_reversed(df_true, df_pred):
    n = len(df_true)
    total_revenues = np.full(n, np.nan, dtype=float)
    total_revenues[1:] = df_true.total_revenues[:-1].values * \
        (1.0 + df_pred.revenue_yoy_growth_rate[1:].values)
    df_pred['total_revenues'] = total_revenues
    #
    df_pred['gross_profit'] = df_pred.total_revenues * df_pred.gross_margin
    #
    df_pred['operating_income'] = \
        df_pred.gross_profit - df_pred.other_expenses
    df_pred['ebt'] = df_pred.operating_income
    #
    df_pred['income_tax_expenses'] = df_pred.ebt * df_pred.tax_rate
    df_pred['net_income'] = df_pred.ebt - df_pred.income_tax_expenses
    #
    df_pred['eps'] = df_pred.net_income / df_pred.share_outstanding
    df_pred['share_price'] = df_pred.eps * df_pred.pe_ratio
    return df_pred[col_sort]


# Make all predictions
def make_pred(df_true, init_row_idx=4, pred_mode='baseline',
              baseline_assumptions=default_baseline_assumptions):
    """
    pred_mode='baseline': use the baseline_assumptions
    pre_mode='optimize': loop through all models in all quantities.
               keep the best.
    """
    df_pred = df_true[['year']].copy()
    assumptions = pd.DataFrame(dtype=object)
    if pred_mode == 'baseline':
        # Predict according to assumptions
        for key in default_baseline_assumptions.keys():
            df_pred.insert(
                df_pred.shape[1],
                key,
                make_pred_col(baseline_assumptions[key],
                              df_true[key],
                              init_row_idx))
            assumptions[key] = baseline_assumptions[key]
    elif pred_mode == 'optimize':
        n = len(df_true)
        print('')
        for key in default_baseline_assumptions.keys():
            best_rmse = np.inf
            best_assumption = None
            best_pred = np.full(n, np.nan, dtype=float)
            for assumption in [('last', 1), ('avg', 3), ('avg', 4)]:
                cur_pred = make_pred_col(assumption, df_true[key],
                                         init_row_idx)
                rmse = RMSE(df_true[key].values, cur_pred)
                if rmse < best_rmse:
                    best_rmse = rmse
                    best_assumption = assumption
                    best_pred = cur_pred
            df_pred.insert(df_pred.shape[1], key, best_pred)
            assumptions[key] = best_assumption
            print('#', key, 'best modelled by', best_assumption)
        print('')
    # Reverse-derive
    df_pred = derive_quant_reversed(df_true, df_pred)
    # Return
    return df_pred, assumptions
