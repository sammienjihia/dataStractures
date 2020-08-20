# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    # function to calculation the addition
    def addition(self, l1, l2, ans):
        total = l1.val + l2.val
        ones = total % 10
        tens = total // 10
        ans.val = ans.val + ones
        
        # initialise a new node in the ans list as the next node
        if tens != 0:
            ans.next = ListNode()
            ans.next.val = tens
        return l1.next, l2.next, ans.next
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # we have to traverse the linked lists adding the value of the nodes 
        # which then form the value of our answere linked list
        
        counter = True
        ansList = []
        
        # traversing through the linked list
        while counter is True:
            
            ans = ListNode()
            
            # first check if the current values in both the list are not None
            if (l1 != None and l2 !=None):
                # add the current values
                l1,l2,ans = self.addition(l1, l2, ans)
                    
            # if values in the list are none, then exit
            elif (l1 == None and l2 == None):
                counter = False
                
            # if one of the item in the list is a none
            else:
                # one of the node in the list has a next node of type None
                if l1 == None:
                    
                    l1, l2, ans = self.addition(ListNode(), l2, ans)
                    
                else:
                    l1, l2, ans = self.addition(l1, ListNode(), ans)
                    
        counter2 = True
        while counter2 is True:
            if ans != None:
                ansList.append(ans.val)
                ans = ans.next
            else:
                counter = False
                
        return ansList
                    
                
        
x =  ListNode()    
x.val = 4

y = ListNode()
y.val = 2

z = ListNode()
z.val = 3
        
y.next = x
x.next = z

x1 = ListNode()
x1.val = 5

y1 = ListNode()
y1.val = 6

z1 = ListNode()
z1.val = 4

x1.next = y1
y1.next = z1

v = Solution()
v.addTwoNumbers(x, x1)