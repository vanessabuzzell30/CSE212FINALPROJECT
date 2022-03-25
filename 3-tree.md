## Trees

**Trees** are like linked lists in that nodes are connected together by pointers. However, unlike linked lists, a tree can connect to multiple different nodes. We will look at the following types of trees: binary trees, binary search trees, and balanced binary search trees.

# Binary Trees

A **binary** tree is a tree that links to no more than two other **nodes**. In the picture below, the top node is called the **root** node. The nodes that connect to no other nodes are called **leaf** nodes. A node that has connected nodes is called a **parent** node. The node connected to the parent are called **child** nodes. The nodes to the left and right of any parent node form a **subtree**. There is always only one root node. While not shown in the picture, it is common for child nodes to also point back up to the parent node (similar to a linked list).
![Binary Tree Diagram](PictureFiles/binarytree.png)

# Binary Search Trees

A **binary search tree** (BST) is a binary tree that follows rules for data that is put into the tree. Data is placed into the BST by comparing the data with the value in the parent node. If the data being added is less than the parent node, then it is put in the left subtree. If the data being added is greater than the parent node, then it is put in the right subtree. If duplicates are allowed than the duplicate can be put either to the left or to the right of the root. By using this process, the data is stored in the tree sorted.

![Binary Search Tree Diagram](PictureFiles/bst.png)

Using the tree above, we can determine where to put additional items. We always start at the root node and compare the new value with it. We keep comparing until we have found an empty place for the new node.
For example, to find the value 3, do the following:

- Start at the root node 4 and compare with the new value 3

- Since 3 is less than 4, goto the left and visit node 2

- Since 3 is greater than 2, goto the right and see there is the number 3
  You would use the same process to add a number to the tree but you would do this process til there is empty spot.

The process that we used to find where to put the new node was an efficient process. If we had a dynamic array or a linked list containing sorted values, we would have an O(n) operation as we search for the proper location to insert a value into the proper sorted position. By using the BST, we are able to exclude a subtree with each comparison. This ability to split the job in half recursively results in O(log n). Maintaining sorted data in a BST performs better than other data structures.

However, the only reason we had O(log n) in the example above was because the tree was "balanced". To see the difference between a **balanced** and an unbalanced tree, we will construct a tree with the same values but in a different order. The reason why the previous tree has 15 as the root node is because 15 was added first. This time, we will add the values in the following order: 8, 10, 21, 28, 36,
50 (purposefully in ascending order).

![Unbalanced Binary Search Tree Diagram](PictureFiles/unbalanced-bst.jpeg)
This tree is a BST but looks more like a linked list. This BST is unbalanced has a resulting performance for searching of O(n) instead of O(log n).# Balanced Binary Search Trees

# Balanced Binary Search Trees

A **balanced binary search tree** (balanced BST) is a BST such that the difference of height between any two subtrees is not dramatically different. The height of a tree can be found by counting the maximum number of nodes between root and the leaves. Since it is not reasonable to expect that the order of data will result in a balanced BST, numerous algorithms have been written to detect if a tree is unbalanced and to correct the unbalance. Common algorithms include red black trees and AVL (Adelson-Velskii and Landis) trees. The example below shows an **AVL tree** which is balanced because the difference of height between subtrees is less than 2.

![AVL Tree Diagram](PictureFiles/avl_tree_initial.jpeg)

If we add 13 to the right of the 12, we end up with an unbalanced AVL tree because the height of the right subtree from 10 is now 2 more than the left subtree.

![AVL Tree Diagram](PictureFiles/avl_tree_unbalanced.jpeg)

The AVL algorithm will detect that the tree has become unbalanced. To balance the tree, a node rotation will be performed. For our tree, we can rotate the node with 13 so that nodes 12 and 14 are children nodes of the 13. When this rotation is done, the tree returns to a balanced state. An AVL tree will always be a Balanced BST and therefore benefit from O(log n) performance.

![AVL Tree Diagram](PictureFiles/avl_tree_rebalanced.jpeg)

Here is a video to help see and hear about AVL Trees!
[Video on AVL Trees](https://www.youtube.com/watch?v=c7d5qS7RQpA)

# Inserting into a BST

# Traversing a BST

# BST in Python
