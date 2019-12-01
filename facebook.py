import turtle
import sys
turtle.bgpic('logo.gif')
Email=input('email-')
password=input('password-')
posts=[]
if Email=='george'and password == input('meet') :
	print('hey')
	print(' you have logged in')
elif Email!='george' and password != input('meet') :
	sys.exit()
class post():
	def __init__(self,name,email,text):
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
	def comment(self,comment):
		self.comment=comment
		self.comment_list.append(self.comment)
		print('anas has commented on '+self.name+"'s post: "+self.comment )
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
		print('you sent ','Anasabbassi' ,'a message:' ,message)
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
user1=User('George','Anasabbassi@js-bethlehem.com','password1456')
user2=User('Loai','loai17@meet.mit.edu','myhiddenpassword123')
user1.add_friend('loai17@meet.mit.edu')
whats_on_your_mind=input('whats_on_your_mind?')
user1.post(whats_on_your_mind)
user1.get_userinfo()
user1.remove_friend('loai17@meet.mit.edu')
typing=input("message-")
reply=input('ur reply-')
user1.send(typing)
user2.recieve('your friend',reply)
poster=comment('george','Gishaq@js-bethlehem.com','hey')
poster.addpost()
poster.comment('hello great post')
turtle.mainloop()
