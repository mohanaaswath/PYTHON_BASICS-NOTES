import pandas as pd

print(pd.__version__) 


data = [100,200,300,400,600]
series = pd.Series(data)
print(series)
 

data = ["a" , "b" , "c"]
series = pd.Series(data)
print(series)


data = [True , False ]
series = pd.Series(data)
print(series)


data = [100 , 200 , 300 , 400 , 500]
series = pd.Series(data , index=["A" , "B" , "C" , "D" , "E"]) 
series.loc["C"] = 800
print(series)
print(series.loc["A"])
print(series.iloc[1])


data = [100 , 200 , 250 , 300 , 110 , 115 , 400 , 500 , 600]
series = pd.Series(data , index=["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I"])
print(series[series >= 200]) 
print(series[series < 200])


Department = {
    "mohan" : "AI&ML",
    "abi"   : "AI&ML",
    "nithin" : "python",
    "vishwa" : "java"
}
series = pd.Series(Department)
print(series)
series.loc["vishwa"] = "react"
print(series)