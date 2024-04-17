class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution(object):
    def insert(self,node,value):
        
        if node.val==-1:
            node.val=value
        else:
            new=ListNode(value)
            currentNode=node
            while(currentNode.next is not None):
                currentNode=currentNode.next
            currentNode.next=new
            
    def addTwoNumbers(self,l1,l2): #two heads
        l3=ListNode(-1)
        c1=l1
        c2=l2
        temp=0
        while True:
            self.insert(l3,(c1.val+c2.val+temp)%10)
            temp=(c1.val+c2.val)//10
            if(c1.next is None or c2.next is None):
                break
            c1=c1.next
            c2=c2.next
            print("temp after main add func: ", temp)
        print("temp check: ", temp)
        if c1.next is not None:
            print("checkpoint1")
            c1=c1.next
            while True:
                self.insert(l3,(c1.val+temp)%10)
                print("hoohaa",temp)
                temp=(c1.val+temp)//10
                print("temp check raj: ", temp)
                if(c1.next is None):
                    break
                c1=c1.next
        print("temp check: ", temp)
        if c2.next is not None:
            print("checkpoint2")
            c2=c2.next
            while True:
                self.insert(l3,(c2.val+temp)%10)
                print("hoohaa",temp)
                temp=(c2.val+temp)//10
                print("temp check raj: ", temp)
                if(c2.next is None):
                    break
                c2=c2.next
        print("temp check: ", temp)
        if temp!=0:
            print("Check to see if it enters this func")#???? why not enter
            self.insert(l3,temp%10)
            if temp//10 !=0:
                self.insert(l3,temp//10)
        return l3
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example usage:
if __name__ == "__main__":
    # Create linked list 1: 2 -> 4 -> 3
    l1 = ListNode(3)
    l1.next = ListNode(7)
    

    # Create linked list 2: 5 -> 6 -> 4
    l2 = ListNode(9)
    l2.next = ListNode(2)
    

    # Create an instance of Solution class
    solution = Solution()

    # Add the two linked lists
    result = solution.addTwoNumbers(l1, l2)

    # Print the result
    print("Result:")
    print_list(result)
