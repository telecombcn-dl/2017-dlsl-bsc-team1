from __future__ import print_function
import os
import numpy as np
import matplotlib.pyplot as plt

fp = open('metrics.txt','r')
acc=[]
loss=[]
val_acc=[]
val_loss=[]

for line in iter(fp):
    l=line.split(',')
    acc.append(l[0][1:len(l[0])-1])
    loss.append(l[1][1:len(l[1])-1])
    val_acc.append(l[2][1:len(l[2]) - 1])
    val_loss.append(l[3][1:len(l[3]) - 2])
fp.close()
plt.plot(loss)
plt.plot(val_loss)
plt.show()