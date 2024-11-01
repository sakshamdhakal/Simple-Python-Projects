while True:
    # getting user input
    user_input = input("Type add, show, edit, complete, or exit:").strip() #removes any spaces in input

    match user_input:
        case 'add' :
            todo = input("Enter a todo:").strip() 

            if todo:  
                with open('todos.txt', 'a') as file :
                    file.write(todo + "\n") # adds a newline so every todo is in a new line
            else :
                    print("Input cannot be empty")
               
        case 'show':
            with open('todos.txt','r') as file :
                todos = file.readlines() # reads everything in file and copies it in todos

            if todos: 

                # new_todos = [item.strip('\n') for item in todos] list comprehension

                for index, item in enumerate(todos) :
                    row = f"{index + 1}.{item.strip('\n')}" # strip removes unnecessary new line
                    print(row.title()) # strip can also be used while printing
            else :
                    print("No Todos found. Please add one.")

        case 'edit':
            with open('todos.txt','r') as file :
                todos = file.readlines()

            if todos : 
                number = int(input("Number of the todo to edit:"))
                
                if 0 < number <= len(todos) : 
                    number = number - 1
                    existing_todo = todos[number]
                    print(existing_todo.title())
                    new_todo = input("Enter a new todo:")
                    if new_todo :
                        todos[number] = new_todo + "\n"
                        with open('todos.txt','w') as file : # opens a txt file 
                            file.writelines(todos)
                    else :
                        print("New todo cannot be empty!")
                else :
                    print("Enter a correct number.")
            else :
                print("No todos to edit:")

        case 'complete':
            with open('todos.txt','r') as file :
                todos = file.readlines()
                if todos:
                    number = int(input("Number of the todo to complete:"))

                    if 0 < number <= len(todos) : #checks if the number is in the list or 
                        index = number - 1
                        remove_todo = todos[index].strip('\n')
                        todos.pop(index)
                        
                        with open('todos.txt','w') as file :
                            file.writelines(todos)
                        
                        message = f"Todo {remove_todo.title()} was removed"
                        print(message)
                    else :
                        print("Enter a correct number.")
                else :
                    print("No todos to complete!")

        case 'exit':
            break
        case everything_else : 
            print("Wrong Input, Please Try Again!!")

print("Bye!")
