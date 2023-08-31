
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        
        # 최종 계산 결과 연결 리스트 변환
        return self.ToReverseLinkedList(str(resultStr))


    #연결 리스트 역순 변환
    def reverseList( self, head : ListNode ) -> ListNode :
        node, prev = head, None

        while node :
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
    
    #연결 리스트를 파이썬 리스트로 변환
    def toList(self, node : ListNode ) -> list:
        list1 : list = []
        while node :
            list1.append(node.val)
            node = node.next
        return list1
    
    #파이썬 리스트를 연결 리스트로 변환
    def ToReverseLinkedList(self, result : str) -> ListNode :
        prev : ListNode = None
        for r in result :
            node = ListNode(r) 
            node.next = prev
            prev = node
        return node
    
