"""
File: testbag.py
Author: Ken Lambert
A tester program for bag implementations.
"""

from listbag import ListBag


def test(bagType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    print("Testing", bagType)
    lyst = list(range(1, 11))
    print("The list of items added is:", lyst)
    b = bagType(lyst)
    print("The bag's size:", len(b))
    print("The bag's string:", b)
    print("The bag is empty:", b.isEmpty())
    print("4 is in the bag:", 4 in b)
    print("0 is in the bag:", 0 in b)
    b.add(7)
    print("Add 7 in bag")
    print("The bag's string:", b)
    b.remove(10)
    print("Remove 10 from bag")
    print("The bag's string:", b)
    print("How many instances of 7?", b.count(7))
    c = ListBag(b)
    print("c = ListBag(b)")
    print("b == c?", b == c)
    d = ListBag([22, 4])
    print("d = ListBag(22, 4)")
    print("b == d?", b == d)
    e = b + d
    print("e = b + d")
    print("bag e's string:", e)
    c.clear()
    print("c.clear()")
    print("bag c's string:", c)


test(ListBag)
