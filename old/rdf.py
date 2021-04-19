import rdflib
import rdflib.namespace

g = rdflib.Graph()
result = g.parse("https://lda.data.parliament.uk/publicationlogs.rdf")

qres = g.query("""
PREFIX schema: <http://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX parl: <http://data.parliament.uk/schema/parl#>

SELECT DISTINCT ?item
WHERE {
    ?item a schema:Article .
    ?item parl:publicationDate ?pub_date .
    ?item parl:ddpModified ?modified .
}
ORDER BY DESC(?pub_date) DESC(?modified)
OFFSET 0
LIMIT 10
"""
)

for (s, p, o) in qres:
    print((s, p, o))
print()

qres = g.query("""
PREFIX parl: <http://data.parliament.uk/schema/parl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
CONSTRUCT {
    ?item parl:paperNumber ?___2 .
    ?item rdfs:label ?___3 .
    ?item parl:publicationDate ?___4 .
    ?item parl:externalLocation ?___5 .
}
WHERE {
    { VALUES ?item {
        <http://data.parliament.uk/resources/1309886>
        <http://data.parliament.uk/resources/1309888>
        <http://data.parliament.uk/resources/1309889>
        <http://data.parliament.uk/resources/1309945>
        <http://data.parliament.uk/resources/1309890>
        <http://data.parliament.uk/resources/1309943>
        <http://data.parliament.uk/resources/1309891>
        <http://data.parliament.uk/resources/1309892>
        <http://data.parliament.uk/resources/1309893>
        <http://data.parliament.uk/resources/1309894>
    } }

    { ?item parl:paperNumber ?___2 . }
    UNION { ?item rdfs:label ?___3 . }
    UNION { ?item parl:publicationDate ?___4 . }
    UNION { ?item parl:externalLocation ?___5 . }
}
""")

for (s, p, o) in qres:
    print(o)

#print(g.serialize(format="turtle").decode("utf-8"))
