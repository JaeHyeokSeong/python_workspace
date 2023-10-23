# reference [1]: https://code-lab1.tistory.com/62 - 이론 설명
# reference [2]: https://8iggy.tistory.com/188 - 구현
# reference [3]: https://www.daleseo.com/python-unittest-testcase/ - unittest 설명
from redBlackTree import RedBlackTree
from node import Node
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

    def test_remove_example1(self):
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

    def test_remove_example2(self):
        data = [35, 20, 50, 10, 30, 40, 80, 5, 37, 45]
        expected_data = [5, 10, 20, 30, 35, 37, 40, 45, 50, 80]
        expected_color = ['Red', 'Black', 'Red', 'Black', 'Black', 'Red', 'Black', 'Red', 'Red', 'Black']

        for d in data:
            self.rbt.insert(d)
        actual_data = self.rbt.inorder_traversal_data()
        actual_color = self.rbt.inorder_traversal_color()

        self.assertEqual(actual_data, expected_data)
        self.assertEqual(actual_color, expected_color)

        self.rbt.remove(40)
        expected_data = [5, 10, 20, 30, 35, 37, 45, 50, 80]
        expected_color = ['Red', 'Black', 'Red', 'Black', 'Black', 'Red', 'Black', 'Red', 'Black']
        actual_data = self.rbt.inorder_traversal_data()
        actual_color = self.rbt.inorder_traversal_color()

        self.assertEqual(actual_data, expected_data)
        self.assertEqual(actual_color, expected_color)

        self.rbt.remove(80)
        expected_data = [5, 10, 20, 30, 35, 37, 45, 50]
        expected_color = ['Red', 'Black', 'Red', 'Black', 'Black', 'Black', 'Red', 'Black']
        actual_data = self.rbt.inorder_traversal_data()
        actual_color = self.rbt.inorder_traversal_color()

        self.assertEqual(actual_data, expected_data)
        self.assertEqual(actual_color, expected_color)

        self.rbt.remove(37)
        expected_data = [5, 10, 20, 30, 35, 45, 50]
        expected_color = ['Red', 'Black', 'Red', 'Black', 'Black', 'Black', 'Red']
        actual_data = self.rbt.inorder_traversal_data()
        actual_color = self.rbt.inorder_traversal_color()

        self.assertEqual(actual_data, expected_data)
        self.assertEqual(actual_color, expected_color)

    def test_remove_example3(self):
        root = Node(35)
        root.color = 'Black'

        n = Node(20)
        root.left = n
        n.parent = root
        n.color = 'Black'

        n = Node(50)
        root.right = n
        n.parent = root
        n.color = 'Black'

        n = Node(10)
        tmp = root.left
        tmp.left = n
        n.parent = tmp
        n.color = 'Red'

        n = Node(30)
        tmp = root.left
        tmp.right = n
        n.parent = tmp
        n.color = 'Red'

        n = Node(40)
        tmp = root.right
        tmp.left = n
        n.parent = tmp
        n.color = 'Black'

        n = Node(80)
        tmp = root.right
        tmp.right = n
        n.parent = tmp
        n.color = 'Black'

        n = Node(5)
        tmp = root.left.left
        tmp.left = n
        n.parent = tmp
        n.color = 'Black'

        n = Node(15)
        tmp = root.left.left
        tmp.right = n
        n.parent = tmp
        n.color = 'Black'

        n = Node(25)
        tmp = root.left.right
        tmp.left = n
        n.parent = tmp
        n.color = 'Black'

        n = Node(33)
        tmp = root.left.right
        tmp.right = n
        n.parent = tmp
        n.color = 'Black'

        n = Node(37)
        tmp = root.right.left
        tmp.left = n
        n.parent = tmp
        n.color = 'Red'

        n = Node(45)
        tmp = root.right.left
        tmp.right = n
        n.parent = tmp
        n.color = 'Red'

        n = Node(2)
        tmp = root.left.left.left
        tmp.left = n
        n.parent = tmp
        n.color = 'Red'

        n = Node(27)
        tmp = root.left.right.left
        tmp.right = n
        n.parent = tmp
        n.color = 'Red'

        expected_data = [2, 5, 10, 15, 20, 25, 27, 30, 33, 35, 37, 40, 45, 50, 80]
        expected_color = ['Red', 'Black', 'Red', 'Black', 'Black', 'Black', 'Red', 'Red', 'Black', 'Black',
                          'Red', 'Black', 'Red', 'Black', 'Black']
        self.rbt.root = root

        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        # remove 15
        expected_data = [2, 5, 10, 20, 25, 27, 30, 33, 35, 37, 40, 45, 50, 80]
        expected_color = ['Black', 'Red', 'Black', 'Black', 'Black', 'Red', 'Red', 'Black', 'Black',
                          'Red', 'Black', 'Red', 'Black', 'Black']
        self.rbt.remove(15)

        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        # remove 33
        expected_data = [2, 5, 10, 20, 25, 27, 30, 35, 37, 40, 45, 50, 80]
        expected_color = ['Black', 'Red', 'Black', 'Black', 'Black', 'Red', 'Black', 'Black',
                          'Red', 'Black', 'Red', 'Black', 'Black']
        self.rbt.remove(33)

        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        # remove 37
        expected_data = [2, 5, 10, 20, 25, 27, 30, 35, 40, 45, 50, 80]
        expected_color = ['Black', 'Red', 'Black', 'Black', 'Black', 'Red', 'Black', 'Black',
                          'Black', 'Red', 'Black', 'Black']
        self.rbt.remove(37)

        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        # remove 35
        expected_data = [2, 5, 10, 20, 25, 27, 30, 40, 45, 50, 80]
        expected_color = ['Black', 'Red', 'Black', 'Black', 'Black', 'Red', 'Black', 'Black',
                          'Black', 'Black', 'Black']
        self.rbt.remove(35)

        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        # remove 40
        expected_data = [2, 5, 10, 20, 25, 27, 30, 45, 50, 80]
        expected_color = ['Black', 'Black', 'Black', 'Black', 'Black', 'Red', 'Black',
                          'Black', 'Black', 'Red']
        self.rbt.remove(40)

        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        # remove 50
        expected_data = [2, 5, 10, 20, 25, 27, 30, 45, 80]
        expected_color = ['Black', 'Black', 'Black', 'Black', 'Black', 'Red', 'Black',
                          'Black', 'Black']
        self.rbt.remove(50)

        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        # remove 80
        expected_data = [2, 5, 10, 20, 25, 27, 30, 45]
        expected_color = ['Black', 'Black', 'Black', 'Black', 'Black', 'Black',
                          'Red', 'Black']
        self.rbt.remove(80)

        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

        # remove 27
        expected_data = [2, 5, 10, 20, 25, 30, 45]
        expected_color = ['Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black']
        self.rbt.remove(27)

        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)

    def test_remove_root_node_case1(self):
        data = [10]
        expected_data = None

        for d in data:
            self.rbt.insert(d)
            self.rbt.remove(d)

        self.assertEqual(self.rbt.root, expected_data)

    def test_remove_root_node_case2(self):
        data = [10, 20]
        expected_data = [20]
        expected_color = ['Black']

        for d in data:
            self.rbt.insert(d)
        self.rbt.remove(10)

        self.assertEqual(self.rbt.inorder_traversal_data(), expected_data)
        self.assertEqual(self.rbt.inorder_traversal_color(), expected_color)
