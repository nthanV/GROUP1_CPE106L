filename = input("Enter the input file name: ")

try:
    with open(filename, 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")
    exit()

print()
while True:
    print("The file has {} lines.".format(len(lines)))
    try:
        n = int(input('Enter a line number [0 to quit]: '))
        if n == 0:
            break
        elif n < 0 or n > len(lines):
            print("Error: Line number must be between 1 and {}.".format(len(lines)))
            continue
        print("{} : {}".format(n, lines[n - 1].strip()))
    except ValueError:
        print("Invalid input. Please enter a valid line number.")
