# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:04:51 2026

@author: Lenovo
"""

#%% ex 1 

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 0.1, 10000)

x = np.cos(520 * np.pi * t + np.pi/3)
y = np.cos(280 * np.pi * t - np.pi/3)
z = np.cos(120 * np.pi * t + np.pi/3)


plt.figure()
plt.grid(True)
plt.legend()
plt.axhline(0, color = 'purple')
plt.title("Axa numerelor reale")


plt.xlabel('t')
plt.ylabel('f(t)')

fig, axs = plt.subplots(3, 1, figsize=(10, 7), sharex=True)

axs[0].plot(t, x, color='blue')
axs[0].set_title(r'$x = \cos(520\pi t + \pi/3)$  (f = 260 Hz)')
axs[0].grid(True)

axs[1].plot(t, y, color='red')
axs[1].set_title(r'$y = \cos(280\pi t - \pi/3)$  (f = 140 Hz)')
axs[1].grid(True)

axs[2].plot(t, z, color='gray')
axs[2].set_title(r'$z = \cos(120\pi t + \pi/3)$  (f = 60 Hz)')
axs[2].set_xlabel('t [s]')
axs[2].grid(True)

plt.tight_layout()
plt.show()


plt.show() 

fs = 200  
Ts = 1 / fs  

t_n = np.arange(0, 0.03 + Ts, Ts)

x_n = np.cos(520 * np.pi * t_n + np.pi/3)
y_n = np.cos(280 * np.pi * t_n - np.pi/3)
z_n = np.cos(120 * np.pi * t_n + np.pi/3)

fig2, axs2 = plt.subplots(3, 1, figsize=(10, 8))
fig2.suptitle(f'(c) Semnale Eșantionate la fs = {fs} Hz')

axs2[0].stem(t_n, x_n, basefmt=" ", linefmt='turquoise', markerfmt='bo')
axs2[0].set_ylabel('x[n]')
axs2[0].grid(True)
axs2[0].set_title('Eșantioane x[n]')

axs2[1].stem(t_n, y_n, basefmt=" ", linefmt='salmon', markerfmt='ro')
axs2[1].set_ylabel('y[n]')
axs2[1].grid(True)
axs2[1].set_title('Eșantioane y[n]')

axs2[2].stem(t_n, z_n, basefmt=" ", linefmt='lime', markerfmt='go')
axs2[2].set_ylabel('z[n]')
axs2[2].set_xlabel('t [s]')
axs2[2].grid(True)
axs2[2].set_title('Eșantioane z[n]')

plt.tight_layout()
plt.show()

#%% ex 2
fs_a = 8000  
N_a = 1600  
t_a = np.arange(N_a) / fs_a  

x_a = np.cos(2 * np.pi * 400 * t_a)

plt.figure(figsize=(10, 3))
plt.plot(t_a, x_a, color='blue')
plt.title('(a) Semnal sinusoidal 400 Hz, 1600 eșantioane')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.show()



fs_b = 8000 
T_b = 3     
t_b = np.arange(0, T_b, 1/fs_b)

x_b = np.cos(2 * np.pi * 800 * t_b)

plt.figure(figsize=(10, 3))
plt.plot(t_b, x_b, color='pink')
plt.title('(b) Semnal sinusoidal 800 Hz, durata 3 secunde')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.show()


fs_c = 10000
T_c = 0.05   
t_c = np.arange(0, T_c, 1/fs_c)
f_c = 240

x_c = 2 * np.mod(t_c * f_c, 1) - 1

plt.figure(figsize=(10, 3))
plt.plot(t_c, x_c, color='green')
plt.title('(c) Semnal sawtooth 240 Hz')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.show()



fs_d = 10000
T_d = 0.05
t_d = np.arange(0, T_d, 1/fs_d)
f_d = 300

x_d = np.sign(np.sin(2 * np.pi * f_d * t_d))

plt.figure(figsize=(10, 3))
plt.plot(t_d, x_d, color='purple')
plt.title('(d) Semnal square 300 Hz')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.show()

I_e = np.random.rand(128, 128)

plt.figure(figsize=(5, 5))
plt.imshow(I_e, cmap='gray')
plt.title('(e) Semnal 2D aleator (128x128)')
plt.colorbar()
plt.show()

I_f = np.zeros((128, 128))

y, x = np.ogrid[-64:64, -64:64]
masca_cerc = x**2 + y**2 <= 40**2
I_f[masca_cerc] = 1

plt.figure(figsize=(5, 5))
plt.imshow(I_f, cmap='gray')
plt.title('(f) Semnal 2D personalizat (Cerc)')
plt.show()

#%% Ex 3

fe = 2000 #nr esantioane

print ("Timpul intre doua esantioane este: ", 1/fe, " secunde.")

#o ora are 3600 de secunde si avem 2000 x 3600 = 7.200.000 apoi avem pentru 4 biti deci 28.800.000 si un byte are 8 biti deci 3.600.000

#deci intr o ora de achizitie o sa avem 3/600.000 de bytes.

print ("Nr de bytes intr o ora de achizitie este 3.600.000 bytes.")
