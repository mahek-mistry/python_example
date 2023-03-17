d={101:"mahek",202:"ronik",303:"jay",456:"manya",562:"heli"}

print(d)

d1=d.copy()
print(d1)

print(d.get(202))
print(d[303])

print(d.items())
print(d.keys())
print(d.values())

print(d.pop(456))
print(d.popitem())

d2={245:"shivangi",879:"kevin",245:"riya",209:"jiya"}
d.update(d2)
print(d)
d[270]="meet"
print(d)

for i in d:
    print(i," : ",d[i])
