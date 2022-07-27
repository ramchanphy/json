import json
sj={"keys1":"value1","keys2":"value2"}
sj["key3"]="value3"
print(json.dumps(sj,indent=2,separators=(",","=")))
