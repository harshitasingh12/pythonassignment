import unittest


def winning_Bosses(fighters, bosses):
    winn = []
    for i in bosses:
        if fighters.count(1) <= i.count(1):
            winn.append(i)
        else:
            continue
    return winn
    


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestWinningBosses(unittest.TestCase):

    def test_01(self):
        fighters = [0, 1, 1]
        bosses = [[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]]
        ans = [[0, 1, 1], [1, 1, 1]]
        self.assertEqual(winning_Bosses(fighters, bosses), ans)

    def test_02(self):
        fighters = [0, 1, 1]
        bosses = [[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]]
        ans = [[0, 1, 1], [1, 1, 1]]
        self.assertEqual(winning_Bosses(fighters, bosses), ans)

    def test_03(self):
        fighters = [0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1]
        bosses = [[0, 0, 0, 0], [0, 0, 1, 1, 1, 1],
                  [0, 1, 1], [1, 1, 1, 1, 1, 1]]
        ans = [[1, 1, 1, 1, 1, 1]]
        self.assertEqual(winning_Bosses(fighters, bosses), ans)


if __name__ == '__main__':
    unittest.main(verbosity=2)
