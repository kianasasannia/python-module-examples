import random
import matplotlib.pyplot as plt

x=[]
for u in range(0,25):
    a=random.randint(10,50)
    x.append(a)
y=[]
for o in range(0,25):
    b=random.randint(10,50)
    y.append(b)


plt.plot(x,y)
plt.show()

