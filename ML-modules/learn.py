import numpy as np
# import sklearn.cross_validation as skcv
import sklearn.svm as sksvm
import sklearn.grid_search as skgs
import sklearn.linear_model as sklm
# import data

class Learn:

    # This method wil initialize the model(s) and train them using the data interface
    # The data is expected to be a numpy array of the shape: (n_samples, n_features)
    def init(self):
        return NotImplemented

    def predict(self, new_sample):
        return NotImplemented

def logisticRegressionGridSearch(X, y):
    param_grid = [{'penalty':['l1', 'l2'], 'dual': [False], 'C': np.logspace(-3.20,10), 'solver':['sag']}]
    grid_search = skgs.GridSearchCV(sklm.LogisticRegression(), param_grid, cv=5)
    grid_search.fit(X,y)
    print 'Best Score of Grid Search: ' + str(grid_search.best_score_)
    print 'Best Params of Grid Search: ' + str(grid_search.best_params_)


def svcSIGMOIDGridSearch(X, y, Test):
    param_grid = [{'C': np.logspace(-3.20,10), 'gamma': np.logspace(-5,3,20), 'kernel': ['sigmoid']}]
    grid_search = skgs.GridSearchCV(sksvm.SVC(), param_grid, cv=5)
    grid_search.fit(X,y)
    print 'Best Score of Grid Search: ' + str(grid_search.best_score_)
    print 'Best Params of Grid Search: ' + str(grid_search.best_params_)

def svcPOLYGridSearch(X, y, Test):
    param_grid = [{'degree': np.linspace(1,10,10),'C': np.logspace(-3.20,10), 'gamma': np.logspace(-5,3,20), 'kernel': ['poly']}]
    grid_search = skgs.GridSearchCV(sksvm.SVC(), param_grid, cv=5)
    grid_search.fit(X,y)
    print 'Best Score of Grid Search: ' + str(grid_search.best_score_)
    print 'Best Params of Grid Search: ' + str(grid_search.best_params_)

def svcRBFGridsearch(X, y, Test):
    param_grid = [{'C': np.logspace(-1,20,10), 'gamma': np.logspace(-5,3,20), 'probability':[True, False], 'kernel': ['rbf']}]
    grid_search = skgs.GridSearchCV(sksvm.SVC(), param_grid, cv=5)
    grid_search.fit(X,y)
    print 'Best Score of Grid Search: ' + str(grid_search.best_score_)
    print 'Best Params of Grid Search: ' + str(grid_search.best_params_)

if __name__ == '__main__':
    print np.linspace(1,5,5)
        
