import json
sj='{"name":"toyota rav4","engine":"2.5L","price":32000}'
a=json.loads(sj)
b="vehicalObj."
for i in a:
    if i!="name":
        c=b+i
        print(c,end=",")