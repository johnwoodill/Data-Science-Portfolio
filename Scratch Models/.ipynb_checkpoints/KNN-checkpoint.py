# Adapted from https://pythonprogramming.net/coding-k-nearest-neighbors-machine-learning-tutorial/

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
from math import sqrt
from collections import Counter
style.use('fivethirtyeight')

def normalize(d):
    return (d - np.mean(d))/np.std(d)

def k_nearest_neighbors(data, predict, k=3, scale=False):
    
    # Check to make sure
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups!')
        
    if scale == False:
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
    
    # To utilize correlation distance, simply scale and use Euclidean distance squared
    if scale == True:
        
        # Empty lists
        distances2 = []
        means = []
        sd = []
        
        # Normalize train and test data
        for iter in data:
            # Get means and sd for predictive values
            means.append(np.mean(data[iter]))
            sd.append(np.std(data[iter]))
            
            # Normalize data
            data[iter] = normalize(data[iter])

        # Normalize test data based on train data mean and sd
        for i in range(0, len(predict)):
            for j in range(len(predict[0])):
                predict[i][j] = (predict[i][j] - means[j])/sd[j]
        
        # Now calculate E. Squared Distance
        for group in data:
            for features in data[group]:
                euclidean_distance2 = np.linalg.norm(np.array(features)-np.array(predict))
                distances2.append([euclidean_distance2,group])
                
        # Sort values in distances and get K closests observations
        votes = [i[1] for i in sorted(distances2)[:k]]

        # Get vote by most common group
        vote_result = Counter(votes).most_common(1)[0][0]
        return vote_result
        
        
        
        

# Train data set
dataset = {'k':[[1,2],[2,3],[3,1], [1, 3], [2, 2], [3, 3], [4, 4], [2, 5]], 'r':[[6,5],[7,7],[8,6], [6, 6], [7, 6], [8, 7], [8, 4]]}

# Test data set
new_features = [1, 1]

# Plot train set
[[plt.scatter(ii[0],ii[1],s=100,color=i) for ii in dataset[i]] for i in dataset]

# Plot test set
plt.scatter(new_features[0], new_features[1], s=100)

# Calculate KNN using test based on train set
result = k_nearest_neighbors(dataset, new_features, scale=False)

# Plot predicted results
plt.scatter(new_features[0], new_features[1], s=100, color = result) 
plt.show()
