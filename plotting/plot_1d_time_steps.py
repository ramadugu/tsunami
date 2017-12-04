"""
plot_1d_time_steps.py

Reads output of tsunami and plots the results in an image file,
one image file per time step.
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='text file output by tsunami simulator')
args = parser.parse_args()

input_file = args.input_file

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# read data into a list
data = [line.rstrip().split() for line in open(input_file).readlines()]

time = [float(line[0]) for line in data]
u = np.array([[float(x) for x in line[1:]] for line in data])
x = np.arange(1, u.shape[1]+1)
time_steps = [0, 25, 50, 75]

for n in range(len(time)):
    print(n)
    fig = plt.figure(figsize=(8,3))
    ax = fig.add_axes((0.12, 0.2, 0.8, 0.7))
    ax.tick_params(axis='both', which='major', labelsize=16)
    plt.ylim(-1,1)
    plt.xlim(1,100)
    plt.xticks(range(25,125,25))
    x = np.arange(1,101)
    plt.plot(x, u[n], 'b-')
    plt.fill_between(x, 0, u[n], color='b', alpha=0.4)
    plt.grid(True)
    plt.xlabel('Spatial grid index',fontsize=16)
    plt.ylabel('Amplitude',fontsize=16)
    plt.title(r'Initial state, $u(x, 0)$', fontsize=16)
    plt.savefig('u_'+'%3.3i' % n+'.png',dpi=100)
    plt.close(fig)
