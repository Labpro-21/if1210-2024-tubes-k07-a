# PROGRAM Random Number Generator Menggunakan LCG
# Writer: Adrian Sami Pratama
# Hari, tanggal: 28 April 2024
# Note: a, c, m fixed. kalau seed dirandomize sama os dan time.
#       Untuk menghasilkan random number dengan range 1 - N --> generate_number(lcg(a=48271, c=0, m=2**31-1, seed=None) ,[1, N+1])

import os
import time

def lcg(a=48271, c=0, m=2**31-1, seed=None): # C++11 minstd_rand
    x0 = seed

    if seed is None:
        x0 = int(os.getpid()*100 + time.time()*100) # Seed diambil dari nilai ini agar seed selalu berbeda setiap waktu
    else:
        x0 = seed # Seed adalah kondisi awal

    x_prev = (a * x0 + c) % m # Diambil dari rumus lcg X(n+1) = (aX(n) + c) mod m
    return x_prev

def generate_number(x_prev, num_range=None): # Fungsi ini bakal ngambil x_prev dari fungsi yang atas
    a=48271 
    c=0 
    m=2**31-1
    x_prev = (a * x_prev + c) % m

    if num_range is None:
        return x_prev
    else:
        return int((x_prev / (m - 1)) * (num_range[1] - num_range[0]) + num_range[0])

defaultlcg = lcg(a=48271, c=0, m=2**31-1, seed=None)
    
print(generate_number(defaultlcg ,[0,31]))                                                                