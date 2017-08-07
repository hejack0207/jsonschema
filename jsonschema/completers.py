import json

def _array():
    return ["[]",]

def _boolean():
    return ["true","false"]

def _integer():
    return ["0",]

def _null():
    return ["",]

def _number():
    return ["0.0",]

def _object():
    return ["{}",]

def _string():
    return ["abc",]

completers={
    u"array": _array, u"boolean": _boolean, u"integer": _integer,
    u"null": _null, u"number": _number, u"object": _object,
    u"string": _string,
}   

def complete(schema, completions):
    if 'type' in schema:
        print schema['type']
        c = completers[schema['type']]
        candidates = c()
        print candidates
    else:
        print 'no type'

if __name__ == '__main__':
    with open("../samples/swagger-2.0.json") as file:
        swagger = json.load(file)
        complete(swagger,dict())
