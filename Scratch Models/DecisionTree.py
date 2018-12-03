class DecisionTree():
    def __init__(self, x, y, n_features, f_idxs,idxs,depth=10, min_leaf=5):
        self.x, self.y, self.idxs, self.min_leaf, self.f_idxs = x, y, idxs, min_leaf, f_idxs
        self.depth = depth
        print(f_idxs)
        self.n_features = n_features
        self.n, self.c = len(idxs), x.shape[1]
        #self.val = np.mean(y[idxs])
        self.val = np.mean(y[idxs])
        self.score = float('inf')
        self.find_varsplit()
        
def find_varsplit(self):



for i in self.f_idxs: self.find_better_split(i)
if self.is_leaf: return
x = self.split_col
lhs = np.nonzero(x <= self.split)[0]
rhs = np.nonzero(x > self.split)[0]
lf_idxs = np.random.permutation(self.x.shape[1])[:self.n_features]
rf_idxs = np.random.permutation(self.x.shape[1])[:self.n_features]
self.lhs = DecisionTree(self.x, self.y, self.n_features, lf_idxs, self.idxs[lhs], depth=self.depth-1, min_leaf=self.min_leaf)
self.rhs = DecisionTree(self.x, self.y, self.n_features, rf_idxs, self.idxs[rhs], depth=self.depth-1, min_leaf=self.min_leaf)

def find_better_split(self, var_idx):

y = dat.Price
x = dat[["CompPrice", "Income", "Advertising", "Population", "Age", "Education", "Urban", "US"]]

sample_sz = 100
n_features = 2
n = len(y)

idxs = np.random.permutation(len(y))[:sample_sz]
f_idxs = np.random.permutation(x.shape[1])[:n_features]

sort_x, sort_y = x.values[idxs,var_idx], y[idxs]
#sort_idx = np.argsort(x)
#sort_y, sort_x = y.iloc[sort_idx], x[sort_idx]
rhs_cnt, rhs_sum, rhs_sum2 = n, sort_y.sum(), (sort_y**2).sum()
lhs_cnt, lhs_sum, lhs_sum2 = 0,0.,0.

for i in range(0, n - min_leaf-1):

xi,yi = sort_x[i],sort_y.values[i]
lhs_cnt += 1; rhs_cnt -= 1
lhs_sum += yi; rhs_sum -= yi
lhs_sum2 += yi**2; rhs_sum2 -= yi**2
if i<self.min_leaf or xi==sort_x[i+1]:
    continue

lhs_std = std_agg(lhs_cnt, lhs_sum, lhs_sum2)
rhs_std = std_agg(rhs_cnt, rhs_sum, rhs_sum2)
curr_score = lhs_std*lhs_cnt + rhs_std*rhs_cnt
if curr_score<self.score: 
    self.var_idx, self.score, self.split = var_idx, curr_score, xi

@property
def split_name(self): return self.x.columns[self.var_idx]

@property
def split_col(self): return self.x.values[self.idxs,self.var_idx]

@property
def is_leaf(self): return self.score == float('inf') or self.depth <= 0 

def predict(self, x):
    return np.array([self.predict_row(xi) for xi in x])

def predict_row(self, xi):
    if self.is_leaf: return self.val
    t = self.lhs if xi[self.var_idx]<=self.split else self.rhs
    return t.predict_row(xi)


# Random Forest Regression Example
import pandas as pd
import numpy as np

dat = pd.read_csv("./data/carseats.csv")

y = dat.Price
x = dat[["CompPrice", "Income", "Advertising", "Population", "Age", "Education", "Urban", "US"]]

def __init__(self, x, y, n_trees, n_features, sample_sz, depth=10, min_leaf=10):
rf = RandomForest(x, y, 10, 2, 250, 10, 5)
rf.predict(x.iloc[:, 2])

def __init__(self, x, y, n_features, f_idxs,idxs,depth=10, min_leaf=5):
dt = DecisionTree(x, y, 5, f_idxs, idxs, 10, 5)
dt.predict(x)