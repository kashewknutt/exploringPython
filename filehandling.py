with open('tempfile.txt', 'r') as source_file:
    contents = source_file.read()
    print(contents)

with open('destination_file.txt', 'w') as destination_file:
    destination_file.write(contents)

print("Contents copied successfully!")