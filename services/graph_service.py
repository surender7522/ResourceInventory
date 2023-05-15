from neo4j import GraphDatabase
from api_models.get_resource import Resource
from scripts.output_pyd.all import all
import json
# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "bitnami1")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()

def time_query(query):
    with driver.session(database="neo4j") as session:
        result = session.run(
            query)
        print(result.data())
        records = list(result)
        # for item in records:
        #     print(item.data())
        summary = result.consume()
        return str(len(records))+" "+str(summary.result_consumed_after)



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
    ch["type"]=res.type
    ch["href"]=res.href
    ch["source"]=res.source
    ch["version"]=res.version
    ch["entitySpecificationRef"]=json.dumps(res.entitySpecificationRef.dict())
    with driver.session(database="neo4j") as session:
        cmd="CREATE (`{1}`:{0} {{".format(res.type, res.name) + "{0} }})".format(",".join(f"{key}: '{value}'" for key, value in ch.items()))
        #print(cmd)
        session.run(cmd)


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


def get_node_by_id(id: str):
    with driver.session(database="neo4j") as session:
        cmd="MATCH (a {id: '"+"{0}'}}) OPTIONAL MATCH (a)-[r]->(b) RETURN type(r),a,b".format(id)
        #cmd="MATCH (a {id: '"+"{0}'}})-[r]->(b) RETURN type(r), a, b".format(id)
        print(cmd)
        result=session.run(cmd)
        records = list(result)
        print(" ms "+str(result.consume().result_available_after))
        return records


def get_node(fields: str  = None, offset: str  = None, limit: str  = None, depth: str = None, expand: str = None,
             relationships: str = None):
    _fields=[]
    if fields:
        list_fields = fields.split(",")
        for item in list_fields:
            field_split = item.split("=")
            _rel = field_split[0].split(".")[-1]
            rel='='
            if _rel=="gt":
                rel=">"
            elif _rel=="gte":
                rel=">="
            elif _rel=="lt":
                rel="<"
            elif _rel=="lte":
                rel="<="
            elif _rel =="eq":
                rel="="
            fieldname = field_split[0].split(".")[0]
            value = field_split[-1]
            _fields.append({"rel": rel, "name": fieldname, "value": value})
    cmd="MATCH (a) "
    if _fields:
        cmd+="WHERE "
        _cmd=" AND ".join("a.{0} {1} '{2}'".format(item["name"], item["rel"], item["value"]) for item in _fields)
        cmd+=_cmd
    cmd+=" OPTIONAL MATCH (a)-[r]->(b) "
    cmd+=" RETURN type(r),a,b"
    if offset:
        cmd+=" SKIP {0}".format(offset)
    if limit:
        cmd+=" LIMIT {0}".format(limit)

    #cmd="MATCH (a {id: '"+"{0}'}})-[r]->(b) RETURN type(r), a, b".format(id)
    print(cmd)
    with driver.session(database="neo4j") as session:
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


