# reference [1]: https://code-lab1.tistory.com/62 - 이론 설명
# reference [2]: https://8iggy.tistory.com/188 - 구현
# reference [3]: https://www.daleseo.com/python-unittest-testcase/ - unittest 설명
from redBlackTree import RedBlackTree
from unittest import TestCase


class RedBlackTreeTest(TestCase):

    def setUp(self) -> None:
        self.rbt = RedBlackTree()

    def test_insert(self):
        data = [8, 7, 9, 3, 6, 4, 5, 12]
        expected_result_data = [3, 4, 5, 6, 7, 8, 9, 12]
        expected_result_color = ['Red', 'Black', 'Red', 'Red', 'Black', 'Black', 'Black', 'Red']

        for d in data:
            self.rbt.insert(d)
        actual_result_data = self.rbt.inorder_traversal_data()
        actual_result_color = self.rbt.inorder_traversal_color()

        self.assertEqual(actual_result_data, expected_result_data)
        self.assertEqual(actual_result_color, expected_result_color)

    def test_exist_search(self):
        data = [8, 7, 9, 3, 6, 4, 5, 12]
        expected_data = 6

        for d in data:
            self.rbt.insert(d)
        actual_data_node = self.rbt.find(expected_data)

        self.assertEqual(actual_data_node.data, expected_data)

    def test_not_exist_search(self):
        data = [8, 7, 9, 3, 6, 4, 5, 12]
        expected_data = 10

        for d in data:
            self.rbt.insert(d)
        actual_data_node = self.rbt.find(expected_data)

        self.assertEqual(actual_data_node, None)
