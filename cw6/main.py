import numpy as np
# # przyklad 1
# a= np.array([0,1])
# print(a)
# print(type(a))
# print(a.dtype)
# b = a.astype('float')
# print(b)
# print(b.dtype)
# print(b.shape)
# print(a.ndim)
# m = np.array([np.arange(2), np.arange(2)])
# print(m.shape)
# print(type(m))

# przyklad 2
from numpy import ndarray

# zera = np.zeros((5,5))
# jedynki = np.ones((4,4))
# print('----------------------')
# print(zera)
# print(jedynki)
# print(zera.dtype)
# print(jedynki.dtype)
# print('----------------------')
# pusta = np.empty((2,2))
# print(pusta)
# poz_1 = pusta[1,1]
# poz_2 = pusta[0,1]
# print(poz_1)
# print(poz_2)
# print('----------------------')
# liczby = np.arange(1,2,0.1)
# print(liczby)
# print('----------------------')
# liczby_lin = np.linspace(1,2,5)
# print(liczby_lin)
# print('----------------------')
# z = np.indices((2,2))
# print(z)
# print('----------------------')
# x, y = np.mgrid[0:6, 0:2]
# print(x)
# print(y)
# print('----------------------')
# mat_diag = np.diag([a for a in range(5)])
# print(mat_diag)
# print('----------------------')
# z = np.fromiter(range(5), dtype='int32')
# print(z)
# print('----------------------')
# bartek = 'bartek'
# bar_2= np.array(list(bartek))
# bar_3= np.array(list(b'bartek'))
# bar_6 = np.fromiter(bartek,dtype='S1')
# print(bar_2)
# print(bar_3)
# print(bar_6)
# print('----------------------')
#