import csv, json
from time import strptime
from time import strftime

def read_txt(loc, cols, rel_row=0, delim="\t", performLookup=-1):
    f = open(loc, encoding='utf-8', errors='replace')
    data = list(csv.reader(f, delimiter=delim))

    out = []

    if performLookup > -1:
        cols = list(map(lambda x: data[performLookup].index(x), cols))

    for i in range(len(data) - rel_row):
        temp = []
        for j in cols:
            temp.append(data[rel_row + i][j])

        out.append(temp)

    f.close()

    return out

#i[0] -- long name i[1] -- short form 
table = read_txt("./countryshortform.csv", [0, 2], 1, ",", -1)

#i[0] -- long name i[1] -- population
pop = read_txt("./populationcountry.csv", [1, 2], 1, ",", -1)

dict = {}
for i in table:
    if i[0] not in dict:
        dict[i[0]] = i[1]


def convertString(string):
    out = ''
    for i in string:
        out += ','.join(i) + "\n"
    return out

for i in pop:
    if i[0] in dict:
        i.append(dict[i[0]])

output = convertString(pop)

with open('./population.csv', 'w', encoding='utf-8') as file1:
    file1.write(output)




print("complete")



