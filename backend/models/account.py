class Account:
    def __init__(self, username, password):
        self.username = username 
        self.password = password 
    def toDBCollection(self):
        return{
            'username': self.username,
            'password': self.password
        }
        
