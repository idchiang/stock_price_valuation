# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 22:47:11 2021

@author: jiang
"""
import matplotlib.pyplot as plt
from src.default import col_sort
from src.util import RMSE

plt.style.use('idcgrid')
plt.ioff()
plt.tick_params(axis='x', which='minor', bottom=False)


def make_sum_col(col_period, col_true, col_pred_base, col_pred_opt,
                 dir_report, col_name):
    fig, ax = plt.subplots(figsize=[8, 6])
    ax.plot(col_period, col_true, marker='o', label='Historical Data')
    rmse = str(round(RMSE(col_true, col_pred_base), 2))
    ax.plot(col_period, col_pred_base, marker='o', linestyle='--',
            label='Baseline prediction\nRMSE=' + rmse)
    rmse = str(round(RMSE(col_true, col_pred_opt), 2))
    ax.plot(col_period, col_pred_opt, marker='o', linestyle='--',
            label='Optimized prediction\nRMSE=' + rmse)
    ax.set_xlabel('Year', size=16)
    ax.set_ylabel(col_name, size=16)
    ax.set_title(col_name, size=20)
    ax.legend()
    fig.savefig(dir_report + col_name + '.png')


def make_sum(df_true, df_pred_base, df_pred_opt, dir_report):
    for col_name in col_sort:
        if col_name == 'year':
            continue
        make_sum_col(
            df_true['year'],
            df_true[col_name],
            df_pred_base[col_name],
            df_pred_opt[col_name],
            dir_report,
            col_name
            )
    plt.close('all')
