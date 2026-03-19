import pickle
import base64

class UserSession:
    def __init__(self):
        self.username = "guest"
        self.role = "admin"

data = pickle.dumps(UserSession())
print(base64.b64encode(data).decode())
