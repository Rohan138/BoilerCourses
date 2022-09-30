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
    course = input("Enter course code e.g. (AAE 20300) or q to quit: ")
    if course == 'q':
        print('Quitting')
        sys.exit(0)
    index = data[data['Course'] == course]['Index']
    print(data[data['Course'] == course])
    if index.empty:
        print('Course not found')
        continue
    k = int(input('Enter number of similar courses to find: '))
    school, number = course.split()

    common = data[(data['School'] == school) & (data['Course'] != course)]
    common_index = common['Index']
    common_mul = np.take(mul[index], common_index, axis=1)
    common_max = top_k(common_mul, k)
    common_vals = np.take(common_index, common_max, axis=1)
    common_courses = data[data['Index'].isin(common_vals)]

    other = data[data['School'] != school]
    other_index = other['Index']
    other_mul = np.take(mul[index], other_index, axis=1)
    other_max = top_k(other_mul, k)
    other_vals = np.take(other_index, other_max, axis=1)
    other_courses = data[data['Index'].isin(other_vals)]

    print(f'Similar courses in {school}:')
    print(common_courses)
    print(f'Similar courses not in {school}:')
    print(other_courses)
    print('')