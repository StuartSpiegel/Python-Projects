from elasticsearch import Elasticsearch
from elasticsearch.serializer import JSONSerializer


class SetEncoder(JSONSerializer):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        if isinstance(obj, Something):
            return 'CustomSomethingRepresentation'
        return JSONSerializer.default(self, obj)


es = Elasticsearch(serializer=SetEncoder())
