from turtle import*
import turtle
turtle.bgcolor('yellow')
class Ball(Turtle):
	def __init__(self,r,color,dx,dy,shape):
		Turtle.__init__(self)
		self.r=r/10
		self.color(color)
		self.dx=dx
		self.dy=dy
		self.penup()
		self.shape('circle')
	def move(self,screen_width,screen_height):
		self.screen_width=screen_width
		self.screen_height=screen_height
		current_x=xcor()
		new_x=current_x+self.dx
		current_y=ycor()
		new_y=current_y+self.dy
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		top_side_ball=new_y+self.r
		bottom_side_ball=new_y-self.r
		x=(right_side_ball,left_side_ball)
		y=(top_side_ball,bottom_side_ball)
		self.goto(new_x,new_y)
		if right_side_ball >= self.screen_width:
			self.goto(current_x,current_y)
		if top_side_ball  >= self.screen_height:
			self.goto(new_x,new_y)
		if left_side_ball<=self.screen_width:
			self.goto(new_x,new_y)
		if bottom_side_ball<=self.screen_height:
			self.goto(new_x,new_y)
turtle.ht()
screen_width=turtle.getcanvas().winfo_width()/2
screen_height=turtle.getcanvas().winfo_height()/2
ball=Ball(400,'blue',400,300,'circle')
print(ball)
while 2==2:
	ball.move(screen_width,screen_height)







