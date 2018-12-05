# Adaptated from: https://github.com/sourabhdattawad/Linear-regression-from-scratch-in-python/blob/master/LinearRegression.ipynb

import numpy as np
import random
import sklearn
from sklearn.datasets.samples_generator import make_regression 
import pylab
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


def gradient_descent(alpha, x, y, conv=0.0001, max_iter=1000):
    converged  = False
    iter = 0
    m = len(x) #Number of samples
    t0 = np.random.random(x.shape[1]) #Initial value of beta0
    t1 = np.random.random(x.shape[1]) #Initial value of beta1

    # Initial Error
    J = sum([(y[i] - (t0 + t1*x[i]))**2 for i in range(m)])
    
    while not converged:
        
        # Loss function
        loss_fn = 1.0/m*sum([(y[i] - (t0 + t1*x[i]))**2 for i in range(m)])

        # Derivative of loss function w.r.t. c (grad0) and m (grad1)
        grad0 = -2.0/m*(sum([(y[i] - (t0+t1*x[i])) for i in range(m)]))
        grad1 = -2.0/m*(sum([(y[i] - (t0+t1*x[i]))*x[i] for i in range(m)]))
        
        # Update betas
        t0 = t0 - alpha * grad0
        t1 = t1 - alpha * grad1
        
        # Calculate RSE
        e = sum( [ (y[i] - (t0 + t1*x[i]))**2 for i in range(m)] )
        
        # Convergence takes place either 
        # 1)after completing all the iterations or 
        # 2)if error difference current and prev is less than some value here(0.0001)
        
        if abs(J-e)<conv:
            print ("Converged successfully")
            converged = True
        
        
        if iter==max_iter:
            converged = True
        
        J=e
        iter+=1
        
    return t0,t1

    
#Dummy dataset
x, y = make_regression(n_samples=1000, n_features=1, n_informative=1, random_state=0, noise=100) 

# Learning Rate
alpha = 0.01

# Converge on 
conv = 0.0001

# Estimate beta0, beta1
beta0, beta1 = gradient_descent(alpha, x, y, conv, max_iter=1000)

# Plot results
plt.scatter(x,y)
plt.plot(x, beta0+x*beta1, 'r')
plt.show()
plt.close()
