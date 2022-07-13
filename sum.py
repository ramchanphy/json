import json
d='{"10":20,"30":40,"50":60}'
y=json.loads(d)
print(y['10']+y["30"])