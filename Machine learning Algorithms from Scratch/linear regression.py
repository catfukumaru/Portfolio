import numpy as np
from sklearn.datasets import make_regression    
# purpose of linear regression:get a straights line that is passes through the middle of our data points

# the equation for a linear line is: y = m*X + b
#X is numeric, single-valued. Here m and b represent the gradient(weight) and y-intercept (or bias)
#X is dependent on the data, and so are the y values. We only have control over m and b, that act as our model parameters. the aim is to find the best values of m and b

class LinearRegression:
    def __init__(self, learning_rate: int = 0.01, number_iterations: int = 1000) -> None:
        self.learning_rate = learning_rate # The learning rate (or alpha) controls the size of the nudges the radient decent takes
        self.number_iterations = number_iterations
        self.weights = None # gradient
        self.bias = None # y-intercept
        # weight and bias a re set to none because they depend on the x and y values 

    def fit(self, X, y): # x and y are the x and y values
        num_samples, num_features = X.shape     # X shape [N, f]
        self.weights = np.random.rand(num_features)  # W shape [f, 1] # randomly initialize the weights given the number of input features. So now our weights are also a NumPy array of size (num_features, )
        self.bias = 0 #  Bias is a single value initialized to zero.

        for i in range(self.number_iterations):

            # y_pred shape should be N, 1
            y_pred = np.dot(X, self.weights) + self.bias  #instead of an iterative approach to sum all values, we can follow a vectorized approach for faster computation. Given that the weights and X values are NumPy arrays, we can use matrix multiplication to get predictions.  
            # In linear regression, predicting output values (ŷ) involves computing a weighted sum across input features (X) plus a bias term for each data point. The quoted section contrasts a slow, explicit loop that iterates over features (e.g., for loop summing w1*x1 + w2*x2 + ...) with a faster "vectorized" method using NumPy's array operations  

            #We are using randomly initialized values for the weights and bias, so the predictions will also be random. 

            #to get the optimal we use the Gradient Descent - If the line is bad, the computer slightly nudges the two numbers to try to make the loss smaller. We take the gradient with respect to each weight value and then move them to the opposite of the gradient. This pushes the the loss towards minimum.
            #  find the difference between both values using the MSE (Mean Square Error ) 
            #For our predictions to be as close to original targets as possible, we now try to make the mse as small as possible

           # Mean Squared Error (MSE) loss function measures prediction errors, forming a u-shaped surface when plotted against model parameters like weights and bias. The minimum loss occurs at the bottom of this "u," where the slope (gradient) flattens to zero - the bottom of the u- , indicating no further improvement direction.

        #The gradient is like a list of slopes( vector of partial derivatives)—one for each setting in your model—showing which way the error goes up or down if you tweak that setting.

#Setting those slopes to zero finds the perfect model settings exactly (via the "normal equation"). But gradient descent gets close by repeatedly nudging settings downhill, against the slopes.

            # X -> [N,f] # dw is again of shape (num_features, ) So we have a separate derivate value for each weight
            # y_pred -> [N]
            # dw -> [f] #  db has a single value.
            #partial derivates of the MSE function with respect to weights and bias values
            dw = (1 / num_samples) * np.dot(X.T, y_pred - y)
            db = (1 / num_samples) * np.sum(y_pred - y)

            #the optimization equations
            #we move the values in the opposite direction of the gradient using basic subtraction.
        #     We only make a small change to the randomly initialized values. We now repeatedly perform the same steps, to converge towards a minimum.
            self.weights = self.weights - self.learning_rate * dw
            self.bias = self.bias - self.learning_rate * db

        return self

    def predict(self, X):
        # just put the values into the linear formula
        return np.dot(X, self.weights) + self.bias
    



X, y = make_regression(
        n_samples=500, n_features=1, noise=15, random_state=4) #generates random linear regression datasets, with added Gaussian noise to add some randomness.


#The independent feature X will be a NumPy array of shape (num_samples, num_features). In our case, the shape of X is (500, 1). i.e. a super long column


#Each row in our data will have an associated target value, so y is also of shape (500,) or (num_samples).

print(f"first 5 X values{X[:5]}")
print(f"y values{y[:5]}")
lr_object = LinearRegression()
lr_object.fit(X,y)
print(f"the predicted values{lr_object.predict(X)[:5]}")