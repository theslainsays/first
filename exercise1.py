#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

xi_start, xi_end = 2, 465
yi_start, yi_end = 2, 465

xi = np.genfromtxt('data.Montoya.txt', usecols=(1))
yi = np.genfromtxt('data.Montoya.txt', usecols=(2))

xi = xi[xi_start - 0:xi_end]
yi = yi[yi_start - 0:yi_end]

xs_start, xs_end = 466, 1154
ys_start, ys_end = 466, 1154

xs = np.genfromtxt('data.Montoya.txt', usecols=(1))
ys = np.genfromtxt('data.Montoya.txt', usecols=(2))

xs = xs[xs_start - 0:xs_end]
ys = ys[ys_start - 0:ys_end]

xa_start, xa_end = 1155, 1679
ya_start, ya_end = 1155, 1679

xa = np.genfromtxt('data.Montoya.txt', usecols=(1))
ya = np.genfromtxt('data.Montoya.txt', usecols=(2))

xa = xa[xa_start - 0:xa_end]
ya = ya[ya_start - 0:ya_end]
#print ' x=', x, '\n\n y=', y

plt.plot(xi, yi, 'r')
plt.plot(xs, ys, 'b')
plt.plot(xa, ya, 'g')
plt.xlabel('time')
plt.ylabel('value')
plt.show()

#when looking at the data.Montoya
#range, min, max, etc
#data centers are of different time zones
#data recorded over span of 1 day
#Didn't know what RTB.requests meant, until day after completing this code (7/1)
#RTB stands for Real-Time Bidding, and RTB.requests refers to the number of requests (value?) and when (time)
#data centers I and S had similiar trends going accross time, so I assume they're both in the same country, most likely US.
#looking closely at A's graph, it appears it must be on the other side of the world (somewhere in Europe), because it peaks whenever I and S reach their lowest points (excluding negative numbers), and A goes low when I and S go high.