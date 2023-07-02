import unittest
import io
from directories import DirectoryTree


class DirectoryTreeTests(unittest.TestCase):
    def setUp(self):
        self.directories = DirectoryTree()

    def test_create(self):
        self.directories.create("foods/grains")
        self.assertEqual(len(self.directories.root.children), 1)
        self.assertIn("foods", self.directories.root.children)
        self.assertIn("grains", self.directories.root.children["foods"].children)

        # cleanup
        self.directories.delete("foods/grains")

    def test_move(self):
        self.directories.create("foods/apple")
        self.directories.create("foods/fruits")
        self.directories.move("foods/apple", "foods/fruits")
        self.assertIn("foods", self.directories.root.children)
        self.assertIn("fruits", self.directories.root.children["foods"].children)
        self.assertNotIn("apple", self.directories.root.children["foods"].children)
        self.assertIn("apple", self.directories.root.children["foods"].children["fruits"].children)

        # cleanup
        self.directories.delete("foods/fruits")

    def test_delete(self):
        self.directories.create("foods/vegitables")
        self.directories.delete("foods/vegitables")
        self.assertNotIn("vegitables", self.directories.root.children["foods"].children)

if __name__ == "__main__":
    unittest.main()