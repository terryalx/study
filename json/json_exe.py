#!/usr/bin/python3

import json

# ------------------------------ ENCODING == json.dump()

ex1 = json.dumps({'name' : 'ben', 'id' : 223, 'location' : 'ojota'})
print(ex1)

ex2 = json.dumps(['k', 'b', 'a', 'f', 'r'])
print(ex2)

ex3 = json.dumps({'k' : 'kemi', 'b' : 'blessing', 'a' : 'adam', 'f' : 'femi', 'r' : 'rolly'}, sort_keys=True)
print(ex3)


from io import StringIO
io_value = StringIO()
json.dump(['streaming API'], io_value)
value = io_value.getvalue()
print(value)

# ------------------------------ DECODING == json.loads()

ex4 = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(ex4)


















