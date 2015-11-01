import unittest
from elevator import Elevator

class test_elevator(unittest.TestCase):

    def setUp(self):
        self.e = Elevator(id=10)

    def test_update(self):
        self.e.update(4, 9)
        self.assertEqual(self.e.floor, 4)
        self.assertEqual(self.e.goal, 9)
        self.assertEqual(self.e.direction, 1)
        self.e.update(10, 5)
        self.assertEqual(self.e.floor, 10)
        self.assertEqual(self.e.goal, 5)
        self.assertEqual(self.e.direction, -1)

    def test_add_request(self):
        self.e.update(5, 8)
        self.assertEqual(self.e.floor, 5)
        self.assertEqual(self.e.goal, 8)

        # add request in the direction of the elevator
        self.e.addRequest(7, 10)
        self.assertEqual(self.e.floor, 5)
        self.assertEqual(self.e.goal, 7)

        # test priority queue implement. closest floor gets updated
        # hence no FCFS
        self.e.addRequest(6, 10)
        self.assertEqual(self.e.floor, 5)
        self.assertEqual(self.e.goal, 6)

    def test_step(self):
        # setting a starting state
        self.e.update(3, 9)
        self.assertEqual(self.e.floor, 3)
        self.assertEqual(self.e.goal, 9)

        # moving quickly through time
        for i in range(3):
            self.e.step()
            self.assertEqual(self.e.floor, i+1+3)
            self.assertEqual(self.e.goal, 9)
        self.assertEqual(self.e.floor, 6)
        self.assertEqual(self.e.goal, 9)

        # add a new request and making sure
        # goals are updated correctly
        self.e.addRequest(7, 11)
        self.assertEqual(self.e.goal, 7)
        self.e.step()
        self.assertEqual(self.e.goal, 9)
        self.e.step()
        self.e.step()
        self.assertEqual(self.e.floor, 9)
        self.assertEqual(self.e.goal, 11)

        # calling step multiple times shouldn't change 
        # state when the lift has stopped
        for i in range(10):
            self.e.step()
        self.assertEqual(self.e.floor, 11)
        self.assertEqual(self.e.goal, 11)


if __name__ == "__main__":
    unittest.main()
