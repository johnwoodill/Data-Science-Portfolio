import numpy as np

def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

# Approximate using softplus
def relu(x):
    return np.log(1 + np.exp(x))
    
def relu_derivative(x):
    return 1 / (1 + np.exp(-x))    


class NeuralNetwork:
    def __init__(self, x, y, activation, learning_rate=1):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4) 
        self.weights2   = np.random.rand(4,1)                 
        self.y          = y
        self.output     = np.zeros(self.y.shape)
        self.activation = activation
        self.learning_rate = learning_rate

    def feedforward(self):
        if self.activation == 'sigmoid':
            self.layer1 = sigmoid(np.dot(self.input, self.weights1))
            self.output = sigmoid(np.dot(self.layer1, self.weights2))
        elif self.activation == 'relu':
            self.layer1 = relu(np.dot(self.input, self.weights1))
            self.output = relu(np.dot(self.layer1, self.weights2))

    def backprop(self):
        
        if self.activation == 'sigmoid':
            # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
            d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
            d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))
        elif self.activation == 'relu':
            # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
            d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * relu_derivative(self.output)))
            d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * relu_derivative(self.output), self.weights2.T) * relu_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += self.learning_rate*d_weights1
        self.weights2 += self.learning_rate*d_weights2


if __name__ == "__main__":
    X = np.array([[0,0,1],
                  [0,1,1],
                  [1,0,1],
                  [1,1,1]])
    y = np.array([[1],[0],[1],[0]])
    nn = NeuralNetwork(X,y, 'sigmoid', 0.1)

    for i in range(1500):
        nn.feedforward()
        nn.backprop()

    print(nn.output)
