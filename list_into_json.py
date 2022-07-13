import json
a=["sam","programer","24","35000"]
b=["john","doctor","25","50000"]
c=["luke","police","30","35000"]
d=["jere","manager","40","45000"]
e=["name","job","age","salary"]
dict={}
dict1={}
dict2={}
dict3={}
dict4={}

i=1
while i<len(a):
    dict1[e[i]]=a[i]
    dict2[e[i]]=b[i]
    dict3[e[i]]=c[i]
    dict4[e[i]]=d[i]
    i+=1
dict["emp1"]=dict1
dict["emp2"]=dict2
dict["emp3"]=dict3
dict["emp4"]=dict4
print(dict)
with open("file3.txt","a") as f:
    j=json.dump(dict,f,indent=4)
