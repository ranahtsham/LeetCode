# --------------------------------------------------------------------------#
# NAME: Rana Ahtsham Ul Haq                                                 #
# GIT: https://github.com/ranahtsham                                        #
# LEETCODE: https://leetcode.com/ranahtsham/                                #
# LINKEDIN: https://www.linkedin.com/in/ranahtsham                          #
# --------------------------------------------------------------------------#
# DATE: Monday, 6th June 2022                                               #
# PROBLEMS: https://leetcode.com/problems/intersection-of-two-linked-lists/ #
# SUBMISSIONS: https://leetcode.com/submissions/detail/715642553/           #
# --------------------------------------------------------------------------#

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        print(f"headA:-> {printValues(headA)}")
        print(f"headB:-> {printValues(headB)}")
        one = headA
        two = headB

        while one != two:
            print(f"before: ONE:-> {printValues(one)}", end= ' \t ')
            print(f"TWO:-> {printValues(two)}", )
            one = headB if one is None else one.next
            two = headA if two is None else two.next
            print(f"after:  ONE:-> {printValues(one)}", end= ' \t ')
            print(f"TWO:-> {printValues(two)}")

        # # second solution
        # stored_set = set()
        # curr = headA
        # while curr:
        #     stored_set.add(curr)
        #     curr = curr.next
        # curr = headB
        # while curr:
        #     if curr in stored_set:
        #         return curr
        #     curr = curr.next
        # return None
        return one


def printValues(head: ListNode):
    strV = ""
    curr = head
    while curr:
        strV += str(curr.val) + " "
        curr = curr.next
    return strV


if __name__ == '__main__':

    common_tail = ListNode(8)
    common_tail.next = ListNode(4)
    common_tail.next.next = ListNode(5)

    obj1 = ListNode(4)
    obj1.next = ListNode(1)
    obj1.next.next = common_tail

    obj2 = ListNode(5)
    obj2.next = ListNode(6)
    obj2.next.next = ListNode(1)
    obj2.next.next.next = common_tail

    sol = Solution()
    result = sol.getIntersectionNode(obj1, obj2)

    print(f"{ 'Not Intercepts' if result is None else 'Intercepted at ' + str(result.val)  }")

