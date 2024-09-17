
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists)==0:
            return None
        
        while len(lists)>1:
            mergedLists=[]
        
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                
                mergedLists.append(self.mergeList(l1,l2))
            lists=mergedLists
        return lists[0]
    
    def mergeList(self,l1: ListNode,l2: ListNode) -> ListNode:
            dummy = ListNode()
            tail = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next=l1
                    l1=l1.next
                else:
                    tail.next= l2
                    l2=l2.next
                tail = tail.next
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return dummy.next
#*-------Tests-------#
#~ Helper function
#~ 1) print linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

#~ 2) create linked list from list of values
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for value in arr:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Example test case
list1 = create_linked_list([1, 4, 5])
list2 = create_linked_list([1, 3, 4])
list3 = create_linked_list([2, 6])

lists = [list1, list2, list3]

# Create a solution instance and call mergeKLists
solution = Solution()
merged_head = solution.mergeKLists(lists)

# Print the result
print_linked_list(merged_head)
#*-------------------#
#^ Time Complexity:
#^ O(nlogk)
#^ Space Complexity: 
#^ 