import sys
import logging

class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}


class DirectoryTree:
    def __init__(self):
        self.root = Node("root")
        self.logger = logging.getLogger(__name__)
       
    def create(self, path):
        curr_node = self.root
        components = path.split("/")

        for component in components:
            if component not in curr_node.children:
                curr_node.children[component] = Node(component)
            curr_node = curr_node.children[component]


    def move(self, source, destination):
        source_components = source.split("/")
        source_node = self._find_node(source_components)

        if not source_node:
            self.logger.error(f"Cannot move {source} to {destination} - Invalid source or destination")
            return False

        destination_components = destination.split("/")
        destination_node = self._find_node(destination_components)

        if not destination_node:
            self.logger.error(f"Cannot move {source} to {destination} - Invalid source or destination")
            return False

        destination_node.children[source_components[-1]] = source_node
        parent = self._find_parent(source_components)
        del parent.children[source_components[-1]]
        return True

    def delete(self, path):
        curr_node = self.root
        components = path.split("/")

        for component in components:
            if component not in curr_node.children:
                self.logger.error(f"Cannot delete {path} - {component} does not exist")
                return False
            curr_node = curr_node.children[component]

        parent = self._find_parent(components)
        del parent.children[components[-1]]
        return True
        
        
    def list_all(self):
        self._print_node(self.root, -1)


    def _find_node(self, components):
        curr_node = self.root
        for component in components:
            if component not in curr_node.children:
                return None
            curr_node = curr_node.children[component]
        return curr_node

    def _find_parent(self, components):
        curr_node = self.root
        for component in components[:-1]:
            curr_node = curr_node.children[component]
        return curr_node


    def _print_node(self, node, level):
        if level >= 0:
            indent = "  " * level
            print(indent + node.name)
        for child in sorted(node.children.values(), key=lambda child: child.name):
            self._print_node(child, level + 1)
        


def main():
    directories = DirectoryTree()

    for line in sys.stdin:
        line = line.strip()
        split_line = line.split(" ", 1)

        if len(split_line) >= 2:
            command, args = split_line[0], split_line[1]
            
            if command == "CREATE":
                directories.create(args)
            elif command == "MOVE":
                source, destination = args.split(" ")
                directories.move(source, destination)
            elif command == "DELETE":
                directories.delete(args)
            else:
                print("Invalid Command")            

        elif len(split_line) == 1:
            command = split_line[0]

            if command == "LIST":
                directories.list_all()
            else:
                print("Invalid Command")            

        else:
            print("Invalid input format")


if __name__ == "__main__":
    main()