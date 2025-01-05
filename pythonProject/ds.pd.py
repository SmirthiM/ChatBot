import matplotlib.pyplot as plt
import numpy as np
x = np.array([10,20,30,40,50])
y = np.array([100,200,350,400,550])
plt.plot(x,marker='o',ms=8,mec='green',mfc='pink')
plt.plot(y)
font1={""}
plt.title("Average limit")
plt.xlabel("Time")
plt.ylabel("Speed")
plt.show()