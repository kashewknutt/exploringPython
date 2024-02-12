def func():
    def inner_fun():
        abc = []
        for i in range(10):
            abc.append(i)
        print("Print statement inside inner function ", abc)
        return abc
    print("Print statement outside inner function")
    return inner_fun

def outer_fun():
    abc = []
    for i in range(10):
        abc.append[i]
    return abc
