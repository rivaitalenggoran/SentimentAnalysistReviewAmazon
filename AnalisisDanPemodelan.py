import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

filepath = 'Dataset//Electronics_sampled.csv'
data = pd.read_csv(filepath)

#Analisis Menggunakan Statistika Deskriptif--------------------------------------------------------

#Rata-Rata-----------------------------------------------------------------------------------------
mean_Rating = data['rating'].mean()
print("Rata-Rata Rating : ", math.floor(mean_Rating))

#Median Rating---------------------------------------------------------------------------------------
median_Rating = data['rating'].median()
print("Median Rating : ", math.floor(median_Rating))

#Modulo Rating---------------------------------------------------------------------------------------
modulo_Rating = data['rating'].std()
print("Modulo Rating : ", math.floor(modulo_Rating))

#Varian Rating---------------------------------------------------------------------------------------
varian_Rating = data['rating'].var()
print("Varian Rating : ", math.floor(varian_Rating))

#Minimum Rating---------------------------------------------------------------------------------------
minimum_Rating = data['rating'].min()
print("Minimum Rating : ", math.floor(minimum_Rating))

#Maksimal Rating---------------------------------------------------------------------------------------
maximum_Rating = data['rating'].max()
print("Maximum Rating : ", math.floor(maximum_Rating))


#Analisis Sentimen Pengguna Melalui Review------------------------------------------------------------
#Polaritas Text review