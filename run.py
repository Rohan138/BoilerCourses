import pandas as pd
import numpy as np
import csv
import sys

print('Loading catalog')
data = pd.read_csv('catalog.csv')
print('Loading scores')
vec = np.genfromtxt('scores.csv', delimiter=',')
mul = vec@vec.T

courses = data['Course']
cname = input("Enter course to reference:")
if cname not in courses:
    print('Course not found')
    sys.exit(1)

school, number = cname.split()
common = data(data['School'] == school)
other = data(data['School'] != school)