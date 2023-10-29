# create a class
# here we declared a new class called User
class User:
	def __init__(self, user_id, username):
		self.id = user_id
		self.username = username
		self.followers = 0


# here we made an object using the class
user_1 = User("001", "angela")
print(user_1)
