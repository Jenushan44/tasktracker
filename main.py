import sys # Provides information about python interpreter 

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
    