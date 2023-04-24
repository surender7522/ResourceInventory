from neo4j import GraphDatabase
from api_models.get_resource import Resource
from scripts.output_pyd.all import all
import json
# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "bitnami1")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()

# def match_person_nodes(tx, name):
#     result = tx.run(
#         "MATCH (tom:Person {name: $name}) RETURN tom",
#         name=name)
#     records = list(result)
#     summary = result.consume()
#     return records, summary


def hot_constraints():
    with driver.session(database="neo4j") as session:
        for i in all:
            uniqueness='CREATE CONSTRAINT resource_{0}_id IF NOT EXISTS FOR (book:{0}) REQUIRE book.id IS UNIQUE'.format(i)
            print(uniqueness)
            session.run(uniqueness)


def add_node(res: Resource):
    ch={}
    for i in res.entityCharacteristics:
        ch[i.name]=i.value
    ch["id"]=res.id
    ch["name"]=res.name
    ch["baseType"]=res.baseType
    ch["href"]=res.href
    ch["source"]=res.source
    ch["version"]=res.version
    ch["entitySpecificationRef"]=json.dumps(res.entitySpecificationRef.dict())
    with driver.session(database="neo4j") as session:
        cmd="CREATE ({1}:{0} {{".format(res.type, res.name) + "{0} }})".format(",".join(f"{key}: '{value}'" for key, value in ch.items()))
        print(cmd)
        session.run(cmd)


def add_rel(id1: str, type1: str, id2: str, type2: str, rel: str):
    with driver.session(database="neo4j") as session:
        cmd="""
        MATCH
        (a:{0}),
        (b:{1}})
        WHERE a.id = '{2}' AND b.id = '{3}'
        CREATE (a)-[r:{4}]->(b)
        RETURN type(r)
        """.format(type1, type2, id1, id2, rel)
        print(cmd)
        session.run(cmd)


def get_node_by_id(id: str):
    with driver.session(database="neo4j") as session:
        cmd="""
        MATCH
        (a)
        WHERE a.id = '{0}'
        RETURN a
        """.format(id)
        print(cmd)
        result=session.run(cmd)
        records = list(result)
        print(" ms "+str(result.consume().result_available_after))
        return records




# with driver.session(database="neo4j") as session:
#     session.execute_write()
    # records, summary = session.execute_read(match_person_nodes, name="Tom Hanks")

# Summary information
# print("The query `{query}` returned {records_count} records in {time} ms.".format(
#     query=summary.query, records_count=len(records),
#     time=summary.result_available_after,
# ))

# # Loop through results and do something with them
# for person in records:
#     print(person.data())


