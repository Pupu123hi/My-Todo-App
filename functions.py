def get_todos(filepath="todos.txt"):
    """ this is the code what we want to write about."""

    with open(filepath,'r') as file_local:
        todos_local=file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath="todos.txt"):
    """ write the to-do item list in text file. """
    with open(filepath,'w') as file:
        file.writelines(todos_arg)
if __name__=="__main__":
    print("Hello")
    print(get_todos())
