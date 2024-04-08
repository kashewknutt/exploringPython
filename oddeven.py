list1 = [1,4,23,1324,6,3456,723,12]

evenlist = []
oddlist = []

for everyelement in list1:
    if everyelement % 2 == 0:
        evenlist.append(everyelement)
    else:
        oddlist.append(everyelement)

print(evenlist, oddlist)
my_dict={"name":"maitreyi","age":9,"weight":85}
print(my_dict)
print("maitreyi's weight is:",my_dict["weight"])