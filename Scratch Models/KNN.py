# Adapted from https://pythonprogramming.net/coding-k-nearest-neighbors-machine-learning-tutorial/

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
from math import sqrt
from collections import Counter
style.use('fivethirtyeight')

def k_nearest_neighbors(data, predict, k=3):
    
    # Check to make sure
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups!')
        
    # List of Euclidean distances    
    distances = []
    
    # Get each group and calculate distance from predicted values
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance,group])
    
    # Sort values in distances and get K closests observations
    votes = [i[1] for i in sorted(distances)[:k]]
    
    # Get vote by most common group
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result

# Train data set
dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}

# Test data set
new_features = [5,7]

# Plot train set
[[plt.scatter(ii[0],ii[1],s=100,color=i) for ii in dataset[i]] for i in dataset]
# same as:
##for i in dataset:
##    for ii in dataset[i]:
##        plt.scatter(ii[0],ii[1],s=100,color=i)

# Plot test set
plt.scatter(new_features[0], new_features[1], s=100)

# Calculate KNN using test based on train set
result = k_nearest_neighbors(dataset, new_features)

# Plot predicted results
plt.scatter(new_features[0], new_features[1], s=100, color = result)  
plt.show()
