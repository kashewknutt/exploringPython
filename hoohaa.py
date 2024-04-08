with open("tempfile.txt", 'r')as source_file:
    contents=source_file.read()
    print(contents)
    with open("destination_file.txt", 'w')as source_file:
        source_file.write(contents)
        print("hoohaa")
