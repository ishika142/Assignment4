try:
    with open("sample.txt", "r") as file:
        print("Contents of the file:")
        for line in file:
            print(line.rstrip())

except FileNotFoundError:
    print("Error: sample.txt file not found.")



