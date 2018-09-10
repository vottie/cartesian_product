# coding: utf-8

from cartesian_product  import CartesianProduct

a = ["a","b"]
b = ["1","2","3"]
c = ["@","?"]
d = ["A","B","C","D"]
e = ["000","111","123","789","0aje"]
f = ["!", "#", "+"]
g = ["91823", "kjk3", "lljk34"]
h = [333, 444, 536, 921, 5150, 512350]

matrix  = [a, b, c, d, e, f, g, h]
result  = []

p = CartesianProduct()
result = p.execute(matrix,result)
#p.show(result)
p.to_csv(result)
