def read_todos(filepath="todos.txt") :
    """ Read a text file and returns the list of todo items."""
    with open(filepath,'r') as file_local :
        todos_local = file_local.readlines() # reads everything in file and copies it in todos
    return todos_local


def write_todos(todos_arg, filepath="todos.txt") :
    """ Writes the todo items list in the text file."""
    with open(filepath,'w') as file : # opens a txt file 
       file.writelines(todos_arg)
