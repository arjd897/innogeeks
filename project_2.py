import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
X=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
Y=np.array([33,36,35,34,33,28,29,33,34,32,29,30,34,31,32,26,29,28,33,34])
plt.scatter(X,Y,color='blue')
plt.xlabel('days')
plt.ylabel('temp(in degrees)')

m=0
c=0
L=0.001

n=100000
for i in range(n):
    Y_pred=m*X+c
    D_m = (-2/n)*sum(X*(Y-Y_pred))
    D_c = (-2/n)*sum(Y-Y_pred)
    m=m-L*D_m
    c=c-L*D_c
Y_pred = m*X+c
plt.scatter(X,Y)
plt.plot([min(X),max(X)],[min(Y_pred),max(Y_pred)],color='red')
plt.show()
'''a=input('enter the value of X to predict Y')
b=m*a+c
print('the value of Y is',b)'''