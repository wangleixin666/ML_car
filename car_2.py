#!/usr/bin/env python    # -*- coding: utf-8 -*
"""暴力的使用纯数值信息，不做任何处理，扔进xgboost中进行训练，得到结果"""

import pandas as pd
# import numpy as np
# import lightgbm as lgb
from xgboost import XGBClassifier
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import log_loss

import warnings

warnings.filterwarnings("ignore")

train = pd.read_csv('D:/kaggle/car/train.csv')
test = pd.read_csv('D:/kaggle/car/test.csv')

features = ['Id', 'Col_1', 'Col_2', 'Col_5', 'Col_6', 'Col_7', 'Col_10', 'Col_13',
            'Col_14', 'Col_16', 'Col_18', 'Col_19', 'Col_21', 'Col_23', 'Col_26', 'Col_30', 'Col_31']

target = ['Score']

clf = XGBClassifier()
clf.fit(train[features], train[target])

test['Score'] = clf.predict(test[features])

# test[['Id', 'Score']].to_csv('D:\kaggle\car\\first.csv', index=False)

