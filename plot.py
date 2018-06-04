import numpy as np 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sys import stdin, argv

fig = plt.figure()
ax1 = fig.add_subplot(111)

data = np.zeros((int(argv[1]), int(argv[2]), 3), dtype=np.int64)
imobj = ax1.imshow(data)
fig.show()

counter = 0
x_lst = []
y_lst = []
num_lst = []

while True:
    line = stdin.readline().strip().split(',')
    if line == ['']:
        break
    else:
        x, y, r, g, b = [int(i) for i in line]
        data[x, y, 0] = r
        data[x, y, 1] = g
        data[x, y, 2] = b
        imobj.set_data(data)
        plt.draw()
        fig.canvas.flush_events()
