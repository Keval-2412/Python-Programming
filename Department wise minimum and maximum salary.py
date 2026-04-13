data = {
    101 : [(1, 20000), (2, 25000), (3, 18000)],
    102 : [(4, 30000), (5, 28000)],
    103 : [(6, 15000), (7, 17000)]
}

for dept, employees in data.items():
   salaries = [emp[1] for emp in employees]
   print(f"Dept {dept} -> Min Salary: {min(salaries)} , Max Salary: {max(salaries)}")
   