# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 22:29:20 2021

@author: jiang
"""
import numpy as np


def RMSE(y_true, y_pred):
    rmse = np.sqrt(np.nanmean((y_true - y_pred)**2))
    return rmse
