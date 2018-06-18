import unittest

from Heap.q855_exam_room import ExamRoom2


class TestExamRoom(unittest.TestCase):
    """Test q855_exam_room.py"""

    def test_exam_room(self):
        # room = ExamRoom(10)
        # self.assertEqual(0, room.seat())
        # self.assertEqual(9, room.seat())
        # self.assertEqual(4, room.seat())
        # self.assertEqual(2, room.seat())
        # self.assertEqual(None, room.leave(4))
        # self.assertEqual(5, room.seat())
        #
        # room = ExamRoom(10)
        # self.assertEqual(0, room.seat())
        # self.assertEqual(9, room.seat())
        # self.assertEqual(4, room.seat())
        # self.assertEqual(None, room.leave(0))
        # self.assertEqual(None, room.leave(4))
        # self.assertEqual(0, room.seat())
        # self.assertEqual(4, room.seat())
        # self.assertEqual(2, room.seat())
        # self.assertEqual(6, room.seat())
        # self.assertEqual(1, room.seat())
        # self.assertEqual(3, room.seat())
        # self.assertEqual(5, room.seat())
        # self.assertEqual(7, room.seat())
        # self.assertEqual(8, room.seat())
        # self.assertEqual(None, room.leave(0))
        #
        # room = ExamRoom(8)
        # self.assertEqual(0, room.seat())
        # self.assertEqual(7, room.seat())
        # self.assertEqual(3, room.seat())
        # self.assertEqual(None, room.leave(0))
        # self.assertEqual(None, room.leave(7))
        # self.assertEqual(7, room.seat())
        # self.assertEqual(0, room.seat())
        # self.assertEqual(5, room.seat())
        # self.assertEqual(1, room.seat())

        self.assertEqual([None, 0, 9, 4, 2, None, 5],
                         ExamRoom2.call(["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"],
                                        [[10], [], [], [], [], [4], []]))

        self.assertEqual([None, 0, 9, 4, None, None, 0, 4, 2, 6, 1, 3, 5, 7, 8, None],
                         ExamRoom2.call(
                             ["ExamRoom", "seat", "seat", "seat", "leave", "leave", "seat", "seat", "seat", "seat",
                              "seat", "seat", "seat", "seat", "seat", "leave"],
                             [[10], [], [], [], [0], [4], [], [], [], [], [], [], [], [], [], [0]]))

        self.assertEqual([None, 0, 7, 3, None, None, 7, 0, 5, 1],
                         ExamRoom2.call(
                             ["ExamRoom", "seat", "seat", "seat", "leave", "leave", "seat", "seat", "seat", "seat"],
                             [[8], [], [], [], [0], [7], [], [], [], []]))

        self.assertEqual([None, 0, 9, 4, 2, None, 5, None, 0, 7],
                         ExamRoom2.call(
                             ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat", "ExamRoom", "seat", "seat"],
                             [[10], [], [], [], [], [4], [], [8], [], []]))

        self.assertEqual([None, 0, None, 0, None, 0, None, 0, None, 0, None],
                         ExamRoom2.call(
                             ["ExamRoom", "seat", "leave", "seat", "leave", "seat", "leave", "seat", "leave", "seat",
                              "leave"],
                             [[1000000], [], [0], [], [0], [], [0], [], [0], [], [0]]))


if __name__ == '__main__':
    unittest.main()
