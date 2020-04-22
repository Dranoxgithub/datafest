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

#1 population 2 country short form
table = read_txt("./population.csv", [1, 2], 0, ",", -1)
#load conversion2 from icao to country short form
dict = {}
for i in table:
    dict[i[1]] = i[0]


data = read_txt("./outputMar.csv", [0, 1, 2, 3, 4], 0, ",", -1)
out = ''
for i in data: 
    if i[0] in dict: 
        i.append(dict[i[0]])
        out += ','.join(i) + "\n"
    else:
        print(i[0])





with open('./outputMar 2.csv', 'w', encoding='utf-8') as file1:
    file1.write(out)


print("complete")



