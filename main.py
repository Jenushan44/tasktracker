import sys # Provides information about python interpreter 
import json 
import datetime 
from pathlib import Path 

tasks_path = Path("tasks.json")

args = sys.argv

if len(args) < 2: 
  print('Please provide a valid command')
  sys.exit() # Immediatley ends the script
    
if tasks_path.exists(): 
  with open("tasks.json", "r") as file: 
    data = json.load(file)
else: 
  data = { "nextId": 1, "tasks": [] }
  with open("tasks.json", "w") as file: 
    json.dump(data,file)
  
if args[1] == 'add': 
  description = args[2]
  task_id = data["nextId"]

  currentTask = {
    "id": task_id, 
    "description": description, 
    "status": "todo",
  }

  data["tasks"].append(currentTask)
  data["nextId"] += 1 

  with open("tasks.json", "w") as file: 
    json.dump(data, file)

  print(f"Tasks successfully added {task_id}")

elif args[1] == 'list': 
  with open("tasks.json", "r") as file: 
    d = json.load(file)

  for task in data['tasks']: 
    print(task["id"], end= " ")
    print(task["description"], end=" ")
    print(task["status"])

else: 
  print("Please provide a valid command")
  sys.exit()