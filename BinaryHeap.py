import uuid
import networkx as nx
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, key, color="lightgreen"):
        self.key = key
        self.left = None
        self.right = None
        self.color = color
        self.id = str(uuid.uuid4())

def visualize_binary_tree(root):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}

    def add_nodes_edges(node, pos, x=0, y=0, layer=1):
        if node is not None:
            tree.add_node(node.id, color=node.color, label=node.key)
            if node.left:
                tree.add_edge(node.id, node.left.id)
                l = x - 1 / 2 ** layer
                pos[node.left.id] = (l, y - 1)
                l = add_nodes_edges(node.left, pos, x=l, y=y - 1, layer=layer + 1)
            if node.right:
                tree.add_edge(node.id, node.right.id)
                r = x + 1 / 2 ** layer
                pos[node.right.id] = (r, y - 1)
                r = add_nodes_edges(node.right, pos, x=r, y=y - 1, layer=layer + 1)

    add_nodes_edges(root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Start root
root = TreeNode(0)

nodes = [root]

for key in [4, 5, 10, 1, 3]:

    node = TreeNode(key)

    nodes.append(node)

    # Parent
    parent_index = (len(nodes) - 2) // 2
    parent = nodes[parent_index]

    # Add child to parent
    if parent.left is None:
        parent.left = node
    else:
        parent.right = node

visualize_binary_tree(root)
