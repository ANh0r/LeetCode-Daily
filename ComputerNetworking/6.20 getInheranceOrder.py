class ThroneInheritance:

    def __init__(self, kingName: str):
        self.name_dict={'':{}}
        self.death_set=set()
        self.birth('',kingName)

    def birth(self, parentName: str, childName: str) -> None:
        self.name_dict[childName]=self.name_dict[parentName][childName]={}

    def death(self, name: str) -> None:
        self.death_set.add(name)

    def getInheritanceOrder(self) -> List[str]:
        curOrder=[]
        def Successor(name):
            for i in self.name_dict[name]:
                if i not in self.death_set:
                    curOrder.append(i)
                Successor(i)
        Successor('')
        return curOrder



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()