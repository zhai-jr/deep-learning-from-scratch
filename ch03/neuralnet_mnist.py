import sys, os
sys.path.append(os.pardir)

import pickle
import numpy as np
#from sigmoid_func import sigmoid_function
from dataset.mnist import load_mnist

def sigmoid_function(x):
	return 1 / (1+np.exp(-x))

def get_data():
	(x_train, t_train), (x_test, t_test) = \
	load_mnist(normalize=True, flatten=True, one_hot_label=False)
	
	return x_test, t_test
	
def init_network():
	with open("sample_weight.pkl", 'rb') as f:
		network = pickle.load(f)
		
	return network

def predict(network, x):
	W1, W2, W3 = network['W1'], network['W2'], network['W3']
	b1, b2, b3 = network['b1'], network['b2'], network['b3']
	
	A1 = np.dot(x, W1) + b1
	Z1 = sigmoid_function(A1)
	
	A2 = np.dot(Z1, W2) + b2
	Z2 = sigmoid_function(A2)
	
	y = np.dot(Z2, W3) + b3
	
	return y
	

x, t = get_data()
network = init_network()

batch_size = 100
accuracy_cnt = 0
for i in range(0, len(x), batch_size):
	x_batch = x[i:i+batch_size]
	y_batch = predict(network, x_batch)
	p = np.argmax(y_batch, axis=1)
	
	accuracy_cnt += np.sum(p == t[i:i+batch_size])

print("accuracy:" + str(float(accuracy_cnt) / len(x)))
