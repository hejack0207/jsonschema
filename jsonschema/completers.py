from jsonschema import _utils

completers={
    u"array": _array, u"boolean": _boolean, u"integer": _integer,
    u"null": _null, u"number": _number, u"object": _object,
    u"string": _string,
}   

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
