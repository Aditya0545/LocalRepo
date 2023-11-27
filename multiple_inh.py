class father():
    def dis_father(self):
        print("Late. Vijay Kumar")

class mother():
    def dis_mother(self):
        print("Suman Devi")

class son(father,mother):
    def dis_son(self):
        print("Aditya Kumar")

info = son()
info.dis_father()
info.dis_mother()
info.dis_son()