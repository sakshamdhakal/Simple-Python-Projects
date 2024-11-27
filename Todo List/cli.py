import functions


while True:
    # getting user input
    user_input = input("Type add, show, edit, complete, or exit:").strip() #removes any spaces in input


   
    if user_input.startswith("add") :
        #list slicing
        todo = user_input[4:] #only takes the input from and after index 4 in user_input 

        if todo:  
            with open('todos.txt', 'a') as file :
                file.writelines(todo + "\n") # adds a todo in a new line
        else :
                print("Input cannot be empty")
            
    elif user_input.startswith("show") :
        todos = functions.read_todos()

        if todos: 

            # new_todos = [item.strip('\n') for item in todos] list comprehension

            for index, item in enumerate(todos) :
                row = f"{index + 1}.{item.strip('\n')}" # strip removes unnecessary new line
                print(row.title()) # strip can also be used while printing
        else :
                print("No Todos found. Please add one.")

    elif user_input.startswith("edit") :
        todos = functions.read_todos()

        if todos : 
            number_str = user_input[5:].strip()
            # print(number)
            if number_str :
                try :
                    number = int(number_str)
                    if 0 < number <= len(todos) : 
                        number = number - 1
                        existing_todo = todos[number]
                        print(existing_todo.title())
                        new_todo = input("Enter a new todo:")
                        if new_todo :
                            todos[number] = new_todo + "\n"
                            functions.write_todos(todos[number])
                        else :
                            print("New todo cannot be empty!")
                    else :
                        print("Enter a correct number.")
                    
                except ValueError:
                    print("Please input a number")
                    continue
            else:
                print("Input cannot be empty")
        else :
            print("No todos to edit:")

    elif user_input.startswith("complete") :
        todos = functions.read_todos()
        if todos:
            number_str = user_input[9:].strip()
            if number_str:
                try :
                    number = int(number_str)

                    if 0 < number <= len(todos) : #checks if the number is in the list or 
                        index = number - 1
                        remove_todo = todos[index].strip('\n')
                        todos.pop(index)
                        
                        functions.write_todos(todos)
                        
                        message = f"Todo {remove_todo.title()} was removed"
                        print(message)
                    else :
                        print("Enter a correct number.")
                except ValueError :
                    print("Please Enter a Number!")
        else :
                print("No todos to complete!")

    elif 'exit' in user_input :
        break

    else :
        print("wrong input!")

print("Bye!")
