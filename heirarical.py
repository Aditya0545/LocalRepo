class parent():
    def dis_parent(self):
        print("Father")

class child1(parent):
    def dis_child1(self):
        print("Child1")

class child2(parent):
    def dis_child2(self):
        print("Child2")

obj1 = child1()
obj1.dis_parent()
obj1.dis_child1()

obj2 = child2()
obj2.dis_parent()
obj2.dis_child2()
