import re
import csv

lines = None
lnums = []
courses = []

def clean(desc):
    desc = desc.replace('\n', ' ')
    desc = desc.replace('\x0c', ' ')
    end = desc.find('Typically offered')
    desc = desc[19:end]
    desc = desc.strip()
    return desc

with open('PurdueCatalog.txt') as infile:
    lines = infile.readlines()

for i, line in enumerate(lines):
    match = re.search(r'\d{5} -', line)
    if match:
        lnums.append(i)
        end = match.span()[1]
        course = line[0:end - 2]
        title = line[end:]
        title = title.strip()
        courses.append([course, title])

descs = []
for i in range(len(lnums) - 1):
    desc = ""
    j = lnums[i] + 1
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

print(courses[0])

with open('catalog.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(courses)