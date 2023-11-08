class User:
    # pass
    # Constructor / Initialize
    # self is the object that
    # is being initialized
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.follower = 0
        self.following = 0
        
    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User("001", "alex")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
