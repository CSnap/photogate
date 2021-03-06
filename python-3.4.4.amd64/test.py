import matplotlib.pyplot as plt
import random
import time
items = [25.5,26.7,23.4,22.5,20,13.4,15.6,-12,-16,20]
x = [1,2,3,4,5,6,7,8,9,10]

plt.ion() #  Interactive on

for i in range(1,100):
    plt.title('graph plotting')
    plt.ylabel('temperature') 
    plt.xlabel('time')
    random.shuffle(items)
    plt.plot(x,items,'ob-')
    plt.axis([0, 10, -40, 40])
    plt.draw()
    #time.sleep(2)
    plt.clf()
    plt.close()
