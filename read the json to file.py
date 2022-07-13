import json
shopping_list={
    "shopping_list":{ 
        "chaco":"15",
        "Biscuits":"50",
        "Diary_milk":"30",
        "ice_cream":"20",
         } 
}
with open('app.txt','w')as f:
    json.dump(shopping_list,f,indent=4)