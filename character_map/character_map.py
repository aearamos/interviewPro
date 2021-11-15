def has_character_map(str1, str2):
    if len(str1) != len(set(str1)) or len(str2) != len(set(str2)):
        return False
    else:
        mapped_list = []
        for i in range(len(str1)):
            llist = LinkedList()
            first_node = Node(str1[i])
            second_node = Node(str2[i])
            first_node.next = second_node
            llist.head = first_node
            mapped_list.append(llist)
    print (True)
            
    return list(mapped_list)
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
print(has_character_map('abc', 'def'))    
