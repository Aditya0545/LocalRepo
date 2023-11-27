class parent():
    def parent_info(self):
        print("Parent")

class child(parent):
    def child_info(self):
        print("Child")

obj = child()
obj.child_info()
obj.parent_info()