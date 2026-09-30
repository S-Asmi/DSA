class Solution:
    def addTwoNumbers(self, l1, l2):

        head = l1

        temp1 = l1
        temp2 = l2

        carry = 0

        prev = None

        while temp1 and temp2:

            total = temp1.val + temp2.val + carry

            temp1.val = total % 10

            carry = total // 10

            prev = temp1

            temp1 = temp1.next
            temp2 = temp2.next

        if temp1:

            while temp1:

                total = temp1.val + carry

                temp1.val = total % 10

                carry = total // 10

                prev = temp1

                temp1 = temp1.next

                if carry == 0:
                    return head

        elif temp2:

            prev.next = temp2

            while temp2:

                total = temp2.val + carry

                temp2.val = total % 10

                carry = total // 10

                prev = temp2

                temp2 = temp2.next

                if carry == 0:
                    return head

        if carry:

            prev.next = ListNode(carry)

        return head

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         # find the length of both the LL and then use the bigger one to add the smaller one in it

#         # def find_len(head:Optional[ListNode]) -> int:
#         #     temp = head
#         #     count = 0
#         #     while temp:
#         #         temp = temp.next
#         #         count += 1
            
#         #     return count
        
#         # ll1 = find_len(l1)
#         # ll2 = find_len(l2)

#         # i decided that i will add on the list 1
#         temp1 = l1
#         temp2 = l2
#         carry = 0
#         while temp1 != None and temp2!= None:
#             sum_tot = temp1.val + temp2.val + carry
#             rem = sum_tot % 10
#             temp1.val = rem
#             carry =  sum_tot // 10
#             temp1= temp1.next
#             temp2= temp2.next
        
#         if temp1!= None:
#             while temp1 != None:
#                 sum_tot = temp1.val + carry
#                 temp1.val = sum_tot % 10
#                 carry = sum_tot // 10
#                 if carry == 0:
#                     return l1
#                 temp1= temp1.next

#         elif temp2!= None:
#             temp1.next = temp2
#             while temp2 != None:
#                 sum_tot = temp2.val + carry
#                 temp2.val = sum_tot % 10
#                 carry = sum_tot // 10
#                 if carry == 0:
#                     return l1
#                 temp2 = temp2.next
        
#         if carry!=0:
#             new_node = ListNode()
#             new_node.val = carry
#             # new_node.next = None
#             temp1.next = new_node
        
#         return l1



            
