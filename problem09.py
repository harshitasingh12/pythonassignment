import unittest
import helper_llists as llists


def search_linked_list(node, sk):
    tp=node;
    i=1
    if(tp.val==sk): 
        return i 
    else:
        while(tp.val!=sk):
            # print(tp.val,i)
            tp=tp.next
            i=i+1;
    return i

class TestSearchLinkedList(unittest.TestCase):

    def test_01(self):
        node = llists.create_from_string(
            "{val:'arun',next:{val:'babu',next:{val:'john',next:{val:'kavya',next:{val:'raheem',next:{val:'surya',next:None}}}}}}")
        search_key = 'john'
        nodenumber = 3
        self.assertEqual(search_linked_list(node, search_key), nodenumber)

    def test_02(self):
        node = llists.create_from_string(
            "{val:'arun',next:{val:'babu',next:{val:'john',next:{val:'kavya',next:{val:'raheem',next:{val:'surya',next:None}}}}}}")
        search_key = 'surya'
        nodenumber = 6
        self.assertEqual(search_linked_list(node, search_key), nodenumber)

    def test_03(self):
        node = llists.create_from_string(
            "{val:'arun',next:{val:'balu',next:{val:'john',next:{val:'kavya',next:{val:'raheem',next:{val:'surya',next:None}}}}}}")
        search_key = 'arun'
        nodenumber = 1
        self.assertEqual(search_linked_list(node, search_key), nodenumber)

    def test_04(self):
        node = llists.create_from_string(
            "{val:'arun',next:{val:'arun madhav',next:{val:'john',next:{val:'kavya',next:{val:'raheem',next:{val:'surya',next:None}}}}}}")
        search_key = 'arun madhav'
        nodenumber = 2
        self.assertEqual(search_linked_list(node, search_key), nodenumber)


if __name__ == '__main__':
    unittest.main(verbosity=2)