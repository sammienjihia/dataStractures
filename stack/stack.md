# Stack
An implementation of the stack data stracture

A stack is a limited access data structure. This means elements can be added or removed from the stack 
only at the top. It follows the first in, last out principle.
Two operations are allowed, push adds an item at the top and pop removes an item from the top.

Applications:
1. Check if a word is a palindrome
2. check if a string of brackets is balances
3. Undo operation in a text editor. This operation is achieved by adding all text operations to a stack
4. Backtracking; where you need to access the most recent elements in a series of elements. Example is a maze.
if you reach a dead end, you need to back track to where you came from.

Implementation:
A stack can be considered an adapter class, basically built on top of another data structure. The underlying 
structure could be an implementation of any collection.

Resource used: https://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html

