import re
import csv
import string

lines = None
lnums = []
courses = []

def clean(desc):
    desc = desc.replace('\n', ' ')
    desc = desc.replace('\x0c', '')
    end = desc.find('Typically offered')
    desc = desc[19:end]
    desc = desc.strip()
    return desc

with open('PurdueCatalog.txt') as infile:
    lines = infile.readlines()

j = 0
for i, line in enumerate(lines):
    line = line.replace('\x0c', '')
    match = re.search(r'\d{5} -', line)
    if match:
        lnums.append(i)
        start = match.span()[0]
        end = match.span()[1]
        clg = line[0:start - 1]
        num = line[start: end - 2]
        course = line[0: end - 2]
        title = line[end:]
        title = title.strip()
        courses.append([j, course, clg, num, title])
        j += 1

descs = []
for i in range(len(lnums) - 1):
    desc = ""
    j = lnums[i] + 1
    if lines[j] == '\n':
        j += 1
    while lines[j] != '\n':
        desc += lines[j]
        j += 1
    desc = clean(desc)
    descs.append(desc)

desc = ''
for i in range(lnums[-1] + 1, len(lines)):
    desc += lines[i]
desc = clean(desc)
descs.append(desc)

for i in range(len(courses)):
    courses[i].append(descs[i])

with open('catalog.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['Index', 'Course', 'School', 'Number', 'Title', 'Description'])
    writer.writerows(courses)