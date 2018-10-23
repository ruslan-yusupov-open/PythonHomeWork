import re


def read_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        print('File not found')


a = read_file("nasa_19950801.tsv")
lines = a.split("\n")

regExp = r'^([^\t]+)\t([^\t]+)\t(\d+)\t([A-Z]+)\t([^\t]+)\t(\d{3})\t(\d+)\t'

dict1 = {}
dict2 = {}

for the_line in lines:
    parsed = re.findall(regExp, the_line)

    if len(parsed) > 0:
        if parsed[0][5] in dict1:
            dict1[parsed[0][5]] += 1
        else:
            dict1[parsed[0][5]] = 1

print(dict1)
