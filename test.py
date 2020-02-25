from app import delete_task, add_one_task, get_todos, save_todos, load_todos
import unittest, csv

class TestStringMethods(unittest.TestCase):

    def test_a_initialize(self):
        self.assertEqual(len(get_todos()), 0, 'The todo list needs to start with cero todos')

    def test_b_add(self):
        add_one_task("Make the bed")
        add_one_task("Make lunch")
        add_one_task("Clean kitchen")
        self.assertEqual(len(get_todos()), 3, 'After adding three tasks, the todo list length must be three')

    def test_c_delete(self):
        delete_task(2)
        self.assertEqual(len(get_todos()), 2, 'After deleting one tasks, the todo list length must be two')
        self.assertEqual(get_todos()[0], "Make the bed", 'After deleting position 2 the first position must still be Make the bed')
        self.assertEqual(get_todos()[1], "Clean kitchen", 'After deleting position 2 the second position must be now Clean kitchen')
    
    def test_d_save(self):
        save_todos()
        file = open("todos.csv", "r") 
        file_content = csv.reader(file)
        _todos = []
        for row in file_content:
            _todos.append(row[0])
        file.close()
        self.assertEqual(get_todos(), _todos, 'The todos on the RAM memory have to be the same TODOs on the todos.csv')

    def test_e_load(self):
        file = open('todos.csv', 'w+') # open the file for writing 'w', create if it doesn't exists
        file.write('\n'.join(['jump', 'run', 'roll'])) # write the content
        file.close() # close the file
        load_todos()
        self.assertEqual(get_todos(), ['jump', 'run', 'roll'], 'The todos on the RAM memory have to be the same TODOs on the todos.csv')

if __name__ == '__main__':
    unittest.main()