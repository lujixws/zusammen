# make a list to hold onto our items
shopping_list = []

# print out instructioins on how to use the app
print("what should we pick up at the sotre ?")
print("Enter 'DONE' to stop adding items.")

while True:
    new_item = input("> ")
    if new_item == "DONE" : 
      break
# add new iteams to our app
    shopping_list.append(new_item)
# print out the list
print("Here's you list: ")
for item in shopping_list:
    print(item) 
