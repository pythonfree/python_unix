# This is a sample Python script.
from re import split
import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')

    # if len(sys.argv) == 1:
    #     print("type a keys")
    # elif sys.argv[1:3] == ["--help"]:
    #     print("HELP")
    # elif sys.argv[1:3] == ["--help", "--all"]:
    #     print("Full help")

    match sys.argv[1:]:
        case ["--help"]:
            print("HELP")
        case ["--help", "--all"]:
            print("HELP ALL")
        case ["--help", command]:
            print(f"Help for {command}")
        case ["--help", command, *args]:
            print(f"Help for {command} with {args}")
        case _:
            print("Type keys: --help or --help -- all")

    for val in sys.argv:
        print(val)


