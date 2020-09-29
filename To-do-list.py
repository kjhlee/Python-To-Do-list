

y = ""
count = 0
x = ""
toDo = []
while(x != "stop"):
    x = input("Add a task to your to do list type 'stop' to stop adding tasks: ")
    if(x == "stop"):
        break
    else:
        toDo.append(x)
        count += 1
        
print("Here are your tasks: ")
for i in range(0, len(toDo)):
    print(str(i+1)+ ". "+ toDo[i])

while(len(toDo) > 0):
    y = input("Have you finished this task '"+ toDo[0] + "':")
    if(y == "yes"):
        toDo.pop(0)
        if(len(toDo) > 0):
            for i in range(0, len(toDo)):
                print(str(i+1)+ ". "+ toDo[i])
    elif(y == "no"):
        which = int(input("Which task have you done 'Pick a number': "))
        if(which > count):
            print("error")
        else:
            toDo.pop(which-1)
            if(len(toDo) > 0):
                for i in range(0, len(toDo)):
                    print(str(i+1)+ ". "+ toDo[i])
                
    else:
        print("You're done with all your tasks")
        
        
        


