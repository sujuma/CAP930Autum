name= input("Enter your name ")
salary=input("Enter the salary ")
designation=input("Enter the designation ")
city=input("Enter the city ")
empnames = ['John','Zayn']
empnames.append(name)
empsalary = ['23000','34000']
empsalary.append(salary)
emp1 = {'Name = ': empnames[2], 'Salary = ': empsalary[2], 'Designation = ': designation, 'City = ': city}
for a, b in emp1.items():
    print(a, b)
for x in empnames:
    print(x)
for y in empsalary:
    print(y)

