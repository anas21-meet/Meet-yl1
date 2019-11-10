class User():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts=[]
		self.messages=[]
		self.texts=[]
	def add_friend(self,email):
		self.friends_list.append(email)
		print(self.name ,'has added ', email, 'as a friend')
	def remove_friend(self,email):
		friends_list.remove(email)
		print(name ,'has removed' ,email, 'as a friend')
	def post(self,text):
		self.posts.append(text)
		print(self.name, 'has posted' ,text)
	def send(self,message):
		self.message=message
		self.messages.append(message)
		print('you sent ',self.name ,'a message:' ,message)
		
	def recieve(self,sender,message):
		self.sender=sender
		self.texts.append(message)
		print(sender,'has sent you a message:' ,message)




	def get_userinfo(self):
		print('Name:',self.name)
		print('Email:',self.email)
		print('password:',self.password)
		print('friends:' ,self.friends_list)
		print('posts:',self.posts)
user1=User('George','Gishaq@js-bethlehem.com','password1456')
user2=User('Loai','loai17@meet.mit.edu','myhiddenpassword123')
user1.add_friend('loai17@meet.mit.edu')
user1.post('hey im george befriend me')
user1.get_userinfo()
user1.send('hey')
user2.recieve('your friend','hey')



