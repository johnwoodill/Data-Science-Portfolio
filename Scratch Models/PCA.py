import numpy as np
import sklearn
from sklearn.utils import extmath   # svd_flip()

def normalize_data(d, type):
    if type == "center":
        return (d - d.mean(axis=0))

    if type == "standardize":
        return (d - d.mean(axis=0)) / np.std(d, axis=0)
    
# Flip signs to enforece deterministic output
# Function from scikitlearn svd_flip()
def svd_flip(u, v):
        # columns of u, rows of v
        max_abs_cols = np.argmax(np.abs(u), axis=0)
        signs = np.sign(u[max_abs_cols, range(u.shape[1])])
        u *= signs
        v *= signs[:, np.newaxis]
        return (u, v)
    
class PCAnalysis():
    def __init__(self, data, scale):
        self.data = data
        self.scale=scale
        self.PC=None
        self.explained_variance = None
        self.total_var=None
        self.explained_variance_ratio=None
        self.n_samples, self.n_features = data.shape
                
    def get_PC(self):

        if self.scale == True:
            X = normalize_data(self.data, "center")
        if self.scale == False:
            X = self.data

        # Get cov matrix
        # Cov matrix ok
        V = np.cov(X.T)

        # Get eigance values and vectors
        values, S, vectors = np.linalg.svd(V, full_matrices=False)
        
        # Flip eigenvectors' sign to enforce deterministic output
        values, vectors = extmath.svd_flip(values, vectors)

        # Project data
        P = values.T @ X.T
        self.PC = P.T
        self.explained_variance_ = S
        total_var = self.explained_variance_.sum()
        self.explained_variance_ratio_ = self.explained_variance_ / total_var
        self.sum_explained_variance_ = self.explained_variance_ratio_.cumsum()
        
        return self.PC
  
   
X = np.array([[1, 2], [3, 4], [5, 6]])

# Define a matrix
X = np.array([7,4,6,8,8,7,5,9,7,8,4,1,3,6,5,2,3,5,4,2,3,8,5,1,7,9,3,8,5,2]).reshape(3, 10).T
PCA_X = PCAnalysis(X, scale=True)
PCA_X.get_PC()
PCA_X.explained_variance_
PCA_X.explained_variance_ratio_
PCA_X.sum_explained_variance_

#------------------------------------------------
# Check with sklearn
from sklearn.decomposition import PCA
pca = PCA(3)
pca.fit(X)
pca.components_
#array([[ 0.70710678,  0.70710678],
#       [ 0.70710678, -0.70710678]])

#array([[ 0.1375708 ,  0.25045969, -0.95830278],
#       [ 0.69903712,  0.66088917,  0.27307986],
#       [ 0.70172743, -0.70745703, -0.08416157]])

pca.transform(X)
#array([[ -2.82842712e+00,   2.22044605e-16],
#       [  0.00000000e+00,   0.00000000e+00],
#       [  2.82842712e+00,  -2.22044605e-16]])

#array([[ 2.15142276, -0.17311941, -0.10681648],
#       [-3.80418259, -2.88749898, -0.5104355 ],
#       [-0.15321328, -0.98688598, -0.26941001],
#       [ 4.7065185 ,  1.30153634, -0.65167999],
#       [-1.29375788,  2.27912632, -0.44919235],
#       [-4.0993133 ,  0.1435814 ,  0.80312818],
#       [ 1.62582148, -2.23208282, -0.80281431],
#       [-2.11448986,  3.2512433 ,  0.16837351],
#       [ 0.2348172 ,  0.37304031, -0.27513962],
#       [ 2.74637697, -1.06894049,  2.09398657]])

pca.explained_variance_
#array([  8.00000000e+00,   2.25080839e-33])
#array([ 8.27394258,  3.67612927,  0.74992815])

pca.explained_variance_ratio_
#array([ 0.65149154,  0.289459  ,  0.05904946])

pca.explained_variance_ratio_.cumsum()
#array([ 0.65149154,  0.94095054,  1.        ])
