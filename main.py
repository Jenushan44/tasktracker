import sys # Provides information about python interpreter 
import json 
import datetime 
from pathlib import Path 

tasks_path = Path("tasks.json")

args = sys.argv

if len(args) < 2: 
  print('Please provide a valid command')
  sys.exit() # Immediatley ends the script
    
if args[1] != 'add': 
  print("Please provide a valid command")
  sys.exit()
else:
  if len(args) < 3:
    print("Please provide a description")
    sys.exit()
  else:  
    print(f"Adding task: {args[2]}")


if tasks_path.exists(): 
  
  with open("tasks.json", "r") as file: 
    data = json.load(file)

else: 
  data = { "nextId": 1, "tasks": [] }
  with open("tasks.json", "w") as file: 
    json.dump(data,file)
  
    