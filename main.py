# coding: utf-8
import sys
import csv

from lib.cartesian_product import CartesianProduct

a = ["a","b"]
b = ["1","2","3"]
c = ["@","?"]
#d = ["A","B","C","D"]
#e = ["000","111","123","789","0aje"]
#f = ["!", "#", "+"]
#g = ["91823", "kjk3", "lljk34"]
#h = [333, 444, 536, 921, 5150, 512350]

if __name__ == '__main__':
    matrix = []

    f = open('input.csv','r')
    csv_data = csv.reader(f)
    for row in csv_data:
        print(row)
        matrix.append(row)

    result  = []

    p = CartesianProduct()
    result = p.execute(matrix,result)
    #p.show(result)
    p.to_csv(result)
