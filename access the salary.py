import json
x= """{ "company":{"employee":{"name":"emma","payble":{"salary":7000,"bonus":800}}}}"""
a=json.loads(x)
print(a["company"]["employee"]["payble"]["salary"])