class Solution(object):
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def insertRajat(self, node, value):
        new = self.ListNode(value)
        if not node:
            return new
        current = node
        while current.next:
            current = current.next
        current.next = new 
        return node 

    def addTwoNumbersRajat(self, l1, l2):  # two heads
        l3 = None  # initialize with None
        c1 = l1
        c2 = l2
        carry = 0
        while c1 or c2 or carry:
            if c1:
                carry += c1.val
                c1 = c1.next
            if c2:
                carry += c2.val
                c2 = c2.next
            l3 = self.insertRajat(l3, carry % 10)
            carry = carry // 10  # Update carry
        return l3

    def addTwoNumbers(self, l1, l2):  # two heads
        l3 = self.ListNode()  # initialize with None
        c1 = l1
        c2 = l2
        carry = 0
        while c1 or c2 or carry:
            if c1:
                carry += c1.val
                c1 = c1.next
            if c2:
                carry += c2.val
                c2 = c2.next
            l3 = self.insertRajat(l3, carry % 10)
            carry = carry // 10  # Update carry
        return self.reverseLinkedList(l3.next)

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example usage:
if __name__ == "__main__":
    # Create an instance of Solution class
    solution = Solution()

    # Create linked list 1: 2 -> 4 -> 3
    l1 = solution.ListNode(2)
    l1.next = solution.ListNode(4)
    l1.next.next = solution.ListNode(3)

    # Create linked list 2: 5 -> 6 -> 4
    l2 = solution.ListNode(5)
    l2.next = solution.ListNode(6)
    l2.next.next = solution.ListNode(4)

    # Add the two linked lists
    result = solution.addTwoNumbersRajat(l1, l2)

    # Print the result
    print("Result:")
    print_list(result)
