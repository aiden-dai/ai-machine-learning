from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd

titanic_dataset = pd.read_csv('data/titanic.csv')

titanic_dataset = titanic_dataset.drop(
    ['fare', 'who', 'adult_male', 'deck', 'embark_town', 'class', 'alive', 'alone', 'sibsp', 'parch'], axis=1)
titanic_dataset = titanic_dataset.dropna()

print(titanic_dataset.head(5))


# Pre processing

# We create the preprocessing pipelines for both numeric and categorical data.

numeric_features = ['age']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())])

categorical_features = ['embarked', 'sex', 'pclass']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])


# Append classifier to preprocessing pipeline.
# Now we have a full prediction pipeline.
clf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', LogisticRegression(solver='lbfgs'))])

X = titanic_dataset.drop('survived', axis=1)
y = titanic_dataset['survived']

"""
y = titanic_dataset.pop('survived')
X = titanic_dataset

"""
print(X.head(5))
print(y.head(5))


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

print(len(X_train))


clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))


clf1 = Pipeline(steps=[('preprocessor', preprocessor),
                       ('classifier',  xgb.XGBClassifier(objective='binary:logistic', eval_metric=['error', 'logloss']))])

"""
# clf = xgb.XGBModel(**param_dist)

clf.fit(X_train, y_train,
        eval_set=[(X_train, y_train), (X_test, y_test)],
        eval_metric=['logloss', 'error'],
        verbose=True)

evals_result = clf1.evals_result()
print(evals_result)
"""
clf1.fit(X_train, y_train)
print(clf1.score(X_test, y_test))

clf2 = Pipeline(steps=[('preprocessor', preprocessor),
                       ('classifier', DecisionTreeClassifier())])
clf2.fit(X_train, y_train)
print(clf2.score(X_test, y_test))

clf3 = Pipeline(steps=[('preprocessor', preprocessor),
                       ('classifier', RandomForestClassifier(n_estimators=10))])
clf3.fit(X_train, y_train)
print(clf3.score(X_test, y_test))


"""
Preprocessing 2 

"""

enc = OrdinalEncoder()
# categorical_features = ['embarked', 'sex', 'pclass']


print(X.head())

X['sex'] = enc.fit_transform(X['sex'].values.reshape(-1, 1))
X['embarked'] = enc.fit_transform(X['embarked'].values.reshape(-1, 1))
print(X.head())
