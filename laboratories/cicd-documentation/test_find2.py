import Tree from tree

tree = Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)

def test_find():
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)

    found_node_1 = tree.find(1)
    found_node_5 = tree.find(5)
    
    assert found_node_1 is None
    assert found_node_5 is None