# inorder Traversing
def traverse_in_order(node):
    if node is None: 
        return []
    return(traverse_in_order(node.left) + 
           [node.key] + 
           traverse_in_order(node.right))

# preorder traversing
def traverse_pre_order(node):
    if node == None:
        return []
    return ( [node.key] + traverse_pre_order(node.left) + traverse_pre_order(node.right))

# postorder traversing
def traverse_pre_order(node):
    if node == None:
        return []
    return ( traverse_pre_order(node.left) + traverse_pre_order(node.right)+ [node.key] )
