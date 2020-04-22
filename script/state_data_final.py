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

table1 = read_txt("./outputJan 2.csv", [0, 1, 2, 3, 4, 5], 0, ",", -1)
table2 = read_txt("./outputFeb 2.csv", [0, 1, 2, 3, 4, 5], 0, ",", -1)
table3 = read_txt("./outputMar 2.csv", [0, 1, 2, 3, 4, 5], 0, ",", -1)

#load conversion2 from icao to country short form
output = ''

for table in table1, table2, table3:
    for i in table:
        if i[1] == 'NY':
            temp = int(i[4])/float(i[5]);
            i.append(str(temp))
            output += ",".join(i) +"\n"

print(output)

with open('./NY.csv', 'w', encoding='utf-8') as file1:
    file1.write(output)



print("complete")



