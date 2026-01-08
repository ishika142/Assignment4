
data = input("Enter some text to write into the file: ")

file = open("output.txt", "w")
file.write(data + "\n")
file.close()

additional_data = input("Enter additional text to append: ")

file = open("output.txt", "a")
file.write(additional_data + "\n")
file.close()

file = open("output.txt", "r")
content = file.read()
file.close()

print("\nFinal content of the file:")
print(content)
