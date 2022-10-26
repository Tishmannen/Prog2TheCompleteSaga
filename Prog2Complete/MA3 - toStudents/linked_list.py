""" linked_list.py

Student: Thor Lindberg
Mail: thor.ronnegard@gmail.com
Reviewed by: Mikael Johansson
Date reviewed: 28/09-2022
"""

from distutils.log import error
from queue import Empty
from typing import List


class ListError(Exception):
    def __init__(self,function,message):
        self.function = function
        self.message = message
        super(ListError, self).__init__(function,message)

class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):             # Optional
        len = 0
        if self.first is not None:
            f = self.first
            while f:
                len += 1
                f = f.succ
        return len

    def mean(self):               # Optional
        f = self.first
        val = 0
        n = 0
        while f:
            val += f.data
            n += 1
            f = f.succ
        return val/n

    def remove_last(self):        # Optional
        f = self.first
        if self.first is None:
            raise ListError("remove_last","Empty list does not have element to remove")
        elif not f.succ:
            val = f.data
            self.first = None
        else:
            f_temp = f
            while f.succ:
                f_temp = f
                f = f.succ
            val = f.data
            f = f_temp
            f.succ = None
        return val

    def remove(self, x):          # Compulsory
        did = False
        if self.first is None:
            raise ListError("remove","Empty list does not have element to remove")
        else:
            f = self.first
            while f:
                if f.data == x:
                    if f == self.first:
                        self.first = f.succ
                        f = self.first
                    elif not f.succ:
                        f = f_previous
                        f.succ = None
                    else:
                       f_next = f.succ
                       f = f_previous
                       f.succ = f_next
                    did = True
                    break
                f_previous = f
                f = f.succ
        return did



    def count(self, x):           # Optional
        return self._count(x,self.first)

    def _count(self,x,f):
        if f is None:
            return 0
        elif f.data == x:
            return 1+self._count(x,f.succ)
        else:
            return self._count(x,f.succ)

    def to_list(self):            # Compulsory
        return self._to_list(self.first)

    def _to_list(self,f):
        if f is None:
            return []
        else:
            return [f.data]+self._to_list(f.succ)


    def remove_all(self, x):      # Compulsory
        if self == None:
            pass
        else:
            f = self.first
            self._remove_all(x,f,'temp')

    def _remove_all(self,x,f,f_prev):
        if f is None:
            pass
        else:
            if f == self.first and f.data == x:
                self.first = f.succ
                f = self.first
                self._remove_all(x,f,'temp')
            else:
                if not f.succ and f.data == x:
                    f = f_prev
                    f.succ = None
                elif f.data == x:
                    f_next = f.succ
                    f = f_prev
                    f.succ = f_next
                self._remove_all(x,f.succ,f)

    def __str__(self):            # Compulsary
        out = '('
        if self.first == None:
            return out + ')'
        else:
            for i in self.__iter__():
                out = out + str(i) + ', '
            return out[:-2]+')'


    def copy(self):               # Compulsary
        pass
#        result = LinkedList()
#        for x in self:
#            result.insert(x)
#        return result
    ''' Complexity for this implementation: 
        O(n^2), for goes through whole list and insert goes through whole list
    '''

    def copy(self):               # Compulsary
        result = LinkedList()
        if self.first is not None:
            f = self.first
            result.first = result.Node(f.data,result.first)
            g = result.first
            while f:
                if f is not self.first:
                    g.succ = result.Node(f.data,g.succ)
                    g = g.succ
                f = f.succ
        return result
    ''' Complexity for this implementation:
        O(n), goes through list once
    '''

    def __getitem__(self, ind):   # Compulsory
        n = 0
        for i in self:
            if n == ind:
                return i
            n += 1
        if n+1 > ind:
            raise ListError("__getitem__","index out of range")
        


class Person:                     # Compulsory to complete
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"

#sort for personal number
    def __lt__(self, other):
        return self.pnr < other.pnr

    def __gt__(self, other):
        return self.pnr > other.pnr

    def __eq__(self, other):
        return self.pnr == other.pnr
    
    def __ne__(self, other):
        return self.pnr != other.pnr

    def __le__(self, other):
        return self.pnr <= other.pnr

    def __ge__(self, other):
        return self.pnr >= other.pnr

        


def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7,9]:
        lst.insert(x)
    lst.print()

    # Test code:
#    lst2 = LinkedList()
#    lst2.insert(2)
#    print(lst2.length())
#    print(lst.mean())
#    print(lst2.remove_last())
#    lst2.print()
#    print(lst.remove(11))
#    lst.print()
#    print(lst.count(1))
#    print(lst.to_list())
#    lst.remove_all(9)
#    lst.print()
#    print(lst.copy())
#    print(lst[11])
#    lst_name = LinkedList()
#    for x,y in [("test1",55),("test2",2),("test3",39),("test4",4)]:
#        lst_name.insert(Person(x,y))
#    lst_name.print()

if __name__ == '__main__':
    main()
