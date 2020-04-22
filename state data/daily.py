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

#2 is the short form 
table = read_txt("./NY.csv", [1, 2, 6], 1, ",", -1)
#load conversion2 from icao to country short form
data = {}
output = ''

for i in table:
    print(i[0])
    if i[1] not in data:
        data[i[1]] = float(i[2])
    else:
        data[i[1]] += float(i[2])

for i in data:
    temp = []
    temp.append(str(i))
    temp.append(str(data[i]))
    output += ','.join(temp) +'\n'

print(output)



with open('./NY 2.csv', 'w', encoding='utf-8') as file1:
    file1.write(output)





print("complete")



