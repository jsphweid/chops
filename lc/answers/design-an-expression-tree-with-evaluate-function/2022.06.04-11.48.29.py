import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

    
class MyNode(Node):
    left: 'MyNode'
    right: 'MyNode'
    def __init__(self, value: str, left=None, right=None):
        super().__init__()
        self.value = value
        self.left = left
        self.right = right
    
    def evaluate(self):
        if self.value.isdigit():
            return int(self.value)
        left = self.left.evaluate()
        right = self.right.evaluate()
        if self.value == "+":
            return left + right
        elif self.value == "-":
            return left - right
        elif self.value == "*":
            return left * right
        else:
            return int(left / right)
    
    
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for item in postfix:
            node = MyNode(item)
            if not item.isdigit():
                right, left = stack.pop(), stack.pop()
                node.left, node.right = left, right
            stack.append(node)
        return stack[0]
        
        
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
