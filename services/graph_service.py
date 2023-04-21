from neo4j import GraphDatabase

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "bitnami1")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()

def match_person_nodes(tx, name):
    result = tx.run(
        "MATCH (tom:Person {name: $name}) RETURN tom",
        name=name)
    records = list(result)
    summary = result.consume()
    return records, summary

with driver.session(database="neo4j") as session:
    records, summary = session.execute_read(match_person_nodes, name="Tom Hanks")

# Summary information
print("The query `{query}` returned {records_count} records in {time} ms.".format(
    query=summary.query, records_count=len(records),
    time=summary.result_available_after,
))

# Loop through results and do something with them
for person in records:
    print(person.data())

session.close()
driver.close()