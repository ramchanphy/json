import json
sj={"id":1,"name":"values","age":16}
f=open("file.json", "w")
a=json.dump(sj,f,indent=2,sort_keys=True)
f.close()