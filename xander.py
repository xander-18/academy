import pandas as xd
import numpy as cv
# data = {
#   "Name" : [ 'Juan' , 'Ana' , 'Luis' , 'Maria'],
#   "Age"  : [ 15 , 14 , 16 , 15],
#   "Note"  : [ 8.5 , 9.0 , 7.5 , 8.0],
# #   "City" : ['Madrid' , 'Barcelona' , 'Valencia' , 'Sevilla']
# }
# df = xd.DataFrame(data)
# df['Cuidad'] = ['Madrid' , 'Barcelona' , 'Valencia' , 'Sevilla']
# print(df)

# cv.random.rand(10)
df_numeros_random = cv.random.randint(1,11, size=5) 
df_numeros = xd.DataFrame(df_numeros_random, columns=['Numeros'])
df_numeros['Dobles'] = df_numeros ['Numeros']*2
print(df_numeros)

df_numeros_random = cv.random.randint