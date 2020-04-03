import pandas as pd
import re
path1=str(input("Enter your csv file location"));
path2=str(input("Enter your json file location"));
res = pd.read_csv(path1,index_col=0) 
res2 = pd.read_json(path2)
def special_character_check(input_str):
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]-+=;,~')
    if(string_check.search(input_str) == None):
        return True 
    else: 
        return False
def lowercase_or_digit_check(input_str):
    flag = 0
    for ch in input_str:
        if ch.isdigit():
            return False
        if ch.isupper():
            flag = 1 
    if flag == 1:
        return True
    return False
def multiple_word_check(input_str):
    for ch in input_str:
        if ch==' ':
            return True
    return False   
print("The invalid names in CSV are : ")
for name in res.index:
    if(not(special_character_check(name) and lowercase_or_digit_check(name) and multiple_word_check(name))):
        print(name)
        res = res.drop(name,axis = 0)
res = res.reset_index()
print("******************************************")
print("The valid entries are:",end = "\n\n")
valid_names = []
i1 = []
i2 = []
index1 = 0
index2 = 0
for name in res['Person Name']:
    index2 = 0
    for nam in res2["n"]:
        if nam.split()==name.split():
            valid_names.append(name)
            i1.append(index1)
            i2.append(index2)
            break
        index2 = index2 + 1 
    index1 = index1 + 1   
for i in range(0,len(i1)):
    print("Name :",end = " ")
    print(res.loc[i1[i],"Person Name"])
    print("Project :",end = " ")
    print(res.loc[i1[i],"Project"])
    print("Organization :",end = " ")
    print(res.loc[i1[i],"Organization"])
    print("Department :",end = " ")
    print(res2.loc[i2[i],"d"])
    print("Roll No. :",end = " ")
    print(res2.loc[i2[i],"i"])
    print('**************')                        
