
def read_and_display_file(filename="hackme.txt"):
    try:
        with open(filename, "r") as file:
            print("Here is some information to hack: ")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The File {filename} does not exist")


read_and_display_file()        
