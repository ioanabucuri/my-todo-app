FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Read a txt file and return a list of
    to-do items
    """
    # file = open('todos.txt', 'w')
    # file.writelines(todos)
    # file.close()

    # with this version you don't need to close the file manually
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# print(__name__)
# the lines of code after this if will only be executed when running functions.py script,
# not when this is imported in another script
if __name__ == "__main__":
    print("hello")
    print(get_todos)

# The value of __name__ is "__main__" only when we execute functions.py directly, not when executing it from another file using import
# e.g. when running cli.py, the value of __main__ is functions (the name of the imported module)