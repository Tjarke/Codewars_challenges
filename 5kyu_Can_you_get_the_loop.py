"""
You are given a node that is the beginning of a linked list. This list always contains a tail and a loop. Your objective is to determine the length of the loop.

For example in the following picture the tail's size is 3 and the loop size is 12:

# Use the `next' attribute to get the following node
node.next


"""

def loop_size(node):
    nodes = [node]
    while True:
        nodes.append(nodes[-1].next)
        if nodes[-1] in nodes[:-1]:
            return len(nodes)-nodes.index(nodes[-1])-1
        
# This should use a dictionary instead of a list and then it is faster:
"""
def loop_size(node):
    index = {}
    i = 0
    while True:
        if node in index:
            return i - index[node]
        index[node] = i
        node = node.next
        i += 1
"""