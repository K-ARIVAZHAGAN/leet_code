# 2. Add Two Numbers

**LeetCode:** [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)  
**Topic:** Linked List  
**Difficulty:** Medium

## My Approach

I add the linked-list digits one node at a time while keeping track of the carry.

- If either list is empty at the start, return the other list.
- Add the current values from both lists along with the carry.
- Store the last digit in the current node of the first list when possible.
- If the first list has ended but the second still has nodes, create new nodes and attach them.
- After processing both lists, append a final node if a carry remains.

This approach reuses and modifies the first linked list and only creates nodes when needed.

## Solution

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            if not l1:
                return l2
            if not l2:
                return l1

            head = l1
            prev = l1
            carry = 0
            while l1 or l2:

                sum_ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
                carry = sum_//10
                sum_ = sum_%10
                if l1:
                    l1.val = sum_
                    prev = l1
                    l1 = l1.next
                else:
                    newNode = ListNode(sum_, None)
                    prev.next = newNode
                    prev = prev.next

                if l2:
                    l2 = l2.next

            if carry == 1:
                newNode = ListNode(carry, None)
                prev.next = newNode
                prev = prev.next

            return head
```

## Complexity Analysis

Let `m` and `n` be the lengths of the two linked lists.

- **Time Complexity:** O(max(m, n)) — each node in both lists is processed once.
- **Space Complexity:** O(1) auxiliary space, excluding nodes created for the returned result.

## Key Learning

When adding numbers represented by reversed linked lists, process corresponding digits together and propagate the carry to the next position.

## Note

The implementation modifies the first input list in place and may append new nodes to it. The LeetCode environment supplies the `ListNode` and `Optional` definitions.
