import Tree from tree

tree = Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)

def test_find():
    found_node_3 = tree.find(3)
    found_node_0 = tree.find(0)
    found_node_8 = tree.find(8)

    assert found_node_3 is not None
    assert found_node_3.data == 3
    
    assert found_node_0 is not None
    assert found_node_0.data == 0
    
    assert found_node_8 is not None
    assert found_node_8.data == 8