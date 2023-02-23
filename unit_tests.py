from linked_list import LinkedList
from stack import Stack
from main import are_parentheses_matched

##################################################
##               Linked List Tests              ##
##################################################

def test_empty_list_append():
    l = LinkedList()
    l.append(3)
    # state of Linked List:
    # [3]
    assert l.size == 1
    assert l.HEAD.element == 3
    assert l.HEAD == l.TAIL
    assert l.TAIL.element == 3

def test_general_append():
    l = LinkedList()
    l.append(3)
    l.append(5)
    # state of Linked List:
    # [3]<->[5]
    assert l.size == 2
    assert l.HEAD.element == 3
    assert l.HEAD.next == l.TAIL
    assert l.TAIL.prev == l.HEAD
    assert l.TAIL.element == 5

    l.append(7)
    # state of Linked List:
    # [3]<->[5]<->[7]
    assert l.size == 3
    assert l.HEAD.element == 3
    assert l.HEAD.next.element == 5
    assert l.TAIL.prev.element == 5
    assert l.TAIL.element == 7

def test_empty_list_prepend():
    l = LinkedList()
    l.prepend(3)
    # state of Linked List:
    # [3]
    assert l.size == 1
    assert l.HEAD.element == 3
    assert l.HEAD == l.TAIL
    assert l.TAIL.element == 3

def test_general_prepend():
    l = LinkedList()
    l.prepend(3)
    l.prepend(5)
    # state of Linked List:
    # [5]<->[3]
    assert l.size == 2
    assert l.HEAD.element == 5
    assert l.HEAD.next == l.TAIL
    assert l.TAIL.prev == l.HEAD
    assert l.TAIL.element == 3

    l.prepend(7)
    # state of Linked List:
    # [7]<->[5]<->[3]
    assert l.size == 3
    assert l.HEAD.element == 7
    assert l.HEAD.next.element == 5
    assert l.TAIL.prev.element == 5
    assert l.TAIL.element == 3

def test_insert():
    l = LinkedList()
    l.insert(3, 0)
    assert l.size == 1
    assert l.HEAD.element == 3
    assert l.TAIL.element == 3
    l.insert(5,1)
    assert l.size == 2
    assert l.HEAD.element == 3
    assert l.HEAD.next == l.TAIL
    assert l.TAIL.prev == l.HEAD
    assert l.TAIL.element == 5
    l.insert(4,1)
    assert l.size == 3
    assert l.HEAD.element == 3
    assert l.HEAD.next.element == 4
    assert l.TAIL.prev.element == 4
    assert l.TAIL.element == 5

def test_contains():
    l = LinkedList()
    assert l.contains(-1) == False
    l.append(3)
    assert l.contains(-1) == False
    assert l.contains(3) == True
    l.append(5)
    assert l.contains(-1) == False
    assert l.contains(3) == True
    assert l.contains(5) == True

def test_get():
    l = LinkedList()
    l.append(3)
    l.append(5)
    l.append(7)
    # state of Linked List:
    # [3]<->[5]<->[7]
    assert l.get(0) == 3
    assert l.get(1) == 5
    assert l.get(2) == 7

def test_remove_first():
    l = LinkedList()
    l.append(3)
    l.append(5)
    l.append(7)
    # state of Linked List:
    # [3]<->[5]<->[7]

    l.remove_first()
    # state of Linked List:
    # [5]<->[7]
    assert l.size == 2
    assert l.HEAD.element == 5
    assert l.TAIL.element == 7
    assert l.HEAD.prev == None

    l.remove_first()
    # state of Linked List:
    # [7]
    assert l.size == 1
    assert l.HEAD.element == 7
    assert l.TAIL.element == 7
    assert l.HEAD.prev == None

    l.remove_first()
    # state of Linked List:
    # []
    assert l.size == 0
    assert l.HEAD == None
    assert l.TAIL == None

def test_remove_last():
    l = LinkedList()
    l.append(3)
    l.append(5)
    l.append(7)
    # state of Linked List:
    # [3]<->[5]<->[7]

    l.remove_last()
    # state of Linked List:
    # [3]<->[5]
    assert l.size == 2
    assert l.HEAD.element == 3
    assert l.TAIL.element == 5
    assert l.TAIL.next == None

    l.remove_last()
    # state of Linked List:
    # [3]
    assert l.size == 1
    assert l.HEAD.element == 3
    assert l.TAIL.element == 3
    assert l.TAIL.next == None

    l.remove_last()
    # state of Linked List:
    # []
    assert l.size == 0
    assert l.HEAD == None
    assert l.TAIL == None

def test_remove_special_cases():
    # Test that attempting to remove an
    # element not in the list does not change
    # the list
    a = LinkedList()
    a.append(2)
    a.remove(1)
    assert a.size == 1
    assert a.HEAD.element == 2
    assert a.TAIL.element == 2
    # Test that removing the element from a
    # single element list results in an
    # empty list
    a = LinkedList()
    a.append(2)
    a.remove(2)
    assert a.size == 0
    assert a.HEAD == None
    assert a.TAIL == None

def test_remove_general():
    a = LinkedList()
    a.append(2)
    a.append(3)
    a.append(5)
    a.append(3)
    # state of a
    # [2]<->[3]<->[5]<->[3]
    a.remove(3)
    # state of a should be
    # [2]<->[5]<->[3]
    b = LinkedList()
    b.append(2)
    b.append(5)
    b.append(3)
    assert a == b


def test_eq():
    a = LinkedList()
    b = LinkedList()
    assert a == b
    a.append(1)
    b.append(1)
    assert a == b
    a.append(2)
    b.append(2)
    assert a == b
    a.append(3)
    b.append(4)
    assert a != b

##################################################
##                   Stack Tests                ##
##################################################

def test_stack():
    s = Stack()
    s.push(1)
    assert s.top() == 1
    s.push(2)
    assert s.top() == 2
    s.push(3)
    assert s.top() == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()

##################################################
##              Parens Checker Tests            ##
##################################################

def test_empty_string():
    assert are_parentheses_matched("") == True

def test_single_char_strings():
    assert are_parentheses_matched("(") == False
    assert are_parentheses_matched(")") == False

def test_simple_matched_parens():
    assert are_parentheses_matched("()") == True
    assert are_parentheses_matched("(())") == True
    assert are_parentheses_matched("()()") == True

def test_simple_unmatched_parens():
    assert are_parentheses_matched("())") == False
    assert are_parentheses_matched("(()") == False

def test_complex_matched_parens():
    assert are_parentheses_matched("((())())") == True

def test_complex_unmatched_parens():
    assert are_parentheses_matched("(()))") == False
    assert are_parentheses_matched("((())") == False