import xlrd, csv
 
def read_xls(loc, cols, rel_row=0):
    out = []
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 
      
 
    for i in range(sheet.nrows - rel_row):
        temp = []
        for j in cols:
            temp.append(sheet.cell_value(rel_row + i, j))
 
        out.append(temp)
    
    return out
 
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

def read_dat(loc, ranges, rel_row=0):
    data = read_txt(loc, [0], 0, delim="\t")
    out = []
    for i in data:
        out.append(list(map(lambda j: i[0][j[0]-1:j[1]].strip(), ranges)))

    return out

def convert_dict_list(dic):
    out = []
    for i in dic:
        out.append([i, dic[i]])
    return out

def convert_pct_str_to_float(s):
    if s and s != '-':
        return float(s) / 100
    else:
        return 0

class Data:
    allSectionTitles = ['privateSchoolEnrollment',
                        'publicSchoolMinority',
                        'currentCostApa',
                        'totalPopulation',
                        'landArea',
                        ]
    
    def __init__(self, year):
        self.year = year
        self.data = {}

    # data format: [[leaid, sectionTitle1, sectionTitle2] ... ]
    def add(self, sectionTitles, data):
        for i in data:
            leaid = i[0]
            if not isinstance(leaid, str):
                leaid = str(int(leaid))
            if len(leaid) == 7:
                leaid = leaid[2:]
            if len(leaid) != 5:
                print(sectionTitles, data)
                raise
            if leaid not in self.data:
                self.data[leaid] = {}
##                for j in allSectionTitles:
##                    self.data[leaid][j] = None

            for j in range(len(sectionTitles)):
                self.data[leaid][sectionTitles[j]] = i[j+1]
                    

            
    def performAction(self, func, rtn, param, defaultValue=0, mustHave=False):
        tbd = []
        for key in self.data:
            empty = False
            
            for i in param:
                if i not in self.data[key]:
                    if mustHave:
                        empty = True
                    else:
                        self.data[key][i] = defaultValue
                        
            if not empty:
                self.data[key][rtn] = func(*list(map(lambda x: self.data[key][x], param)))
            else:
                tbd.append(key)
        print(tbd)
        for i in tbd:
            del self.data[i]

    def find(self, sectionTitle, value):
        out = []
        for key in self.data:
            if sectionTitle in self.data[key] and self.data[key][sectionTitle] == value:
                out.append(key)
        return [len(out), out]

    def export(self, sectionTitle):
        out = []
        for key in self.data:
            if sectionTitle in self.data[key]:
                out.append(self.data[key][sectionTitle])
        return out


