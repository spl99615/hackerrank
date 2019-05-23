from re import compile


# pattern = compile('"(\w+=\w+)"|"(\w+=\w+; )*(\w+=\w+)"')
pattern = compile(r'"(\w+=\s*\w+; )*(\w+=\s*\w+)"')


checkstr = '"coding=helloworld; foobar=demo; random=error"'
checkstr1 = '"hello=world;;; foo=bar"'
checkstr2 = '"sessionid= 12344556; username= john; loggedin= True"'

if pattern.match(checkstr2):
    print(True)
else:
    print(False)
