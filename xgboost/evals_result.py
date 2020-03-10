from sklearn.datasets import load_iris
import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split


# read in the iris data
iris = load_iris()

X = iris['data']
y = iris['target']

X, y = X[y != 2], y[y != 2]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234565)


"""
### load data in do training
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# param = [('max_depth', 2), ('objective', 'binary:logistic'), ('eval_metric', 'logloss'), ('eval_metric', 'error'), ('n_estimators',2)]
param = {'max_depth': 2, 'objective': 'binary:logistic', 'eval_metric': ['logloss', 'error'], 'n_estimators': 2}
num_round = 2
watchlist = [(dtest,'eval'), (dtrain,'train')]

evals_result = {}
bst = xgb.train(param, dtrain, num_round, watchlist, evals_result=evals_result)

print('Access logloss metric directly from evals_result:')
print(evals_result['eval']['logloss'])


print('')
print('Access complete dictionary:')
print(evals_result)

"""
param_dist = {'objective': 'binary:logistic', 'n_estimators': 2}

clf = xgb.XGBModel(**param_dist)

clf.fit(X_train, y_train,
        eval_set=[(X_train, y_train), (X_test, y_test)],
        eval_metric=['logloss', 'error'],
        verbose=True)

evals_result = clf.evals_result()
print(evals_result)
