import networkx as nx
import matplotlib.pyplot as plt
from secretsharing import secret_int_to_points, points_to_secret_int

# Define access policy attributes
ATTR1 = "attr1"
ATTR2 = "attr2"
ATTR3 = "attr3"
ATTR4 = "attr4"

# Define access policy formula
policy_formula = """
and
  / \
or  attr2
|   |
1   or
|   / \
attr4  id
"""

# Generate LSSS access tree
policy_tree = nx.DiGraph()
stack = [(policy_tree.add_node(0), policy_formula)]
while stack:
    parent, formula = stack.pop()
    if formula.strip().startswith("and"):
        formula = formula.strip()[3:].strip()
        children = formula.split("\n")
        left_child, right_child = children
        left_node = policy_tree.number_of_nodes() + 1
        right_node = policy_tree.number_of_nodes() + 2
        policy_tree.add_edge(parent, left_node)
        policy_tree.add_edge(parent, right_node)
        stack.append((left_node, left_child))
        stack.append((right_node, right_child))
    elif formula.strip().startswith("or"):
        formula = formula.strip()[2:].strip()
        children = formula.split("\n")
        for child in children:
            child_node = policy_tree.number_of_nodes() + 1
            policy_tree.add_edge(parent, child_node)
            stack.append((child_node, child))
    elif formula.strip().startswith("not"):
        formula = formula.strip()[3:].strip()
        child_node = policy_tree.number_of_nodes() + 1
        policy_tree.add_edge(parent, child_node)
        stack.append((child_node, formula))
    else:
        policy_tree.nodes[parent]["attribute"] = formula

# Assign attributes to nodes
policy_tree.nodes[1][ATTR1] = True
policy_tree.nodes[4][ATTR1] = True
policy_tree.nodes[5][ATTR1] = True
policy_tree.nodes[6][ATTR2] = True
policy_tree.nodes[8][ATTR4] = True
policy_tree.nodes[9]["id"] = "1234567890"

# Visualize access tree
pos = nx.nx_agraph.graphviz_layout(policy_tree, prog="dot")
nx.draw(policy_tree, pos, with_labels=True, node_size=800, font_size=14, font_weight="bold")
nx.draw_networkx_edge_labels(
    policy_tree,
    pos,
    edge_labels={(u, v): "" for u, v in policy_tree.edges},
    font_size=12,
    font_weight="bold",
    label_pos=0.3,
)
plt.show()
