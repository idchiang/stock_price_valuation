# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 22:08:09 2021

@author: jiang
"""
import numpy as np
from src.default import col_sort


# Derive quantities
def derive_quant(df):
    n = len(df)
    # 收益成長率
    growth_rate = [np.nan] * len(df)
    for i in range(1, n):
        growth_rate[i] = df.total_revenues[i] / df.total_revenues[i - 1] - 1
    df['revenue_yoy_growth_rate'] = growth_rate
    # 毛利率
    df['gross_margin'] = df.gross_profit / df.total_revenues
    # 營運與其他成本
    df['other_expenses'] = df.gross_profit - df.ebt
    # 稅
    df['income_tax_expenses'] = df.ebt - df.net_income
    df['tax_rate'] = df.income_tax_expenses / df.ebt
    # 本益比
    df['pe_ratio'] = df.share_price / df.eps
    # Sort and return
    return df[col_sort]
