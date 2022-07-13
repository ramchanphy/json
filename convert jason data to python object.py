import json
sj={"4":5,"3":2,"1":3,"2":4}
y=json.dumps(sj,sort_keys=True)
print(y)