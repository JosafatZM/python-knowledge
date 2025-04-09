employee_salaries = {
    "Meli": 1000000,
    "Monse": 500000,
    "Sanz": 999999,
    "Jair": 250000
}

extra_employee_salaries = {
    "Meli": 567000,
    "Andrea": 45643
}

# employee_salaries.update(extra_employee_salaries)
# print(employee_salaries)

extra_employee_salaries.update(employee_salaries)
print(extra_employee_salaries)