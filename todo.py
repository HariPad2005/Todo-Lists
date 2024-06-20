todos=[]
try:
    with open('to_do.txt','r+') as f:
        lines = f.readlines()
        for x in lines:
            l=x.split('-')
            todos.append(l[1].strip())
        f.close()
except IOError:
        print("File doesnot exist. Creating a new file.")
        f=open('to_do.txt','w+')                                #The File is created if it doesnot exist.
        f.close()
print("The list of previous todo-s: ",todos)                    #previous works that are already stored.
while True:
    prompt = input("Enter options(add/show/edit/save/file/exit): ")
    prompt = prompt.strip().lower()
    match prompt:
        case 'add':
            todos.append(input("Enter the To-do work: "))
        case 'show':
            for index, item in enumerate(todos):
                line = f"{index+1}-{item}"
                print(line)
        case 'edit':
            if(len(todos)==0):                                  #if the list is empty, it prints there are no works existing.
                print("No works exist to be edited!")
                continue
            print(todos)
            index_value = int(input("Enter the number of todo to edit: "))
            index_value -= 1
            new_todo = input("Enter the new todo: ")
            todos[index_value] = new_todo
        case 'save':                                            #for saving into file
            with open('to_do.txt','w+') as f:
                for index, item in enumerate(todos):
                    flag = True
                    line = f"{index+1}-{item}"
                    f.write(line+'\n')                          #written to file
            f.close() 
            print("Written to to_do.txt")           
        case 'file':
            print("Contents in File: \n")
            with open("to_do.txt",'r') as txt:
                for line in txt:
                    print(line, end='')                         #printing the contents of the file
            txt.close()
        case 'exit':
            break
        case default:
            print("Enter Valid Option")                         #if an invalid option is given, It notifies.




        
