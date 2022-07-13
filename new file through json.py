import json
sj={"name":"phyphy","class":"12","village":"ningchou"}
with open("team.txt","w") as f:
    f=json.dump(sj,f,indent=4)