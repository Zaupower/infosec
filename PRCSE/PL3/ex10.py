'''
Read the “. json” file resultant of exercise 1 and determine the following metrics. Store this
information as human-readable text in well formatted “.txt” file.
c. For each department:
i. The number of employees.
ii. Average salary.
iii. Early expenses based on base salary (14 months)
d. For the company:
i. Number of departments.
ii. Departments with lowest and highest early wages.
iii. Total amount of wage expenses.
'''

import json

# Step 1: Read the JSON file
json_file_path = './supportfiles/ex9.json'  # Replace with the actual path to your JSON file

with open(json_file_path, 'r') as json_file:
    employee_data = json.load(json_file)

# Step 2: Calculate the metrics
company_metrics = {
    'num_departments': len(employee_data),
    'min_max_early_wages': {'min_department': None, 'max_department': None},
    'total_wage_expenses': 0
}

department_metrics = {}

for department, employees in employee_data.items():
    num_employees = len(employees)
    
    # Calculate average salary
    total_salary = sum(float(employee['Salary']) for employee in employees)
    avg_salary = total_salary / num_employees
    
    # Calculate early expenses based on base salary for 14 months
    early_expenses = total_salary * 14
    
    # Update department metrics
    department_metrics[department] = {
        'num_employees': num_employees,
        'avg_salary': avg_salary,
        'early_expenses': early_expenses
    }
    
    # Update company metrics
    company_metrics['total_wage_expenses'] += early_expenses

    # Update min and max departments based on early expenses
    if company_metrics['min_max_early_wages']['min_department'] is None or \
            department_metrics[department]['early_expenses'] < \
            department_metrics[company_metrics['min_max_early_wages']['min_department']]['early_expenses']:
        company_metrics['min_max_early_wages']['min_department'] = department

    if company_metrics['min_max_early_wages']['max_department'] is None or \
            department_metrics[department]['early_expenses'] > \
            department_metrics[company_metrics['min_max_early_wages']['max_department']]['early_expenses']:
        company_metrics['min_max_early_wages']['max_department'] = department

# Step 3: Save the metrics to a text file
txt_file_path = './supportfiles/metrics.txt'  # Replace with the desired output text file path

with open(txt_file_path, 'w') as txt_file:
    # Write company-level metrics
    txt_file.write("Company Metrics:\n")
    txt_file.write(f"Number of Departments: {company_metrics['num_departments']}\n")
    txt_file.write(f"Departments with Lowest Early Wages: {company_metrics['min_max_early_wages']['min_department']}\n")
    txt_file.write(f"Departments with Highest Early Wages: {company_metrics['min_max_early_wages']['max_department']}\n")
    txt_file.write(f"Total Wage Expenses: {company_metrics['total_wage_expenses']}\n\n")

    # Write department-level metrics
    txt_file.write("Department Metrics:\n")
    for department, metrics in department_metrics.items():
        txt_file.write(f"Department: {department}\n")
        txt_file.write(f"Number of Employees: {metrics['num_employees']}\n")
        txt_file.write(f"Average Salary: {metrics['avg_salary']}\n")
        txt_file.write(f"Early Expenses: {metrics['early_expenses']}\n\n")

print(f'The metrics have been successfully calculated and saved to {txt_file_path}.')