from re import compile
from re import match


#pattern = compile('"(\w+=\w+)"|"(\w+=\w+; )*(\w+=\w+)"')
pattern = compile('"(\w+=\s*\w+; )*(\w+=\s*\w+)"')


checkstr = '"coding=helloworld; foobar=demo; random=error"'
checkstr1 = '"hello=world;;; foo=bar"'
checkstr2 = '"sessionid= 12344556; username= john; loggedin= True"'

if pattern.match(checkstr2):
    print(True)
else:
    print(False)
