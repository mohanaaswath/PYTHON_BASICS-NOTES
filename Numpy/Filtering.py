import numpy as np
age = np.array([[21,17,14,16,17,22,24,36],
                [65,72,13,15,21,40,45,10]])
teenage = age[age<18]
print(teenage)  #[17 14 16 17 13 15 10]

adults = age[(age >= 18) & (age < 65)]
seniors = age[age >= 65]
events = age[age %2 == 0]
odds = age[age %2 != 0 ]

print(adults)
print(seniors)
print(events)
print(odds)

adult = np.where(age >= 18 , age , 0)  
print(adult)