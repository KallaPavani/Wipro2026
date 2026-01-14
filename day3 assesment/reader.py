from file_package.writer import write_numbers_to_file

def read_file_safely(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:\n")
            print(content)

    except FileNotFoundError:
        print("File not found")

    except PermissionError:
        print("Permission denied")

    

file_name = "numbers.txt"

write_numbers_to_file(file_name)
read_file_safely(file_name)