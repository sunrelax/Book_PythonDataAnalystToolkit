import numpy as np
np.array([[1,2,3],[4,5,6]])
np.array([[1,2,3],[4,5,6],[7,8,9]])
np.arange(1,300)
np.linspace(1,300,15)
np.zeros((4,4))
np.ones((4,4))
np.full((4,4),3)
np.empty((4,2))
np.repeat([1,2,3,4],5)
np.random.randint(1,100,5)
x=np.arange(0,10)
x.reshape(5,2)
x=np.arange(0,12).reshape(2,3,2)
x.shape=(6,2)
x.ravel()
type(x)
x[3]

import numpy as np
x=np.array([[1,2],[3,4]])
y=np.array([[6,7,8],[9,10,11]])
np.append(x,y)

x=np.array([[1,2],[3,4]])
y=np.array([[7,8],[10,11]])
np.dot(x,y)

np.concatenate((x,y),axis=1)
np.vstack((x,y))
np.hstack((x,y))
x=np.linspace(1,300,15)
np.all(x>20)
np.any(x>20)
x[np.where(x>20)]
x[~(x>200)]

x=np.arange(0,12).reshape(2,6)
y=np.arange(5,17).reshape(2,6)
x
y
x*y
x-y
x.ndim
x.nbytes
x.dtype
x
np.transpose(x)

import numpy.ma as ma
x=ma.masked_array([87,99,100,76,0],[0,0,0,0,1])
x[3]

x=ma.masked_array([87,99,100,76,0])
x.mask=[0,0,0,0,1]
x[4]=82
x.mask

x=np.arange(0,10).reshape(5,2)
x[x<5]
x[0]
x[:,0]

x=np.arange(0,10).reshape(5,2)
x.mean()
x.var()
x.std()
x.sum(axis=0)
x.cumsum()
x.max()
x=np.matrix([[2,3],[33,3],[4,1]])
x.mean()