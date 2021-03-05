import unittest
import math

# DO NOT TOUCH THE BELOW CODE


class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# DO NOT TOUCH THE BELOW CODE


def llcreation(ll, num):
    nn = LLNode(num)
    while ll.next != None:
        ll = ll.next
    ll.next = nn


def get_on_switches(link):
    numbers = []
    for word in link.split('->'):
        if word.isdigit():
            numbers.append(int(word))
    root = LLNode(numbers[0])
    for j in range(1, len(numbers)):
        llcreation(root, numbers[j])
    li = []
    while root != None:
        if root.val == 1:
            li.append(0)
        else:
            li.append(int(math.log(root.val, 2)))
        root = root.next
    li.sort()
    res = [] 
    from collections import Counter
    return [item for item, count in Counter(li).items() if count % 2]

# print(get_on_switches("2->4->32->16->64->16->4->64->128->1"))
# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestGetOnSwitches(unittest.TestCase):

    def test_01(self):
        input_string_for_linked_list = "1"
        output_switches = [0]

        self.assertEqual(get_on_switches(
            input_string_for_linked_list), output_switches)

    def test_02(self):
        input_string_for_linked_list = "2->4->32"
        output_switches = [1, 2, 5]

        self.assertEqual(get_on_switches(
            input_string_for_linked_list), output_switches)
    
    def test_03(self):
        input_string_for_linked_list = "2->4->2"
        output_switches = [2]

        self.assertEqual(get_on_switches(
            input_string_for_linked_list), output_switches)

    def test_04(self):
        input_string_for_linked_list = "2->4->32->16->4->2->4"
        output_switches = [2, 4, 5]

        self.assertEqual(get_on_switches(
            input_string_for_linked_list), output_switches)

    def test_05(self):
        input_string_for_linked_list = "2->4->32->16->64->16->4->64->128->1"
        output_switches = [0, 1, 5, 7]

        self.assertEqual(get_on_switches(
            input_string_for_linked_list), output_switches)


if __name__ == '__main__':
    unittest.main(verbosity=2)