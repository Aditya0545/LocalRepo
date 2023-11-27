class grandparent():
    def g_parent(self):
        print("Grand Parent")

class parent(grandparent):
    def parent(self):
        print("Parent")

class child(parent):
    def child(self):
        print("Child")

obj = child()
obj.g_parent()
obj.parent()
obj.child()