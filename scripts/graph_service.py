from neo4j import GraphDatabase

import json
# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "bitnami1")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()

def add_rel(id1: str, type1: str, id2: str, type2: str, rel: str):
    print("{0} {1} {2} {3} {4}".format(id1, type1, id2, type2, rel))
    with driver.session(database="neo4j") as session:
        cmd="""
        MATCH
        (a:{0}),
        (b:{1})
        WHERE a.id = '{2}' AND b.id = '{3}' AND NOT (a)-[:{4}]->(b)
        CREATE (a)-[r:{4}]->(b)
        RETURN type(r)
        """.format(type1, type2, id1, id2, rel)
        print(cmd)
        session.run(cmd)