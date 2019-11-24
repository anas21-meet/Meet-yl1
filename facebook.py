#Email=input('email-')
#password=input('password-')
posts=[]
#if Email=='Gishaq@js-bethlehem.com':
#	print('hey')
#if password == input('meet'):
#	print(' you have logged in')

class post():
	def __init__(self,name,email,text,comment):
		self.comment=comment
		self.name=name
		self.email=email
		self.text=text
		posts=[]
	def like(self,random,n):
		self.likes=[]
		self.random=random
		self.n=n
		self.likes.append(n)
class comment(post):
	comment_list=[]
	def comment(self):
		self.comment_list.append(self.comment)
	def addpost(self):
		posts.append(poster)
		posts.append(self.text)
		print(self.name +' has posted '+ self.text)


class User():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.messages=[]
		self.texts=[]
	def add_friend(self,email):
		self.friends_list.append(self.email)
		print(self.name ,'has added ', self.email, 'as a friend')
	def remove_friend(self,email):
		self.friends_list.remove(self.email)
		print(self.name ,'has removed' ,self.email, 'as a friend')
	def post(self,text):
		self.text=text
		posts.append(self.text)
		print(self.name, 'has posted' ,self.text)
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
		print('posts:',posts)
user1=User('George','Gishaq@js-bethlehem.com','password1456')
user2=User('Loai','loai17@meet.mit.edu','myhiddenpassword123')
user1.add_friend('loai17@meet.mit.edu')
user1.post('hey im george befriend me')
user1.get_userinfo()
user1.remove_friend('Gishaq@js-bethlehem.com')
user1.send('hey')
user2.recieve('your friend','hey')
poster=comment('george','Gishaq@js-bethlehem.com','hello','great post')
poster.addpost()
poster.comment()











		







