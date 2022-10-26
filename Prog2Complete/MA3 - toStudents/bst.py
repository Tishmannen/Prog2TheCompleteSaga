""" bst.py

Student: Thor Lindberg
Mail: thor.ronnegard@gmail.com
Reviewed by: Mikael Johansson
Date reviewed: 28/09-2022
"""


from linked_list import LinkedList
import random
import math


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        return self._height(self.root)

    def _height(self,h):
        if h is None:
            return 0
        else:
            return 1+max(self._height(h.left),self._height(h.right))

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      # Compulsory
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left,k)
            # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right,k)
            # r.right =  right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                n = r.right
                while n.left:
                    n = n.left
                r.key = n.key
                r.right = self._remove(r.right,n.key)
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def __str__(self):                            # Compulsory
        s = '<'
        for i in iter(self):
            s = s + str(i) + ', '
        if s == '<':
            s = s + '>'
        else:
            s = s[:-2] + '>'
        return s

    def to_list(self):                            # Compulsory
        lst = []
        for i in iter(self):
            lst.append(i)
        return lst

        #Time complexity:
        #1.39*n*log_2(n)+O(n), it is the average pathlength and append can be ignored since it is O(1)

    def to_LinkedList(self):                      # Compulsory
        lst = LinkedList()
        for i in iter(self):
            lst.insert(i)
        return lst

        #Time complexity:
        #1.39*n*log_2(n)+O(n), it is the average pathlength and insert is O(n)

    def ipl(self):                                # Compulsory
        return self._ipl(self.root,0)
    
    def _ipl(self,r,n):
        if r is None:
            return 0
        else:
            n = n+1
            return n+self._ipl(r.left,n)+self._ipl(r.right,n)


def random_tree(n):                               # Useful
    t = BST()
    for i in range(n):
        t.insert(random.random())
    return t


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")

    for n in range(10000,110000,10000):
        t = random_tree(n)
        div = t.ipl()/n
        div_theo = 1.39*math.log2(n)
        perc_diff = 1-div/div_theo
        print('Height: ' + str(t.height()) + ', n: ' + str(n) + \
            ', IPL/n: ' + str(round(div,3)) + ', theoretical IPL/n: ' + str(round(div_theo,3))\
                 + ', diff IPL: ' + str(round(100*perc_diff,3)) + '%')


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size? Yes since it goes through the tree
2. computing height? No since it doesnt know the structure of the tree
3. contains? Yes, it knows what the tree contains
4. insert? Cant insert since it only yields
5. remove? Cant remove since it only yields




Results for ipl of random trees
===============================
One run:
Height: 31, n: 10000, IPL/n: 16.667, theoretical IPL/n: 18.47, diff IPL: 9.761%
Height: 33, n: 20000, IPL/n: 17.199, theoretical IPL/n: 19.86, diff IPL: 13.396%
Height: 35, n: 30000, IPL/n: 18.414, theoretical IPL/n: 20.673, diff IPL: 10.927%
Height: 42, n: 40000, IPL/n: 19.209, theoretical IPL/n: 21.25, diff IPL: 9.602%
Height: 37, n: 50000, IPL/n: 19.751, theoretical IPL/n: 21.697, diff IPL: 8.972%
Height: 43, n: 60000, IPL/n: 20.942, theoretical IPL/n: 22.063, diff IPL: 5.079%
Height: 38, n: 70000, IPL/n: 19.928, theoretical IPL/n: 22.372, diff IPL: 10.926%
Height: 41, n: 80000, IPL/n: 20.212, theoretical IPL/n: 22.64, diff IPL: 10.722%
Height: 39, n: 90000, IPL/n: 21.732, theoretical IPL/n: 22.876, diff IPL: 5.0%
Height: 39, n: 100000, IPL/n: 21.095, theoretical IPL/n: 23.087, diff IPL: 8.631%

The path length seems to grow as 1.39*n*math.log2(n) + O(n)

The height grows with n but slowly




"""
