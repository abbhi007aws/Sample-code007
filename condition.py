# get input form user
salary = input("Please enter your salary  : ")
# Check if the input is a digit
if salary.isdigit():
   salary = int(salary)
# condition based on logic

if salary < 25000:
   print(f"You are L1 and your current salary is : {salary}")
elif salary < 50000 and  salary > 25000:
   print(f"you are in L2 your current salary is : {salary}")


         
   

