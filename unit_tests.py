import unittest
from gameoflife import dead_state, next_board_state

def failed_test(expected_state, actual_state):
    print("FAILED TEST 1")
    print("Expected board state: ")
    print(expected_state)
    print("Actual board state: ")
    print(actual_state)

def compare(expected_next_state, actual_next_state):
    if expected_next_state == actual_next_state:
        print("PASSED TEST 1")
    else:
        failed_test(expected_next_state, actual_next_state)

    # RULE 1: Any living cell with 0-1 living neighbors becomes dead (underpopulation)
    # RULE 2: Any living cell with 2-3 living neighbors stays alive
    # RULE 3: Any living cell with more than 3 living neighbors will die (overpopulation)
    # RULE 4: Any dead cell with exactly 3 live neighbors becomes alive (reproduction)

rows, cols = (5, 5)

class TestGameofLife(unittest.TestCase):
    def test_next_board_state_1(self):
        self.assertEqual(True, False)

        # TEST 1: Dead cells with all dead neighbors remain dead
        initial_state0, expected_next_state0 = dead_state(rows, cols)
        actual_next_state0 = next_board_state(initial_state0)

        compare(expected_next_state0, actual_next_state0)

    def test_next_board_state_2(self):
        self.assertEqual(True, False)

        # TEST 2 (RULE 1, UNDERPOPULATION)
        initial_state1 = [
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_next_state1 = dead_state(rows, cols)
        actual_next_state1 = next_board_state(initial_state1)

        compare(expected_next_state1, actual_next_state1)

    def test_next_board_state_3(self):
        self.assertEqual(True, False)

        # TEST 3 (RULE 2 & RULE 4)
        # each 1 has two neighbors and will stay alive, the 0 neighbor will become alive by reproduction
        initial_state2 = [
            [1, 1],
            [0, 1],
            [0, 0]
        ]
        expected_next_state2 = [
            [1, 1],
            [1, 1],
            [0, 0]
        ]
        actual_next_state2 = next_board_state(initial_state2)

        compare(expected_next_state2, actual_next_state2)

    def test_next_board_state_4(self):
        # TEST 4 (RULE 3 and 4)
        # the living cells with more than three neighbors([0,1] and [1,1]) will die, and the 0 with three neighbors ([0,0])
        # will become alive
        initial_state4 = [
            [0, 1, 1, 0],
            [1, 1, 1, 0]
        ]
        expected_next_state4 = [
            [1, 0, 1, 0],
            [1, 0, 1, 0]
        ]
        actual_next_state4 = next_board_state(initial_state4)

        compare(expected_next_state4, actual_next_state4)

if __name__ == '__main__':
    unittest.main()
