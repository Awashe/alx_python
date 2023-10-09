import requests
import sys

EMPLOYEE_URL = "https://jsonplaceholder.typicode.com/users/"
TODO_URL = "https://jsonplaceholder.typicode.com/users/{}/todos"

employee_id = sys.argv[1]

employee_response = requests.get(EMPLOYEE_URL + employee_id)
employee_data = employee_response.json()
employee_name = employee_data["name"]

todo_response = requests.get(TODO_URL.format(employee_id))
todo_data = todo_response.json()
total_tasks = len(todo_data)
done_tasks = [task for task in todo_data if task["completed"]]
num_done_tasks = len(done_tasks)

print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")
for task in done_tasks:
    print(f"\t {task['title']}")