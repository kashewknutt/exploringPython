with open("tempfile.txt", 'r')as source_file:
    contents=source_file.read()
    print(contents)
    with open("destination_file.txt", 'w')as bob:
        bob.write(contents)
        print("hoohaa")
