#!/usr/bin/env python
# coding: utf-8

# In[23]:


class TreeNode:
    def __init__(self , x):
        self.val = x
        self.left = None
        self.right = None


# In[24]:


class BST(TreeNode):
    def __init__(self , val ,parent = None):
        super().__init__(val)
        self.parent = parent
        
        
    def insert(self , val):
        if val < self.val:
            if self.left is None:
                new_node = BST(val , parent = self)
                self.left  = new_node
            else:
                self.left.insert(val)
                
                
        else:
            if self.right is None:
                self.right = BST(val , parent = self)
            else:
                self.right.insert(val)


# In[25]:


def print_tree(tree, level=0, label='.'): 
    print(' ' * (level*2) + label + ':', tree.val)
    for child, lbl in zip([tree.left, tree.right], ['L', 'R']):  # do for all children 
        if child is not None:
            print_tree(child, level+1, lbl)


# In[26]:


def find_root(self):
    temp = self
    while temp.parent is not None:
        temp = temp.parent
        
    return temp

BST.find_root = find_root


# In[27]:


def find_min(self):
    min_node = self
    
    if self.left is not None:
        min_node = find_min(self.left)
        
    return min_node

BST.find_min = find_min


# In[28]:


def set_for_parent(self , new_ref):
    if self.parent is None:
        return
    
    if self.parent.right == self:
        self.parent.right = new_ref
        
    if self.parent.left == self:
        self.parent.left = new_ref
        
BST.set_for_parent = set_for_parent


# In[29]:


def replace_with_node(self , node):
    self.set_for_parent(node)
    node.parent = self.parent
    self.parent = None
    return node.find_root()

BST.replace_with_node = replace_with_node


# In[30]:


def delete(self , val):
    if self.parent is None and self.right is None and self.left is None and self.val == val:
        return None
    
    if self.val == val:
        if self.right is None and self.left is None:
            self.set_for_parent(None)
            return self.find_root()
        
    if self.right is None:
        return self.replace_with_node(self.left)
    
    if self.left is None:
        return self.replace_with_node(self.right)
    
    
    successor = self.right.find_min()
    
    self.val = successor.val
    
    
    return self.right.delete(successor.val)



    if val < self:
        if self.left is not None:
            return self.left.delete(val)
        else:
            return self.find_root()
        
    else:
        if self.rigth is not None:
            return self.right.delete(val)
        else:
             return self.find_root()
            
BST.delete = delete
            


# In[33]:


b = BST(5)
b.insert(6)
b.insert(9)
b.insert(4)
print_tree(b)
b.delete(9)
print_tree(b)


# In[ ]:




