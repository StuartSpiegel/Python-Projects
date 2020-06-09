from elasticsearch import helpers
from elasticsearch.client import Elasticsearch
import random
from datetime import datetime

# Set global environment variables
elastichost = 'localhost'
port = '9200'
direction = ['in', 'out']  # REST API
outputIndex = 'events'
counter_x = 0  # The number of docs processed (ID number of doc) in range of (x) docs
saveSize = 3
eventCount = 30
es = Elasticsearch([{'host': elastichost, 'port': port}])  # Create the ES instance

# Create the list of actions to hold the docs to import, when stack gets too big push to ES.
actions = []

# Main processing code, append the collected fields to the list and bulk ingest with the BULK API until the push
# point (size)
for k in range(eventCount):
    source = {'size': random.randint(1, 101),
              "duration": random.randint(1, 101),
              "direction": random.choice(direction),
              "id": counter_x
              }
    action = {
        "_index": outputIndex,
        '_op_type': 'index',
        "_type": "_doc",
        "_id": counter_x,
        "_source": source
    }
    actions.append(action)
    counter_x += counter_x
    if len(actions) >= saveSize:
        helpers.bulk(es, actions)
        del actions[0:len(actions)]

    if len(actions) > 0:
        helpers.bulk(es, actions)

    print("Done.")
    print("Docs Processed: " + counter_x)

doc = {
    "author": 'example value',
    "text": 'Elasticsearch is sick bro',
    "timestamp": datetime.now(),
}


def view_backend():
    res = es.index(index="test-index", id=1, body=doc)
    print(res['result'])
    res = es.get(index="test-index", id=1)
    print(res['_source'])
    es.indices.refresh(index="test-index")
    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total']['value'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])


view_backend()
