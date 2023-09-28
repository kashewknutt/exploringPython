def check_stack_isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
s=[] # An empty list to store stack elements, initially its empty
top = None # This is top pointer for push and pop operation
def main_menu():
    while True:
       print("Stack Implementation")
       print("1 - Push")
       print("2 - Pop")
       print("3 - Peek")
       print("4 - Display")
       print("5 - Exit")
       ch = int(input("Enter the your choice:"))
       
       if ch==1:
           el = input("Enter the value to push an element:")
           push(s,el)
       elif ch==2:
           e=pop_stack(s)
           if e=="UnderFlow":
               print("Stack is underflow!")
           else:
               print("Element popped:",e)
       elif ch==3:
           e=pop_stack(s)
           if e=="UnderFlow":
               print("Stack is underflow!")
           else:
               print("The element on top is:",e)
       elif ch==4:
           display(s)
           continue
       elif ch==5:
           break
       else:
           print("Sorry, You have entered invalid option")
       display(s)
def push(stk,e):
    stk.append(e)
    top = len(stk)-1
def display(stk):
    if check_stack_isEmpty(stk):
        print("Stack is Empty")
    else:
        top = len(stk)-1
        print(stk[top],"-Top")
        for i in range(top-1,-1,-1):
            print(stk[i])
def pop_stack(stk):
    if check_stack_isEmpty(stk):
        return "UnderFlow"
    else:
        e = stk.pop()
        if len(stk)==0:
            top = None
        else:
            top = len(stk)-1
        return e
def peek(stk):
    if check_stack_isEmpty(stk):
        return "UnderFlow"
    else:
        top = len(stk)-1
        return stk[top]
main_menu()
