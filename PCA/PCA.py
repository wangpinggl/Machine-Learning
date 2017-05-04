import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
    
if __name__ == '__main__':
    data = pd.read_csv('datamatrix.csv')
    data = data.as_matrix()[:,1:]
    S = np.cov(data)
    print S
    eig_value, eig_vector = np.linalg.eig(S)
    index = np.argsort(eig_value)[::-1]
    print eig_vector
    print eig_value
    X = data.T.dot(eig_vector[index[:2]].T)
    plt.scatter(X[:,0],X[:,1])
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('2D plot')
    plt.show()