import numpy as np

def smp(mm, j):
    while 1:
        i = np.random.randint(mm)
        if i != j:
            break
    return i

if __name__ == '__main__':
    
    data = [[1,1,1],[2,2,1],[2,0,1],[2,1,1],[0,0,-1],[1,0,-1],[0,1,-1],[-1,-1,-1]]
    C = 0.2
    
    mm = len(data)
    nn = len(data[1]) - 1
    
    print mm, nn
    
    X = np.zeros([mm,nn])
    for i in range(mm):
        for j in range(nn):
            X[i,j] = data[i][j]
    print X
    
    y = np.zeros(mm)
    for i in range(mm):
        y[i] = data[i][nn]
    print y
    
    alpha = np.zeros(mm)
    print alpha
    
    w = np.random.random(nn)
    b = 0.0
    print w
    
    for k in range(100):
        for j in range(mm):
            i = smp(mm, j)
            
            L = 0
            H = 0
            if y[i] != y[j]:
                L = np.maximum(0, alpha[j] - alpha[i])
                H = np.minimum(C, C + alpha[j] - alpha[i])
            else:
                L = np.maximum(0, alpha[i] + alpha[j] - C)
                H = np.minimum(C, alpha[i] + alpha[j])
                
            ao_j = alpha[j]
            
            E = w.dot(X.T) + b - y
            eta = 2*X[i].dot(X[j]) - X[i].dot(X[i]) - X[j].dot(X[j])
            alpha[j] += -y[j]*(E[i]-E[j])/eta
            if alpha[j] > H:
                alpha[j] = H
            if alpha[j] < L:
                alpha[j] = L

            alpha[i] += y[i]*y[j]*(ao_j-alpha[j])
            
            w = alpha*y
            w = w.dot(X)
            bb = y - w.dot(X.T)
            b = np.mean(bb)
            
        print w, b   