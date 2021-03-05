import unittest
import helper_llists as llists

import unittest
import helper_llists as llists
import math

def get_on_switches(node):
    """
    ??? Write what needs to be done ???
    """
    l=[]
    while(node!=None):
        l.append(node.val)
        node=node.next
        switch_final=[]
    for switch in l:
        s=int(math.log(int(switch),2))
        if(s in switch_final):
            switch_final.remove(s)
        else:
            switch_final.append(s)
    return sorted(switch_final)            

    pass


class TestGetOnSwitches(unittest.TestCase):

    def test_01(self):
        node = llists.create_from_string(
            "{val:1,next:None}")

        output_switches = [0]

        self.assertEqual(get_on_switches(node), output_switches)

    def test_02(self):
        node = llists.create_from_string(
            "{val:2,next:{val:4,next:{val:32,next:None}}}")

        output_switches = [1, 2, 5]

        self.assertEqual(get_on_switches(node), output_switches)

    def test_03(self):
        node = llists.create_from_string(
            "{val:2,next:{val:4,next:{val:2,next:None}}}")

        output_switches = [2]

        self.assertEqual(get_on_switches(node), output_switches)

    def test_04(self):
        node = llists.create_from_string(
            "{val:2,next:{val:4,next:{val:32,next:{val:16,next:{val:4,next:{val:2,next:{val:4,next:None}}}}}}}")

        output_switches = [2, 4, 5]

        self.assertEqual(get_on_switches(node), output_switches)

    def test_05(self):
        node = llists.create_from_string(
            "{val:2,next:{val:4,next:{val:32,next:{val:16,next:{val:64,next:{val:16,next:{val:4,next:{val:64,next:{val:128,next:{val:1,next:None}}}}}}}}}}")

        output_switches = [0, 1, 5, 7]

        self.assertEqual(get_on_switches(node), output_switches)


if __name__ == '__main__':
    unittest.main(verbosity=2)
