class Resistor:
    def __init__(self, type_res: str, nominal: int, capacity: int, precision: int):
        self.type_res = type_res
        self.nominal = nominal
        self.capacity = capacity
        self.precision = precision

    def __str__(self):
        return f'Type: {self.type_res}, nominal: {self.nominal}' \
               f' Om, capacity: {self.capacity} Wt, precision: {self.precision} %'

    def __hash__(self):
        sum_n = 0
        for i in range(1, 5):
            sum_n += self.type_res.__hash__() + self.nominal + self.capacity + self.precision
        return sum_n


class Node:
    def __init__(self, resistor: Resistor):
        self.resistor = resistor
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.node = None
        self.delete_ob = []

    def add_resistor(self, resistor: Resistor):
        self.__add_resistor(resistor, )

    def __add_resistor(self, resistor: Resistor, node: Node = None):
        if node is None:
            node = Node(resistor)

        if self.node is None:
            self.node = node
        else:
            temp = self.node
            while True:
                if temp.resistor.__hash__() == node.resistor.__hash__():
                    break
                if temp.resistor.type_res >= node.resistor.type_res and temp.resistor.nominal >= node.resistor.nominal:
                    if temp.right is None:
                        temp.right = node
                        break
                    else:
                        temp = temp.right
                        continue
                else:
                    if temp.left is None:
                        temp.left = node
                        break
                    else:
                        temp = temp.left
                        continue

    def print_nodes_with_nominal(self, nominal: int):
        if self.node is None:
            print("Empty tree")
            return
        self.__nominal(self.node, nominal)

    def __nominal(self, node: Node, nominal: int):
        if node.left is not None:
            self.__nominal(node.left, nominal)
        if node.right is not None:
            self.__nominal(node.right, nominal)
        if node.resistor.nominal == nominal:
            print(node.resistor)

    def __precision_find(self, node: Node, precision: int):
        if node.left is not None:
            self.__precision_find(node.left, precision)
            if node.left.resistor.precision == precision:
                self.delete_ob.append(node)
        if node.right is not None:
            self.__precision_find(node.right, precision)
            if node.right.resistor.precision == precision:
                self.delete_ob.append(node)

    def print_tree(self):
        if self.node is None:
            print("Empty tree")
            return
        self.__show_tree(self.node)

    def __show_tree(self, node: Node):
        if node.left is not None:
            self.__show_tree(node.left)
        if node.right is not None:
            self.__show_tree(node.right)
        print(node.resistor)

    def delete_tree(self):
        self.__delete_tree(self.node)
        self.node = None

    def __delete_tree(self, node: Node):
        if node.left is not None:
            self.__delete_tree(node.left)
            node.left = None
        if node.right is not None:
            self.__delete_tree(node.right)
            node.right = None
        del node

    def delete_nodes_with_precision(self, precision: int):
        self.__precision_find(self.node, precision)
        if self.node.resistor.precision == precision:
            self.delete_ob.append(self.node)
        count = len(self.delete_ob)
        for i in range(0, count):
            if self.node.resistor.precision == precision:
                left = None
                right = None
                if self.node.left is not None:
                    left = self.node.left
                if self.node.right is not None:
                    right = self.node.right
                del self.node
                self.node = None
                if right is not None:
                    self.__add_resistor(None, right)
                if left is not None:
                    self.__add_resistor(None, left)
            else:
                self.__precision_find(self.node, precision)
                deleted_node = None
                if self.delete_ob[0].left is not None:
                    if self.delete_ob[0].left.resistor.precision == precision:
                        deleted_node = self.delete_ob[0].left
                        self.delete_ob[0].left = None
                else:
                    deleted_node = self.delete_ob[0].right
                    self.delete_ob[0].right = None
                if deleted_node.left is not None:
                    self.__add_resistor(None, deleted_node.left)
                if deleted_node.right is not None:
                    self.__add_resistor(None, deleted_node.right)
            self.delete_ob.clear()


print("\n\nCreate and add Resistors to tree\n")
tree = BinaryTree()
tree.add_resistor(Resistor("d", 100, 100, 80))
tree.add_resistor(Resistor("b", 100, 100, 80))
tree.add_resistor(Resistor("c", 90, 1, 8))
tree.add_resistor(Resistor("a", 80, 1, 9))
tree.add_resistor(Resistor("b", 110, 1, 1))
tree.add_resistor(Resistor("o", 10, 1, 6))
tree.add_resistor(Resistor("f", 70, 1, 6))
tree.print_tree()
print("___________________________________\nDelete all Resistor with precision = 6 \n")
tree.delete_nodes_with_precision(6)
tree.print_tree()
print("___________________________________\nPrint all Resistor with nominal = 100 \n")
tree.print_nodes_with_nominal(100)
print("___________________________________\nDelete tree ")
tree.delete_tree()
tree.print_tree()