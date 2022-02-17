class Solution:
	def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
		res, curr = head, head
		try:
			while True:
				for _ in range(m-1):
					curr = curr.next
				last = curr
				curr = curr.next
				last.next = None
				for _ in range(n):
					curr = curr.next
				last.next = curr
		except:
			return res
