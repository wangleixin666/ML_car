#!/usr/bin/env python    # -*- coding: utf-8 -*

"""
一个简单的小练习，涉及到文本信息的处理，待完成，只有一个baseline
来源：https://www.lintcode.com/ai/car-insurance-risk/overview
某保险公司销售一种汽车保险，需要对汽车状态进行评估。现在你需要设计一个算法模型，可以根据汽车的各项指标对汽车的投保风险进行打分
投保风险是从0到70的正整数，数值越大代表风险越高。
"""
import pandas as pd
# from sklearn.metrics import mean_squared_error

train = pd.read_csv('D:/kaggle/car/train.csv')
test = pd.read_csv('D:/kaggle/car/test.csv')

print train.info()
# print test.info()

features = ['Id', 'Col_1', 'Col_2', 'Col_3', 'Col_4', 'Col_5', 'Col_6', 'Col_7', 'Col_8', 'Col_9',
            'Col_10', 'Col_11', 'Col_12', 'Col_13', 'Col_14', 'Col_15', 'Col_16', 'Col_17', 'Col_18', 'Col_19',
            'Col_20', 'Col_21', 'Col_22', 'Col_23', 'Col_24', 'Col_25', 'Col_26', 'Col_27', 'Col_28', 'Col_29',
            'Col_30', 'Col_31', 'Col_32']

target = ['Score']

feature_of_object = ['Col_3', 'Col_4', 'Col_8', 'Col_9', 'Col_11', 'Col_12', 'Col_15', 'Col_17', 'Col_20',
                     'Col_22', 'Col_24', 'Col_25', 'Col_27', 'Col_28', 'Col_29', 'Col_32']
# category_columns = train.dtypes[train.dtypes == 'object'].index
features_encode = pd.get_dummies(feature_of_object)


# train = train_data(features_encode)
# (32000, 34)
# Must pass DataFrame with boolean values only

"""
对于非数值型数据如何进行处理
对于categorical type，是无法直接用于训练模型的，需要进一步处理成数值型，才可以用于后续操作
常用的encoding方式有两种：LabelEncoder、OneHotEncoder，sklearn中对这两种方式都做了实现，pandas中用get_dummies方法实现
在机器学习中用的最多的是哑编码（也就是Dummy coding或OneHotEncoder）, 当然如果某个特征的取值有成百上千个
用Dummy coding这种方式显然就不合适了，最好的方式是用LabelEncoder，或者更具这个特征的分布特征，把重要的几个取值和剩余的取值进行哑编码。
reg = lgb.LGBMRegressor()
reg.fit(train[features], train[target])

test['predict_score'] = reg.predict(test[features])

test[['Id', 'predicted_score']].to_csv('D:\kaggle\car\\first.csv', index=False)
"""

