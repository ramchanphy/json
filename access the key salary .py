import json
sj="""{"company":{"employ":{"name":"emma","payble":{"salary":7000,"bonus":800}}}}"""
a=json.loads(sj)
print(a["company"]["employ"]["payble"]["salary"])