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
table = read_txt("./countrycodetest1.csv", [0, 2], 1, ",", -1)
#load conversion2 from icao to country short form
conversion2 = {}
for i in table:
    conversion2[i[0]] = i[1]


data = read_txt("./Mar.csv", [5, 6, 9], 0, ",", -1)
with open("conversion.json") as f:
    conversion = json.load(f)


def convertStates(data):
    temp = []
    for i in data:
        if i[0] != '' and i[1] != '':
            time = i[2].split(" ");
            i[2] = time[0]
            if i[1] in conversion:
                i[1] = conversion[i[1]]
                temp.append(i)
    return temp
temp = convertStates(data)

def convertTCountry(temp):
    temp2 = []
    for i in temp:
        if i[0][:2] in conversion2:
            i[0] = conversion2[i[0][:2]]
            temp2.append(i)
        elif i[0][0] in conversion2:
            i[0] = conversion2[i[0][0]]
            temp2.append(i)
    
    return temp2

def convertString(string):
    out = ''
    for i in string:
        out += ','.join(i) + "\n"
    return out



temp2 = convertTCountry(temp)
temp2String = convertString(temp2)
with open('./shortformMar.csv', 'w', encoding='utf-8') as file1:
    file1.write(temp2String)


deaths = read_txt("./total-deaths-and-cases-covid-19.csv", [1, 2, 3, 4], 1, ",", -1)
def processInfo(deaths):
    info = []
    for i in deaths:
        if i[0] != "":
            a = strptime(i[1], "%b %d, %Y")
            i[1] = strftime("%Y-%m-%d",a)
            info.append(i)
    return info

info = processInfo(deaths)

#prepare dictionary country: {date: [confirmed, deaths]}
#0 - code 1 - date 
def prepDict(info):
    dict = {}
    for i in info:
        if i[0] not in dict:
            entry = {}
            data = [i[2], i[3]]
            entry[i[1]] = data
            dict[i[0]] = entry
        else:
            data = [i[2], i[3]]
            dict[i[0]][i[1]] = data
    return dict


infoDict = prepDict(info)



#temp2 - origin, des, time;   info - code, time, cases, deaths
def connect(infoDict, temp2):
    output = ''
    for i in temp2: 
        if i[0] in infoDict:
            current = infoDict[i[0]]
            if i[2] in current:
                i.append(current[i[2]][0])
                i.append(current[i[2]][1])
                output += ','.join(i) + "\n"
                print(i)
    return output


output = connect(infoDict, temp2)
with open('./outputMar.csv', 'w', encoding='utf-8') as file:
    file.write(output)


print("complete")



