import database.dao as db

class userService:

    def __init__(self):
        self.dao = db

    def register(self, username, password):
        db.registerUser(username, password)
        print(f'User {username} registered!')

    def login(self, username, password):
        loggedIn, isAdmin, currentUser= db.login(username, password)
        return loggedIn, isAdmin, currentUser

    def viewUsers(self):
        db.viewAllUsers()

    def grantAdmin(self, id):
        db.grantAdmin(id)

    def deleteUser(self, id):
        db.deleteUser(id)    

    