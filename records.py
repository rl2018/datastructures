class recordType():
    def __init__ (self,tID,tLastname,tFirstname,tDept):
        self.id=tID
        self.Lastname=tLastname
        self.Firstname=tFirstname
        self.Dept=tDept

# record1 = record(ID, Lastname, Firstname, Dept)
record1=recordType(2468,"Jones","John",243)
print(record1.Lastname)

record2=recordType(3579,"Smith","Sam",634)
print(record2.Lastname)

record3=recordType(1428,"Zimmer","Zoe",243)
print(record3.Lastname)

people=[
    recordType(2468,"Jones","John",243),
    recordType(3579,"Smith","Sam",634),
    recordType(1428,"Zimmer","Zoe",243)
]

print(people[0].Lastname)
print(people[1].Lastname)
print(people[2].Lastname)