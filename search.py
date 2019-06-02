import re

#data = ["P_C_01_a", "PAV-PRD1-MAT1-2-PAT1-COL2-3-BST1", "P_K_01_a", "PAV-PRD1-MAT9-65-PAT22-65-COL5-6-7-22-BST1"]
dataFull = ["P_C_01_a", "P_C_01_b", "P_C_02_a", "P_C_02_b", "P_C_03_a", "P_C_03_b", "P_C_04_a", "P_C_04_b", "P_C_05_a", "P_C_05_b", "P_C_06_a", "P_C_06_b", "P_C_09_a", "P_C_09_b", "P_C_10_a", "P_C_10_b", "P_C_11_a", "P_C_11_b", "P_C_12_a", "P_C_12_b", "P_C_13_a", "P_C_13_b", "P_C_14_a", "P_C_14_b", "P_C_15_a", "P_C_15_b", "P_C_16_a", "P_C_16_b", "P_C_20_a", "P_C_20_b", "P_C_21_a", "P_C_21_b", "P_C_22_a", "P_C_22_b", "P_C_23_a", "P_C_23_b", "P_C_24_a", "P_C_24_b", "P_C_25_a", "P_C_25_b", "P_C_26_a", "P_C_26_b", "P_C_27_a", "P_C_27_b", "P_C_28_a", "P_C_28_b", "P_C_29_a", "P_C_29_b", "P_C_30_a", "P_C_30_b", "P_C_31_a", "P_C_31_b", "P_C_32_a", "P_C_32_b", "P_D_01", "P_G_01_a", "P_G_01_b", "P_G_02_a", "P_G_02_b", "P_K_01_a", "P_K_01_b", "P_K_02_a", "P_K_02_b", "P_K_03_a", "P_K_03_b", "P_K_04_a", "P_K_04_b", "P_K_05_a", "P_K_05_b", "P_K_06_a", "P_K_06_b", "P_M_01_a", "P_M_01_b", "P_M_03_a", "P_M_04_a", "P_M_04_b", "P_M_05_a", "P_R_01_a", "P_R_01_b", "P_R_02_a", "P_R_02_b", "P_R_03_a", "P_R_03_b", "P_R_04_a", "P_R_04_b", "P_R_05_a", "P_R_05_b", "P_R_06_a", "P_R_06_b", "P_R_07_a", "P_R_07_b", "P_S_01_a", "P_S_01_b", "P_S_02_a", "P_S_02_b", "P_S_03_a", "P_S_03_b", "P_S_04_a", "P_S_04_b", "P_W_01_a", "P_W_01_b", "P_W_02_a", "P_W_02_b", "P_W_03_a", "P_W_03_b", "P_W_04_a", "P_W_04_b", "PAV-PRD1-MAT1-2-PAT1-COL2-BST1", "PAV-PRD1-MAT1-2-PAT1-COL2-BST2", "PAV-PRD1-MAT1-5-PAT1-COL2-BST1", "PAV-PRD1-MAT1-5-PAT1-COL2-BST2", "PAV-PRD1-MAT1-4-PAT1-COL1-BST1", "PAV-PRD1-MAT1-4-PAT1-COL1-BST2", "PAV-PRD1-MAT1-5-PAT1-COL2-BST1", "PAV-PRD1-MAT1-5-PAT1-COL2-BST2", "PAV-PRD1-MAT1-PAT2-COL2-BST1", "PAV-PRD1-MAT1-PAT2-COL2-BST2", "PAV-PRD1-MAT1-PAT2-COL1-2-BST1", "PAV-PRD1-MAT1-PAT2-COL1-2-BST2", "PAV-PRD1-MAT1-PAT2-COL1-BST1", "PAV-PRD1-MAT1-PAT2-COL1-BST2", "PAV-PRD1-MAT1-2-5-PAT3-COL2-BST1", "PAV-PRD1-MAT1-2-5-PAT3-COL2-BST2", "PAV-PRD1-MAT1-2-5-PAT3-COL1-BST1", "PAV-PRD1-MAT1-2-5-PAT3-COL1-BST2", "PAV-PRD1-MAT1-2-PAT4-COL2-BST1", "PAV-PRD1-MAT1-2-PAT4-COL2-BST2", "PAV-PRD1-MAT1-2-PAT4-COL1-BST1", "PAV-PRD1-MAT1-2-PAT4-COL1-BST2", "PAV-PRD1-MAT1-2-PAT5-COL2-BST1", "PAV-PRD1-MAT1-2-PAT5-COL2-BST2", "PAV-PRD1-MAT1-2-PAT5-COL2-BST1", "PAV-PRD1-MAT1-2-PAT5-COL2-BST2", "PAV-PRD1-MAT1-5-8-PAT6-COL2-BST1", "PAV-PRD1-MAT1-5-8-PAT6-COL2-BST2", "PAV-PRD1-MAT1-5-8-PAT6-COL1-BST1", "PAV-PRD1-MAT1-5-8-PAT6-COL1-BST2", "PAV-PRD1-MAT1-PAT7-COL2-BST1", "PAV-PRD1-MAT1-PAT7-COL2-BST2", "PAV-PRD1-MAT1-PAT8-COL2-BST1", "PAV-PRD1-MAT1-PAT8-COL2-BST2", "PAV-PRD1-MAT1-5-PAT9-COL2-BST1", "PAV-PRD1-MAT1-5-PAT9-COL2-BST2", "PAV-PRD1-MAT1-PAT10-COL2-BST1", "PAV-PRD1-MAT1-PAT10-COL2-BST2", "PAV-PRD1-MAT1-5-PAT11-COL2-BST1", "PAV-PRD1-MAT1-5-PAT11-COL2-BST2", "PAV-PRD1-MAT1-8-PAT12-COL2-BST1", "PAV-PRD1-MAT1-8-PAT12-COL2-BST2", "PAV-PRD1-MAT1-5-PAT13-COL1-2-BST1", "PAV-PRD1-MAT1-5-PAT13-COL1-2-BST2", "PAV-PRD1-MAT1-PAT14-COL2-BST1", "PAV-PRD1-MAT1-PAT14-COL2-BST2", "PAV-PRD1-MAT1-5-PAT15-COL2-BST1", "PAV-PRD1-MAT1-5-PAT15-COL2-BST2", "PAV-PRD1-MAT1-5-PAT16-COL1-2-BST1", "PAV-PRD1-MAT1-5-PAT16-COL1-2-BST2", "PAV-PRD1-MAT1-PAT17-COL1-2-BST1", "PAV-PRD1-MAT1-PAT17-COL1-2-BST2", "PAV-PRD1-MAT1-PAT18-COL1-2-BST1", "PAV-PRD1-MAT1-PAT18-COL1-2-BST2", "PAV-PRD1-MAT6-PAT19-BST2", "PAV-PRD1-MAT1-8-PAT20-BST1", "PAV-PRD1-MAT1-8-PAT20-BST2", "PAV-PRD1-MAT1-5-PAT21-BST1", "PAV-PRD1-MAT1-5-PAT21-BST2", "PAV-PRD1-MAT9-PAT22-COL5-BST1", "PAV-PRD1-MAT9-PAT22-COL5-BST2", "PAV-PRD1-MAT9-PAT22-COL6-BST1", "PAV-PRD1-MAT9-PAT22-COL6-BST2", "PAV-PRD1-MAT9-PAT22-COL7-BST1", "PAV-PRD1-MAT9-PAT22-COL7-BST2", "PAV-PRD1-MAT9-PAT23-COL5-BST1", "PAV-PRD1-MAT9-PAT23-COL5-BST2", "PAV-PRD1-MAT9-PAT23-COL6-BST1", "PAV-PRD1-MAT9-PAT23-COL6-BST2", "PAV-PRD1-MAT9-PAT23-COL7-BST1", "PAV-PRD1-MAT9-PAT23-COL7-BST2", "PAV-PRD2-MAT10-COL5-BST1", "PAV-PRD2-MAT10-COL5-BST2", "PAV-PRD2-MAT1-COL6-BST1", "PAV-PRD2-MAT2-COL6-BST1", "PAV-PRD2-MAT2-COL6-BST2", "PAV-PRD2-MAT1-COL8-BST1", "PAV-PRD3-MAT11-COL3-BST1", "PAV-PRD3-MAT11-COL3-BST2", "PAV-PRD3-MAT12-COL1-BST1", "PAV-PRD3-MAT12-COL1-BST2", "PAV-PRD3-MAT12-COL10-BST1", "PAV-PRD3-MAT12-COL10-BST2", "PAV-PRD3-MAT12-COL9-BST1", "PAV-PRD3-MAT12-COL9-BST2", "PAV-PRD3-MAT14-BST1", "PAV-PRD3-MAT14-BST2", "PAV-PRD3-MAT5-COL10-BST1", "PAV-PRD3-MAT5-COL10-BST2", "PAV-PRD3-MAT5-COL2-BST1", "PAV-PRD3-MAT5-COL2-BST2", "PAV-PRD1-MAT3-5-COL2-3-BST1", "PAV-PRD1-MAT3-5-COL2-3-BST2", "PAV-PRD1-MAT3-12-COL2-1-BST1", "PAV-PRD1-MAT3-12-COL2-1-BST2", "PAV-PRD1-MAT3-5-COL5-3-BST1", "PAV-PRD1-MAT3-5-COL5-3-BST2", "PAV-PRD1-MAT3-12-COL5-1-BST1", "PAV-PRD1-MAT3-12-COL5-1-BST2", "PAV-PRD1-MAT7-5-COL10-3-BST1", "PAV-PRD1-MAT7-5-COL10-3-BST2", "PAV-PRD1-MAT7-12-COL10-1-BST1", "PAV-PRD1-MAT7-12-COL10-1-BST2", "PAV-PRD1-MAT7-5-COL9-3-BST1", "PAV-PRD1-MAT7-5-COL9-3-BST2", "PAV-PRD1-MAT7-12-COL9-1-BST1", "PAV-PRD1-MAT7-12-COL9-1-BST2"]
print(len(dataFull))

#dataDivided=data[3].split('-')

def divideTags (x):
    list = []
    for i in x:
        a = i.split('-')
        list.append(a)
    return(list)


def flattenList (x):
    flatList = []
    for sublist in x:
        for i in sublist:
            flatList.append(i)
    return flatList


def findAlone(x):
    if len(x) <= 2:  # тут надо переписать
        return(x)

def clearDigits(x):
    noDigits=[]
    for i in x:
        if not i.isdigit():
            noDigits.append(i)
    return(''.join(noDigits))

def addPrevTag (x):
    for i in x:
        if findAlone(i):
            tag = clearDigits(x[x.index(findAlone(i)) - 1])
            y = tag + findAlone(i)
            return (y)

def replaceAlone (x):
    for n, i in enumerate(x):
        if findAlone(i):
            x[n] = addPrevTag(x)
    return x


dataDivided = flattenList(divideTags(dataFull))

print(replaceAlone(dataDivided))
print(set(replaceAlone(dataDivided)))
print(len(set(replaceAlone(dataDivided))))
print(len(replaceAlone(dataDivided)))

listSorted = sorted(list(set(replaceAlone(dataDivided))))
print(listSorted)
print(len(listSorted))
# for x in data:
#     print(x.partition('_'))
#
# def search(items, query):
#     return items
#
#
# def get_tags(items):
#
#     return []


# if __name__ == '__main__':
#     print(search([], [])
#     print(get_tags([])