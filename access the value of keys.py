import json
sj="""{"key1":"value","key2":"value2"}"""
y=json.loads(sj)
print(y["key2"])