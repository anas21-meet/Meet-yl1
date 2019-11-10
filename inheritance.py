from turtle import *
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
		current_x=xcor()
		new_x=current_x+dx
		current_y=ycor()
		new_y=current_y+dy
		right_side_ball=new_x+r
		left_side_ball=new_x-r
		top_side_ball=new_y+r
		bottom_side_ball=new_y-r
		x=(right_side_ball,left_side_ball)
		y=(top_side_ball,bottom_side_ball)
		self.goto(x,y)
		if xcor() > screen_width:
			self.goto(current_x)


ball=Ball(5,'blue','2','3','circle')
print(ball)







