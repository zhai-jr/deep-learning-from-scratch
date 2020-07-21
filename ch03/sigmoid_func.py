import numpy as np
import matplotlib.pyplot as plt

def sigmoid_function(x):
	return 1 / (1 + np.exp(-x))
	
def step_function(x):
	return np.array(x > 0, dtype = np.int)
	
def relu_function(x):
	return np.maximum(0, x)
	
x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid_function(x)
y2 = step_function(x)
y3 = relu_function(x)

plt.plot(x, y1, label="sigmoid")
plt.plot(x, y2, linestyle = "--", label="step")
plt.plot(x, y3, label="relu")
plt.ylim(-0.1, 1.1)
plt.show()