import pandas as pd
import numpy as np

a = pd.Series([1,2,3,5,5],index=["a","b","c","d","e"])
#print(a)

#print(a[2])
#print(a["c"])#
#print(a*2)     # entre outras operacoes '+' '-' '/' 
print(a.mean()) # 'median' 'mode' 'min' 'max'
print(a[:2])
print(a[-2:])




dict = {"a":1,"b":2,"c":3,"d":4,"e":5}
b = pd.Series(dict, index=["c","b","X","a","d","e"])
print(a.mul(b, fill_value=0))  #  'div'
print(b)

print("quantidade de números:",b.count())      # NaN não é contado
print("quantidade de elementos:",b.size)


c = pd.Series([[1, 2, 3], 'foo', [], [3, 4]])
print(c)

print(c.explode())     # observe os indices
print(c.explode(ignore_index = True))

d = pd.Series([4+3j,-1,4,4+3j])
print(d)
print(d.abs())

e = pd.Series([0, 1, np.nan, 3])
print(e)
print(e.interpolate(method='linear'))  #'linear', 'polynomial', 'from_derivatives'
