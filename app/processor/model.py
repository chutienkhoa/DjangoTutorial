import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from repository.models import DataModel, DrawTable, UserModel

data_csv = pd.read_csv("../data/iris.csv")
data = data_csv.values
X = data[:, 0:4]
y = data[:, 4]
labelIndexer = preprocessing.LabelEncoder()
y_indexer = labelIndexer.fit_transform(y)
validation_size = 0.2
seed = 7
X_train, X_validation, y_train, y_validation = train_test_split(X, y_indexer, test_size=0.3, random_state=seed)
num_folds = 10
num_instances = len(X_train)
seed = 7
scoring = 'accuracy'
models = []
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = KFold(n_splits=10)
    cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())

    # data_model = DataModel()
    # # print(name)
    # data_model.model_name = name
    # data_model.precision = cv_results.mean()
    # data_model.recall = cv_results.std()
    # data_model.accuracy = cv_results.std()+cv_results.mean()
    # DataModel.objects.get_or_create(model_name=name,
    #                                 precision=cv_results.mean(),
    #                                 recall=cv_results.std(),
    #                                 accuracy=(cv_results.std() + cv_results.mean()))

aaa = DataModel()
test_data_model = aaa.get_data_model_by_name(model_name="SVM")
for mo in test_data_model:
    # print(mo)
    print(mo.precision)
    print(mo.recall)
