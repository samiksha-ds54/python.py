# Simulate Folder/File Structure using Binary Tree

# Node of Binary Tree
class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


# Create the folder/file structure
root = Node("Root")

root.left = Node("Documents")
root.right = Node("Pictures")

root.left.left = Node("Resume.txt")
root.left.right = Node("Assignment.pdf")

root.right.left = Node("Photo.jpg")
root.right.right = Node("Wallpaper.png")


# Function to display tree
def display(node, space=""):
    if node is None:
        return

    print(space + "|-- " + node.name)

    display(node.left, space + "    ")
    display(node.right, space + "    ")


# Display folder/file structure
print("FOLDER / FILE STRUCTURE")
print("========================")

display(root)