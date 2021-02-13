# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 21:55:49 2021

@author: jiang
"""
default_baseline_assumptions = {
    'revenue_yoy_growth_rate': ('avg', 3),
    'gross_margin': ('avg', 4),
    'other_expenses': ('last', 1),
    'tax_rate': ('last', 1),
    'share_outstanding': ('last', 1),
    'pe_ratio': ('const', 20)
    }

col_sort = [
    'year', 'total_revenues', 'revenue_yoy_growth_rate',
    'gross_profit', 'gross_margin', 'other_expenses', 'operating_income',
    'ebt', 'tax_rate', 'income_tax_expenses', 'net_income',
    'share_outstanding', 'eps', 'pe_ratio', 'share_price']
