import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix
    
if __name__ == '__main__':
    data = pd.read_csv('datamatrix.csv')
    data = data.as_matrix()[:,1:]
    dst_mat = distance_matrix(data.T, data.T, 2)
    dst_mat += np.eye(data.shape[1])*1e16
    
    n_neighbor = 100
    W = np.zeros([data.shape[1], data.shape[1]])
    for i in range(dst_mat.shape[1]):
        index = np.argsort(dst_mat[i])
        w = np.linalg.pinv(data.T[index].T).dot(data.T[i])
        W[i,index] = w
        
    M = np.eye(W.shape[1]) - W
    _, S, V = np.linalg.svd(M)
    
    index = np.argsort(S)
    print S[index[:3]]
    X = V[index[:3]]
        
    plt.scatter(X[0],X[1])
    plt.xlabel('x1')
    plt.ylabel('x2')
    #plt.title('2D plot')
    plt.show()
        
    
    