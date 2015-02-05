
import numpy as np
import scipy.spatial.distance as distance

def compare(gest1, gest2):
    # distance matrix
    d = np.ndarray([gest1.shape[0], gest2.shape[0]])

    for i in np.arange(gest1.shape[0]):
        for j in np.arange(gest2.shape[0]):
            d[i,j] = distance.pdist(np.array([gest1[i],gest2[j]]))

    print d

if __name__=="__main__":
    cl0 = np.loadtxt('samples/cl0.points')
    cl1 = np.loadtxt('samples/cl1.points')

    print compare(cl0, cl1)
