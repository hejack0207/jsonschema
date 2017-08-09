import json
from ref_resolver import RefResolver

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

resolver=None

def ref(ref, schema, completions):
    print ref
    scope, resolved = resolver.resolve(ref)
    resolver.push_scope(scope)

    complete(resolved, completions)
    resolver.pop_scope()


def complete(schema, completions):
    print schema
    if 'type' in schema:
        print schema['type']
        c = completers[schema['type']]
        candidates = c()
        completions['values']=candidates

    if 'properties' in schema:
        properties=schema['properties']
        keys=properties.keys()
        #print keys
        completions['keys']=keys
        for key in keys:
            print "key:"+key
            completions[key]=dict()
            complete(properties[key],completions[key])

    if '$ref' in schema:
        print "resolving reference"
        ref(schema["$ref"],schema,completions)
    if "anyOf" in schema:
        for seq in schema["anyOf"]:
            ref(seq["$ref"],schema,completions)
    if "allOf" in schema:
        for seq in schema["allOf"]:
            ref(seq["$ref"],schema,completions)
    if "oneOf" in schema:
        for seq in schema["oneOf"]:
            ref(seq["$ref"],schema,completions)

if __name__ == '__main__':
    with open("../../samples/swagger-2.0.json") as file:
        swagger = json.load(file)
        resolver=RefResolver.from_schema(swagger)
        completion=dict()
        complete(swagger,completion)
        print completion


