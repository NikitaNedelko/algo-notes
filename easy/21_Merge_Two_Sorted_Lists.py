"""21. Merge Two Sorted Lists

Скорость работы:
Затрачено памяти:
"""


class ListNode(object):
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None):
        merged_list = ListNode(0)
        tail = merged_list

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2

        return merged_list.next


if __name__ == "__main__":
    solution = Solution()
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    print(solution.mergeTwoLists(nums1, nums2))

"""
1 2 4 5 6 7 9 10
2 8 12

1 2 4
1 3 4
"""
