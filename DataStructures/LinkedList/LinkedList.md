## General ideas

LinkedList has *no random access*.

Each element is called a **_node_**, 
whose strcutre has a link called **_next_** pointing to the next node, 
and a **_val_** containing contents.

Note a LinkedList is a chain of nodes. 
You can add node to or delete node from the chain. 
However, the nodes are still there. 
They are not destroyed. 
The only thing matter is that are they hooked to the chain, or not.

By the way, **_head_** is just the name of a normal node.

A trick named "Modify travel Loop" is to first come up with a loop going through the LinkedList,
and then modify on that according to the requirements.

Manipulation on *contents* includes reading or updating.

Manipulation on *nodes* includes adding and deleting.

Useful Data Structures are 
- Hash Table
- List
- Set

Useful Algorithms are 
- Two Pointers: Prev-Curr, Slow-Fast
- Recursion

Useful Tricks are 
- Dummy Node
- Modify travel Loop
