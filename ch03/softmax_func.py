import numpy as np

def softmax_function(x):
	x_max = np.max(x)
	x_exp = np.exp(x - x_max)
	
	return x_exp / np.sum(x_exp)
	
a = np.array([0.3, 2.9, 4.0])
y = softmax_function(a)

print(y)

print(np.sum(y))