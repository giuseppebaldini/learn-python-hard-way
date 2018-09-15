# Inheritance vs. Composition

# Inheritance: child class inherits from parent class
# Actions on the child can:
    # 1 IMPLY an action on the parent
    # 2 OVERRIDE action on the parent
    # 3 ALTER an action on the parent

# 1 Implicit inheritance with empty block using 'pass'

class Parent(object):

def implicit(self):
print("PARENT implicit()")

class Child(Parent):
pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# 2 Explicit inheritance, override using same name

class Parent(object):

def override(self):
print("PARENT override()")

class Child(Parent):

def override(self):
print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

# 3 Special case of overriding - altering using super()

class Parent(object):

def altered(self):
print("PARENT altered()")

class Child(Parent):

def altered(self):
print("CHILD, BEFORE PARENT altered()")
super(Child, self).altered()
print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

# Composition
# Instead of replacing / altering (2 & 3) we can call functions in a module

class Other(object):

def override(self):
print("OTHER override()")

def implicit(self):
print("OTHER implicit()")

def altered(self):
print("OTHER altered()")

class Child(object):

def __init__(self):
self.other = Other()

def implicit(self):
self.other.implicit()

def override(self):
print("CHILD override()")

def altered(self):
print("CHILD, BEFORE OTHER altered()")
self.other.altered()
print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()
