import pandas as xd
import numpy as cv
data = {
  "Name" : [ 'Juan' , 'Ana' , 'Luis' , 'Maria'],
  "Age"  : [ 15 , 14 , 16 , 15],
  "Note"  : [ 8.5 , 9.0 , 7.5 , 8.0],
  "City" : ['Madrid' , 'Barcelona' , 'Valencia' , 'Sevilla']
}

df = xd.DataFrame(data)
print(df)
