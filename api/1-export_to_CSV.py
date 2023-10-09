import csv
import requests
import sys

EMPLOYEE_URL = "https://jsonplaceholder.typicode.com/users/"
TODO_URL = "https://jsonplaceholder.typicode.com/users/{}/todos"

employee_id = sys.argv[1]

employee_response = requests.get(EMPLOYEE_URL + employee_id)
employee_data = employee_response.json()
employee_name = employee_data["username"]

todo_response = requests.get(TODO_URL.format(employee_id))
todo_data = todo_response.json()

csv_filename = f"{employee_id}.csv"

with open(csv_filename, mode='w', newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    for task in todo_data:
        employee_writer.writerow([employee_id, employee_name, str(task["completed"]), task["title"]])