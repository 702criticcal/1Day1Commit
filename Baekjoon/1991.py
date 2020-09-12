class Node:

    def __init__(self, item, left_child, right_child):
        self.item = item
        self.left, self.right = left_child, right_child


def preorder(node):
    traversal = []
    traversal.append(node.item)
    if node.left != '.':
        traversal += preorder(tree[node.left])
    if node.right != '.':
        traversal += preorder(tree[node.right])
    return traversal


def inorder(node):
    traversal = []
    if node.left != '.':
        traversal += inorder(tree[node.left])
    traversal.append(node.item)
    if node.right != '.':
        traversal += inorder(tree[node.right])
    return traversal


def postorder(node):
    traversal = []
    if node.left != '.':
        traversal += postorder(tree[node.left])
    if node.right != '.':
        traversal += postorder(tree[node.right])
    traversal.append(node.item)
    return traversal


N = int(input())
tree = {}
for _ in range(N):
    root, left, right = input().split()
    tree[root] = Node(root, left, right)

print(''.join(preorder((tree['A']))))
print(''.join(inorder((tree['A']))))
print(''.join(postorder((tree['A']))))
