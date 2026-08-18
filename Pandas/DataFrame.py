import pandas as pd

Department = {
    "Name" : ["mohan" , "ram" , "sam" , "vishwa"] ,
    "Age" : [20 , 21 , 22 , 20]
}
df = pd.DataFrame(Department )
print(df)

df = pd.DataFrame(Department , index=["Employee 1" , "Employee 2" , "Employee 3" , "Employee 4" ])
#print(df)

#add new column

df["Job"] = ["AL & ML " , "front-end" , "ui&ux" , "business"]
print(df)

#add new row

new_row = pd.DataFrame([{"Name":"nithin" , "Age":19 , "Job":"Police"}] , index=["Employee 5"])
df = pd.concat([df , new_row])
print(df)