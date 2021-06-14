# Graph database - neo4j

from py2neo import *

graph = Graph("http://localhost:7474", auth=("neo4j", "database_1"))
#graph.delete_all()

a = Node('Person',name='Julia')
a.add_label('Girl')
graph.create(a)
b = Node('Person',name='lilian')
graph.create(b)
r = Relationship(a,'is_friend',b)
print(a,b,r)

b.update({'name': 'lilian222'})
graph.push(b)


s = a | b | r
graph.create(s)
print(s)

graph.delete_all()
