shopping_list = []

# -----------------------------> Def show_help function
def show_help():
    print("what should we pick up at the sotre ?")
    print(""" 
Enter 'DONE' to stop adding items.
Enter 'SHOW' to see your current list.
Enter 'HELP' for this help.
""")

# -----------------------------> def show_list function    
def show_list():
    # print out the list
    print("Here's you list: ")
    for item in shopping_list:
        print(item) 

# ----------------------------> show help at the begining the program    
show_help()

while True:
    new_item = input("> ")
    if new_item == "DONE" : 
      break
    elif new_item == "HELP" :
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    shopping_list.append(new_item)