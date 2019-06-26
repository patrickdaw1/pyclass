import random

name=input("Enter yo name ")
salary=input("SALARY")
raise_per=random.randint(0,100)
raise_amount=(int(salary)/raise_per)+int(salary)
print(f"{salary} {raise_amount}")