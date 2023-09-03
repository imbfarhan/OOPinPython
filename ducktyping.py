class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")


class Laptop:
    #What matters is, ide object should have method execute let it be pycharm or myeditor, it should have execute method
    #We are not concerned about type of ide, we only have to know that ide should have execute method
    def code(self,ide):
        ide.execute()

ide=PyCharm()
ide=MyEditor()


lap1=Laptop()
lap1.code(ide)