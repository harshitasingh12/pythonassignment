import unittest
import helper_llists as llists

def sorted_linked_list(node):
    l=[]
    t=node;
    while(t.next!=None):
        l.append(t.val);
        t=t.next;
    l.append(t.val)
    l=sorted(l)
    str=""
    for i in range (0,len(l)):
        str=str+'{val:"'
        str=str+l[i]
        str=str+'",next:'
    str=str+'None'
    for j in range(0,i+1):
        str=str+'}'

    N=llists.create_from_string(str)
    return N

class TestSortingLinkedList(unittest.TestCase):
    
    def test_01(self):
        node = llists.create_from_string(
            '{val:"c",next:{val:"f",next:{val:"a",next:{val:"b",next:{val:"x",next:{val:"k",next:None}}}}}}')
        rotated_list_01 = llists.create_from_string(
            '{val:"a",next:{val:"b",next:{val:"c",next:{val:"f",next:{val:"k",next:{val:"x",next:None}}}}}}')
        self.assertEqual(sorted_linked_list(node), rotated_list_01)

    def test_02(self):
        node = llists.create_from_string(
            '{val:"a",next:{val:"b",next:{val:"c",next:{val:"f",next:{val:"e",next:{val:"d",next:None}}}}}}')
        rotated_list_02 = llists.create_from_string(
            '{val:"a",next:{val:"b",next:{val:"c",next:{val:"d",next:{val:"e",next:{val:"f",next:None}}}}}}')
        self.assertEqual(sorted_linked_list(node), rotated_list_02)

    def test_03(self):
        node = llists.create_from_string(
            '{val:"string",next:None}')
        rotated_list_03 = llists.create_from_string(
            '{val:"string",next:None}')
        self.assertEqual(sorted_linked_list(node), rotated_list_03)

    def test_04(self):
        node = llists.create_from_string(
            '{val:"boy",next:{val:"varanasi",next:{val:"a",next:{val:"to",next:{val:"came",next:None}}}}}')
        rotated_list_04 = llists.create_from_string(
            '{val:"a",next:{val:"boy",next:{val:"came",next:{val:"to",next:{val:"varanasi",next:None}}}}}')
        self.assertEqual(sorted_linked_list(node), rotated_list_04)

    def test_05(self):
        node = llists.create_from_string(
            '{val:"f",next:{val:"e",next:{val:"d",next:{val:"c",next:{val:"b",next:{val:"a",next:None}}}}}}')
        rotated_list_05 = llists.create_from_string(
            '{val:"a",next:{val:"b",next:{val:"c",next:{val:"d",next:{val:"e",next:{val:"f",next:None}}}}}}')
        self.assertEqual(sorted_linked_list(node), rotated_list_05)


if __name__ == '__main__':
    unittest.main(verbosity=2)                

