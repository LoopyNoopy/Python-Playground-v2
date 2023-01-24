#Following: https://www.youtube.com/watch?v=idjm8gKsqeI
from neo4j import GraphDatabase

#Establish the connection
graphdb = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j","12345"))

#Search all nodes
session = graphdb.session()
q1 = "MATCH (x) RETURN (x)"
nodes = session.run(q1)
print(nodes.properties())
for node in nodes:
    for item in node:
        print(item)