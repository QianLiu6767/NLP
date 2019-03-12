# !usr/bin/env python
# -*- coding:utf-8 -*-
# Author:LiuQian,time:2019/3/12

# -------------------------数据聚类------------------------------
from collections import Counter

from sklearn.mixture import GaussianMixture
from sklearn.naive_bayes import GaussianNB
from sklearn.decomposition import PCA

import numpy as np
import seaborn as sns

iris = sns.load_dataset("iris")

pca = PCA(n_components=2)
model = GaussianMixture(n_components=3, covariance_type="full")
model2 = GaussianNB()

X, y = pca.fit_transform(iris.iloc[:, :-1]), iris.iloc[:, -1]

y = y[:, np.newaxis]

model.fit(X, y)
predict_value = model.predict(X)


iris['PCA1'] = X[:, 0]
iris['PCA2'] = X[:, 1]
iris['cluster'] = predict_value

# 方式1：可视化选取
sns.lmplot('PCA1', 'PCA2', data=iris, hue='species', col='cluster', fit_reg=False);


test = iris[['cluster', 'species']]

# 方式2：
Counter(list(zip(test.cluster, test.species)))

# 方式3：
model2.fit(test.cluster[:, np.newaxis], test.species)

model2.predict([[0], [1], [2]])