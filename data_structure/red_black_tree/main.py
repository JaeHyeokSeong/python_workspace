# reference [1]: https://code-lab1.tistory.com/62 - 이론 설명
# reference [2]: https://8iggy.tistory.com/188 - 구현
# reference [3]: https://www.daleseo.com/python-unittest-testcase/ - unittest 설명
from redBlackTree import RedBlackTree
from unittest import TestCase


class RedBlackTreeTest(TestCase):

    def setUp(self) -> None:
        self.rbt = RedBlackTree()

    def test_insert_basic(self):
        data = [8, 7, 9, 3, 6, 4, 5, 12]
        expected_result_data = [3, 4, 5, 6, 7, 8, 9, 12]
        expected_result_color = ['Red', 'Black', 'Red', 'Red', 'Black', 'Black', 'Black', 'Red']

        for d in data:
            self.rbt.insert(d)
        actual_result_data = self.rbt.inorder_traversal_data()
        actual_result_color = self.rbt.inorder_traversal_color()

        self.assertEqual(actual_result_data, expected_result_data)
        self.assertEqual(actual_result_color, expected_result_color)

    def test_insert_complex(self):
        data = [20, 10, 50, 30, 80, 40, 35, 25]
        expected_result_data = [10, 20, 25, 30, 35, 40, 50, 80]
        expected_result_color = [
            'Black', 'Red', 'Red', 'Black', 'Black', 'Black', 'Red', 'Black'
        ]

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

    def test_find_the_smallest_data(self):
        data = [8, 7, 9, 3, 6, 4, -3, 5, 12]
        expected_data = -3

        for d in data:
            self.rbt.insert(d)
        actual_data_node = self.rbt.find_min_node(self.rbt.root)

        self.assertEqual(actual_data_node.data, expected_data)

    def test_remove_node_located_in_root_node_with_size1(self):
        data = 10
        expected_data = None
        expected_root_status = None
        expected_result_data = []

        self.rbt.insert(data)
        self.rbt.remove(data)

        self.assertEqual(self.rbt.find(data), expected_data)
        self.assertEqual(self.rbt.root, expected_root_status)
        self.assertEqual(self.rbt.inorder_traversal_data(),
                         expected_result_data)

    def test_remove_node_located_in_root_node_with_size2(self):
        data = [10, 20]
        remove_data = 10
        expected_data = None
        expected_root_data = 20
        expected_root_color = 'Black'
        expected_result_data = [20]
        expected_result_color = ['Black']

        for d in data:
            self.rbt.insert(d)
        self.rbt.remove(remove_data)

        self.assertEqual(self.rbt.find(remove_data), expected_data)
        self.assertEqual(self.rbt.root.data, expected_root_data)
        self.assertEqual(self.rbt.root.color, expected_root_color)
        self.assertEqual(self.rbt.inorder_traversal_data(),
                         expected_result_data)
        self.assertEqual(self.rbt.inorder_traversal_color(),
                         expected_result_color)

    def test_remove_case4(self):
        data = [20, 5, 40, -10, 80]
        expected_result_data = [5, 20, 40, 80]
        expected_result_color = ['Black', 'Black', 'Black', 'Red']
        for d in data:
            self.rbt.insert(d)
        self.rbt.remove(-10)

        self.assertEqual(self.rbt.inorder_traversal_data(), expected_result_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_result_color)

        self.rbt.remove(5)
        expected_result_data = [20, 40, 80]
        expected_result_color = ['Black', 'Black', 'Black']
        self.assertEqual(self.rbt.inorder_traversal_data(), expected_result_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_result_color)

        self.rbt.remove(20)
        expected_result_data = [40, 80]
        expected_result_color = ['Black', 'Red']
        self.assertEqual(self.rbt.inorder_traversal_data(), expected_result_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_result_color)

    def test_remove_example(self):
        data = [10, 5, 20, 3, 7, 15, 25, 1, 4]
        expected_data = [1, 3, 4, 5, 7, 10, 15, 20, 25]
        expected_color = ['Red', 'Black', 'Red', 'Red', 'Black', 'Black', 'Red', 'Black', 'Red']
        for d in data:
            self.rbt.insert(d)

        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        self.rbt.remove(5)
        expected_data = [1, 3, 4, 7, 10, 15, 20, 25]
        expected_color = ['Black', 'Red', 'Red', 'Black', 'Black', 'Red', 'Black', 'Red']
        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        self.rbt.remove(7)
        expected_data = [1, 3, 4, 10, 15, 20, 25]
        expected_color = ['Black', 'Red', 'Black', 'Black', 'Red', 'Black', 'Red']
        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        self.rbt.remove(10)
        expected_data = [1, 3, 4, 15, 20, 25]
        expected_color = ['Black', 'Red', 'Black', 'Black', 'Black', 'Red']
        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        self.rbt.remove(20)
        expected_data = [1, 3, 4, 15, 25]
        expected_color = ['Black', 'Red', 'Black', 'Black', 'Black']
        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        self.rbt.remove(25)
        expected_data = [1, 3, 4, 15]
        expected_color = ['Black', 'Black', 'Red', 'Black']
        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        self.rbt.remove(15)
        expected_data = [1, 3, 4]
        expected_color = ['Black', 'Black', 'Black']
        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        actual_node = self.rbt.find(3)
        self.assertEqual(actual_node.data, 3)
        actual_node = self.rbt.find(15)
        self.assertEqual(actual_node, None)
