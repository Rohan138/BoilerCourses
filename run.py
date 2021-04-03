import pandas as pd
import numpy as np
import csv
import sys

def top_k(a, k):
    ind = np.argpartition(a, -k)[0, -k:]
    ind = ind[np.argsort(a[0, ind])][::-1]
    return ind

print('Loading catalog')
data = pd.read_csv('catalog.csv')
print('Loading vectors')
vec = np.genfromtxt('vectors.csv', delimiter=',')
mul = vec@vec.T

courses = data['Course']
while True:
    course = input("Enter course to reference or q to quit: ")
    if course not in courses:
        if course != 'q':
            print('Course not found')
        print('Quitting')
        sys.exit(1)

    k = input('Enter number of courses to find: ')
    school, number = course.split()
    index = data[data['Course'] == course]['Index']
    common = data[data['School'] == school]
    other = data[data['School'] != school]
    common_index = common['Index']
    other_index = other['Index']
    common_mul = np.take(mul[index], common_index, axis=1)
    other_mul = np.take(mul[index], other_index, axis=1)
    common_max = top_k(common_mul, k)
    other_max = top_k(other_mul, k)
    common_courses = data[data['Index'].isin(common_max)]
    other_courses = data[data['Index'].isin(other_max)]
    print(common_courses)
    print(other_courses)