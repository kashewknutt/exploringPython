from source import func

try_fun = func
print("Calling func:")
func()
print("Calling try_fun:")
try_fun()
print("Printing try_fun and calling simultaneously:", try_fun())
print("Printing try_fun without calling:", try_fun)

