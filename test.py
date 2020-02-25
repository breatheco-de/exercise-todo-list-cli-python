from app import delete_task, add_one_task, get_todos
import unittest

class TestStringMethods(unittest.TestCase):

    def test_initialize(self):
        self.assertEqual(len(get_todos()), 0, 'The todo list needs to start with cero todos')

    def test_isupper(self):
        add_one_task("Make the bed")
        add_one_task("Make lunch")
        add_one_task("Clean kitchen")
        self.assertEqual(len(get_todos()), 3, 'After adding three tasks, the todo list length must be three')

    def test_split(self):
        delete_task(2)
        self.assertEqual(len(get_todos()), 2, 'After deleting one tasks, the todo list length must be two')
        self.assertEqual(get_todos()[0], "Make the bed", 'After deleting position 2 the first position must still be Make the bed')
        self.assertEqual(get_todos()[1], "Clean kitchen", 'After deleting position 2 the second position must be now Clean kitchen')

if __name__ == '__main__':
    unittest.main()
