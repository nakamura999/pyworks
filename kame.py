# ドラゴンボール風白黒絵画

# 読み込み
# python
# import turtle
# borl = turtle.Turtle()
# 打っても打たなくても良いコード　borl.shape('turtle')   種類turtle,arrow,circle,square
# import kame
# kame.kame_control(borl)

def kame_control(kame):
	for i in range(5):
		kame.forward(150)
		kame.left(144)
	kame.penup()
	kame.goto(-150,-100)
	kame.left(40)
	kame.pendown()
	for i in range(5):
		kame.forward(100)
		kame.left(144)
	kame.penup()
	kame.home()
	kame.goto(-170,150)
	kame.left(150)
	kame.pendown()
	for i in range(5):
		kame.forward(70)
		kame.left(144)
	kame.penup()
	kame.home()
	kame.forward(300)
	kame.left(90)
	kame.pendown()
	kame.circle(300)
	kame.left(90)
	kame.penup()
	kame.forward(300)
	kame.pendown()
