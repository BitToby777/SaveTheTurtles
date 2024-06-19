"""
Toby Feb 27 2024
This is an adventure game that allows you to choose options for a turtle, while being coded using Turtle.
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
import time
import random

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()
t.shape('turtle')

t.color('blue')
t.write('Save the Turtles!',
        font=('Times New Roman', 40, 'bold'),
        align='center')

t.pu()
m = turtle.Turtle()
m.pu()
m.goto(500, 500)
m.shape('turtle')
x = 5
y = 5
t.goto(-200, -200)
t.pd()
t.pensize(5)
t.pencolor('gray')
t.fillcolor('#8B0000')
t.begin_fill()
t.goto(-200, -50)
t.goto(200, -50)
t.goto(200, -200)
t.goto(-200, -200)
t.end_fill()
x_list = list()
y_list = list()
t.pu()
t.goto(0, -150)
t.color('red')
t.write('Enter to Start', font=('Times New Roman', 35, 'bold'), align='center')
t.goto(0, -200)
t.write('Or S to Skip', font=('Times New Roman', 35, 'bold'), align='center')
dumb = input("")
if (dumb != "S"):

  turtle.bgcolor("#ADD8E6")
  t.clear()
  t.goto(-200, -300)
  t.begin_fill()
  t.color('green')
  t.fillcolor("#7CFC00")
  t.pd()
  t.goto(-200, 350)
  t.goto(-100, 350)
  t.goto(-100, -300)
  t.goto(-200, -300)
  t.pu()
  t.end_fill()
  t.goto(200, -300)
  t.pd()
  t.begin_fill()
  t.goto(200, 350)
  t.goto(100, 350)
  t.goto(100, -300)
  t.goto(200, -300)
  t.pu()
  t.end_fill()
  t.speed(1)
  t.goto(0, -300)
  t.goto(0, 150)
  t.color('brown')
  t.write('Sigh...', font=('Times New Roman', 35, 'bold'), align='center')
  time.sleep(3)
  t.undo()
  t.write('I dont know where my family is.',
          font=('Times New Roman', 20, 'bold'),
          align='center')
  time.sleep(5)
  t.undo()
  t.write('My Mommy is so sweet.',
          font=('Times New Roman', 25, 'bold'),
          align='center')
  time.sleep(3)
  turtle.bgcolor("Pink")
  t.clear()
  m.color('purple')
  m.goto(0, 0)
  t.write('She made the yummiest cookies. They were Turtastic!',
          font=('Times New Roman', 15, 'bold'),
          align='center')
  time.sleep(5)
  t.undo()
  m.pu()
  m.speed(1)
  m.pensize(5)
  m.goto(0, -200)
  m.color('brown')
  m.begin_fill()
  m.pd()
  m.circle(100)
  m.end_fill()
  m.color('black')
  m.pu()
  m.goto(0, -70)
  m.begin_fill()
  m.pd()
  m.circle(20)
  m.end_fill()
  m.pu()
  m.goto(50, -150)
  m.begin_fill()
  m.pd()
  m.circle(20)
  m.end_fill()
  m.pu()
  m.goto(-50, -150)
  m.begin_fill()
  m.pd()
  m.circle(20)
  m.end_fill()
  m.pu()
  m.color('purple')
  m.goto(0, 50)
  t.write('I can almost even smell them.',
          font=('Times New Roman', 20, 'bold'),
          align='center')
  time.sleep(3)
  t.undo()
  t.write('But she is gone now... :(',
          font=('Times New Roman', 30, 'bold'),
          align='center')
  m.goto(500, 50)
  time.sleep(4)
  t.undo()
  t.write('Will you help me find my family?',
          font=('Times New Roman', 20, 'bold'),
          align='center')
  time.sleep(5)
  turtle.bgcolor("#7CFC00")
  t.clear()
  m.clear()
  t.speed(0)
  t.goto(0, -500)
  t.speed(1)
  t.goto(0, 300)
t.clear()
turtle.bgcolor("green")
t.goto(0, -100)
t.pensize(20)
t.speed(5)
t.goto(-200, -100)
t.pd()
t.goto(-200, 200)
t.goto(-50, 200)
t.goto(-50, -100)
t.goto(-200, -100)
t.pu()
t.goto(200, 200)
t.pd()
t.goto(50, 200)
t.goto(50, -100)
t.goto(200, -100)
t.goto(200, 200)
t.speed(1)
t.pu()
t.goto(-120, 225)
t.pd()
t.color('red')
t.write('THE END IS NEAR',
        font=('Times New Roman', 15, 'bold'),
        align='center')
t.pu()
t.goto(130, 225)
t.pd()
t.write('STAY AWAY', font=('Times New Roman', 20, 'bold'), align='center')
t.pu()
t.goto(0, -150)
t.color('black')
t.write('What uplifting tunnels!',
        font=('Times New Roman', 30, 'bold'),
        align='center')
time.sleep(3)
t.undo()
t.write('Which tunnel should I dig through?',
        font=('Times New Roman', 20, 'bold'),
        align='center')
time.sleep(3)
t.undo()
t.pu()
t.color('orange')
t.goto(0, 100)
t.pd()
t.write('1: Tunnel 1', font=('Times New Roman', 70, 'bold'), align='center')
t.pu()
t.color('blue')
t.goto(0, -100)
t.pd()
t.write('2: Tunnel 2', font=('Times New Roman', 70, 'bold'), align='center')
t.pu()
first_choice = input()
if (first_choice == "1"):
  t.goto(-130, 100)
  t.clear()
  t.pensize(3)
  t.speed(6)
  turtle.bgcolor("gray")
  t.color('black')
  t.pd()
  t.goto(300, 250)
  t.pu()
  t.goto(200, -200)
  t.pd()
  t.goto(-50, 70)
  t.pu()
  t.goto(-330, -220)
  t.pd()
  t.goto(-250, -110)
  t.pu()
  t.goto(-70, 156)
  t.pd()
  t.goto(277, -207)
  t.pu()
  t.goto(-120, 209)
  t.pd()
  t.goto(80, -90)
  t.pu()
  t.speed(1)
  t.goto(0, -50)
  t.write('This place looks messed up.',
          font=('Times New Roman', 25, 'bold'),
          align='center')
  time.sleep(3)
  t.undo()
  t.pu()
  t.goto(-100, 100)
  t.pd()
  t.color('white')
  t.fillcolor('black')
  t.begin_fill()
  t.circle(30)
  t.end_fill()
  t.pu()
  t.goto(-100, 115)
  t.pd()
  t.write('8', font=('Times New Roman', 25, 'bold'), align='center')
  t.pu()
  t.goto(-100, 0)
  t.write('Ooh, a Magic 8 ball!',
          font=('Times New Roman', 25, 'bold'),
          align='center')
  time.sleep(3)
  t.undo()
  t.write('What should I ask it?',
          font=('Times New Roman', 25, 'bold'),
          align='center')
  time.sleep(3)
  t.undo()
  t.pu()
  t.color('orange')
  t.goto(0, 100)
  t.pd()
  t.write('1: Is my mother still alive?',
          font=('Times New Roman', 30, 'bold'),
          align='center')
  t.pu()
  t.color('blue')
  t.goto(0, -100)
  t.pd()
  t.write('2: Is a hot dog a sandwich?',
          font=('Times New Roman', 30, 'bold'),
          align='center')
  t.pu()
  second_choice = input()
  if (second_choice == "1"):
    t.fillcolor("black")
    t.speed(5)
    t.goto(0, -300)
    t.pu()
    t.begin_fill()
    t.circle(300)
    t.speed(1)
    t.end_fill()
    t.pu()
    t.goto(0, 0)
    t.color('white')
    t.write('Outlook not so good',
            font=('Times New Roman', 35, 'bold'),
            align='center')
    time.sleep(3)
    turtle.bgcolor("gray")
    t.clear()
    t.write('WAHHHHHHHHHHHH!!!',
            font=('Times New Roman', 30, 'bold'),
            align='center')
    time.sleep(3)
    t.undo()
    turtle.bgcolor("#006994")
    t.write('I cried so much that I am swimming in my own tears.',
            font=('Times New Roman', 15, 'bold'),
            align='center')
    time.sleep(3)
    t.pu()
    t.undo()
    t.pensize(7)
    t.pencolor('silver')
    t.fillcolor('#848884')
    t.begin_fill()
    t.pd()
    t.circle(50)
    t.pu()
    t.end_fill()
    t.pd()
    t.write('Q', font=('Times New Roman', 50, 'bold'), align='center')
    t.pu()
    t.goto(100, -100)
    t.write('Ooh, a shiny quarter!',
            font=('Times New Roman', 25, 'bold'),
            align='center')
    time.sleep(3)
    t.undo()
    t.write('Should I pick it up up up?',
            font=('Times New Roman', 20, 'bold'),
            align='center')
    time.sleep(3)
    t.undo()
    t.pu()
    t.color('orange')
    t.goto(0, 100)
    t.pd()
    t.write('1: Nah', font=('Times New Roman', 70, 'bold'), align='center')
    t.pu()
    t.color('#90EE90')
    t.goto(0, -100)
    t.pd()
    t.write('2: Free Money!',
            font=('Times New Roman', 50, 'bold'),
            align='center')
    t.pu()
    third_choice = input()
    t.clear()
    t.goto(0, 150)
    m.color('red')
    m.goto(0, 200)
    m.write('You shall not pass.',
            font=('Times New Roman', 25, 'bold'),
            align='center')
    time.sleep(3)
    m.undo()
    m.write(
        'Perhaps you had 25 cents, I shall let you in with open turtle arms.',
        font=('Times New Roman', 12, 'bold'),
        align='center')
    time.sleep(5)
    m.undo()
    if (third_choice == "1"):
      t.write('No, but I can get it...',
              font=('Times New Roman', 25, 'bold'),
              align='center')
      time.sleep(2)
      t.undo()
      m.write('Too late, kiss your sweet chances goodbye!',
              font=('Times New Roman', 15, 'bold'),
              align='center')
      time.sleep(2)
      m.undo()
      m.goto(500, 0)
      t.write('What a B-Head!',
              font=('Times New Roman', 40, 'bold'),
              align='center')
      time.sleep(2)
      t.undo()
      t.goto(0, 0)
      t.color('red')
      t.write('Ending 1: Wasted in the Wasteland',
              font=('Times New Roman', 22, 'bold'),
              align='center')
    else:
      t.write('I got it!!!',
              font=('Times New Roman', 30, 'bold'),
              align='center')
      time.sleep(2)
      t.undo()
      m.write('Thanks, fellow traveler!',
              font=('Times New Roman', 15, 'bold'),
              align='center')
      time.sleep(2)
      m.undo()
      m.goto(500, 0)
      turtle.bgcolor("#87CEEB")
      t.clear()
      t.color('silver')
      t.speed(5)
      t.goto(-300, -300)
      t.begin_fill()
      t.pd()
      t.goto(-300, 100)
      t.goto(-125, 100)
      t.goto(-125, -300)
      t.goto(-125, -300)
      t.pu()
      t.end_fill()
      t.goto(-100, -300)
      t.begin_fill()
      t.pd()
      t.goto(-100, 200)
      t.goto(75, 200)
      t.goto(75, -300)
      t.goto(-100, -300)
      t.pu()
      t.end_fill()
      t.goto(100, -300)
      t.begin_fill()
      t.pd()
      t.goto(100, 150)
      t.goto(300, 150)
      t.goto(300, -300)
      t.goto(100, -300)
      t.pu()
      t.end_fill()
      t.speed(1)
      t.goto(0, -100)
      t.color('yellow')
      t.write('Ooh, an epic city!',
              font=('Times New Roman', 40, 'bold'),
              align='center')
      time.sleep(3)
      t.undo()
      t.write('It is okay, dead mother, I will make you proud!',
              font=('Times New Roman', 15, 'bold'),
              align='center')
      time.sleep(5)
      t.undo()
      t.goto(0, 0)
      t.color('red')
      t.write('Ending 2: In the Never Sleeping City',
              font=('Times New Roman', 20, 'bold'),
              align='center')
  else:
    t.fillcolor("black")
    t.speed(5)
    t.goto(0, -300)
    t.pu()
    t.begin_fill()
    t.circle(300)
    t.speed(1)
    t.end_fill()
    t.pu()
    t.goto(0, 0)
    t.color('white')
    t.write('It is certain',
            font=('Times New Roman', 50, 'bold'),
            align='center')
    time.sleep(3)
    time.sleep(3)
    turtle.bgcolor("gray")
    t.clear()
    t.write('Good to know!',
            font=('Times New Roman', 50, 'bold'),
            align='center')
    time.sleep(3)
    t.undo()
    m.color('red')
    m.goto(50, 0)
    m.write('Hey, wanna have a hot dog eating contest?',
            font=('Times New Roman', 15, 'bold'),
            align='center')
    time.sleep(4)
    m.undo()
    t.write('Nah, I am good.',
            font=('Times New Roman', 30, 'bold'),
            align='center')
    time.sleep(5)
    t.undo()
    m.goto(50, 0)
    m.write('Well too bad, bucko!',
            font=('Times New Roman', 30, 'bold'),
            align='center')
    time.sleep(4)
    m.undo()
    m.pencolor('yellow')
    m.fillcolor('orange')
    m.pu()
    m.goto(-20, 50)
    m.begin_fill()
    m.pd()
    m.goto(-20, 200)
    m.goto(20, 200)
    m.goto(20, 50)
    m.goto(-20, 50)
    m.end_fill()
    m.pu()
    m.goto(30, 50)
    m.begin_fill()
    m.pd()
    m.goto(30, 200)
    m.goto(70, 200)
    m.goto(70, 50)
    m.goto(30, 50)
    m.end_fill()
    m.pu()
    m.goto(50, 0)
    m.write('Whoever eats their hot dog first gets the largest hot dog ever!',
            font=('Times New Roman', 11, 'bold'),
            align='center')
    time.sleep(5)
    m.undo()
    t.write('How am I gonna beat this dirty, hot dog eating machine?',
            font=('Times New Roman', 14, 'bold'),
            align='center')
    time.sleep(3)
    t.undo()
    t.pu()
    t.color('blue')
    t.goto(0, 100)
    t.pd()
    t.write('1: Distract him',
            font=('Times New Roman', 50, 'bold'),
            align='center')
    t.pu()
    t.color('orange')
    t.goto(0, -100)
    t.pd()
    t.write('2: Give away your hot dog',
            font=('Times New Roman', 30, 'bold'),
            align='center')
    t.pu()
    t.goto(0, 0)
    third_choice = input()
    t.clear()
    if (third_choice == "1"):
      t.write('You ate any good hot dogs recently?',
              font=('Times New Roman', 15, 'bold'),
              align='center')
      time.sleep(3)
      t.undo()
      m.write('I had a Belgian Hot Dog with Onion-',
              font=('Times New Roman', 15, 'bold'),
              align='center')
      t.color('gray')
      t.goto(-25, 45)
      t.pd()
      t.begin_fill()
      t.goto(-25, 205)
      t.goto(25, 205)
      t.goto(25, 45)
      t.goto(-25, 45)
      t.end_fill()
      t.pu()
      t.color('yellow')
      t.goto(0, 0)
      m.undo()
      m.write('Hey! Not fair!!!',
              font=('Times New Roman', 30, 'bold'),
              align='center')
      time.sleep(3)
      t.pensize(20)
      m.clear()
      m.goto(500, 200)
      t.pencolor('yellow')
      t.fillcolor('orange')
      t.pu()
      t.goto(-100, -200)
      t.begin_fill()
      t.pd()
      t.goto(-100, 200)
      t.goto(100, 200)
      t.goto(100, -200)
      t.goto(-100, -200)
      t.end_fill()
      t.pu()
      t.color('red')
      t.goto(0, 0)
      t.write('Looks so yummy!',
              font=('Times New Roman', 30, 'bold'),
              align='center')
      time.sleep(3)
      t.clear()
      t.write('AEEUHGHEHSE NO FEL GOOOOD',
              font=('Times New Roman', 25, 'bold'),
              align='center')
      time.sleep(3)
      t.clear()
      t.hideturtle()
      time.sleep(3)
      t.write('Ending 3: Too hot, dog!',
              font=('Times New Roman', 30, 'bold'),
              align='center')
    else:
      t.goto(-100, 0)
      m.goto(25, 0)
      m.write('You cant give me your hot dog! I win by default.',
              font=('Times New Roman', 14, 'bold'),
              align='center')
      time.sleep(4)
      m.undo()
      m.write('Take the L, Loser!',
              font=('Times New Roman', 30, 'bold'),
              align='center')
      time.sleep(2)
      m.clear()
      m.goto(500, 200)
      t.write('Is everyone in this world a jerk?',
              font=('Times New Roman', 15, 'bold'),
              align='center')
      time.sleep(3)
      t.color('green')
      t.clear()
      t.goto(0, 400)
      turtle.bgcolor("yellow")
      t.goto(0, -400)
      turtle.bgcolor("silver")
      t.goto(0, 0)
      m.color('gray')
      m.pensize(10)
      m.pd()
      m.goto(400, 150)
      m.goto(-400, 150)
      m.color('purple')
      m.pu()
      m.goto(0, 180)
      t.write('OMG I FOUND YOU! What happened?',
              font=('Times New Roman', 20, 'bold'),
              align='center')
      time.sleep(3)
      t.undo()
      m.write(
          'I cant believe you found me! I got locked up here by very evil turtles.',
          font=('Times New Roman', 12, 'bold'),
          align='center')
      time.sleep(5)
      m.undo()
      t.write('They are so evil. I can get you out with...',
              font=('Times New Roman', 20, 'bold'),
              align='center')
      time.sleep(4)
      t.undo()
      t.color('orange')
      t.goto(0, 100)
      t.pd()
      t.write('1: Metal cutters',
              font=('Times New Roman', 50, 'bold'),
              align='center')
      t.pu()
      t.color('blue')
      t.goto(0, -100)
      t.pd()
      t.write('2: The Force',
              font=('Times New Roman', 50, 'bold'),
              align='center')
      t.pu()
      t.goto(0, 0)
      fourth_choice = input()
      t.clear()
      if (fourth_choice == "1"):
        t.pensize(15)
        t.goto(0, -300)
        t.pd()
        t.color('gray')
        t.goto(0, 150)
        t.pu()
        t.clear()
        m.clear()
        m.write('Thank you so much sweetheart!',
                font=('Times New Roman', 20, 'bold'),
                align='center')
        time.sleep(3)
        m.undo()
        t.goto(-100, 0)
        m.goto(100, 0)
        t.write('I am so glad I found you!',
                font=('Times New Roman', 25, 'bold'),
                align='center')
        time.sleep(3)
        t.undo()
        m.write('Me toooooo!',
                font=('Times New Roman', 40, 'bold'),
                align='center')
        time.sleep(3)
        m.undo()
        m.write('Wanna shell hug???',
                font=('Times New Roman', 30, 'bold'),
                align='center')
        time.sleep(3)
        m.undo()
        t.write('Of course! :)',
                font=('Times New Roman', 40, 'bold'),
                align='center')
        time.sleep(3)
        t.undo()
        t.goto(-5, 0)
        m.goto(5, 0)
        time.sleep(3)
        t.write('Ending 4: Broken Walls fix Hearts',
                font=('Times New Roman', 25, 'bold'),
                align='center')
      else:
        t.write('GIMME THE FORCE!!!!!',
                font=('Times New Roman', 30, 'bold'),
                align='center')
        time.sleep(3)
        t.undo()
        t.turtlesize(20)
        t.goto(0, 300)
        m.clear()
        m.hideturtle()
        t.goto(0, 0)
        t.turtlesize(1)
        t.write('The jail cell is gone!!!',
                font=('Times New Roman', 30, 'bold'),
                align='center')
        time.sleep(3)
        t.undo()
        t.write('But... my... mommy... is... dead...',
                font=('Times New Roman', 20, 'bold'),
                align='center')
        time.sleep(3)
        t.undo()
        t.write(
            'WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
            font=('Times New Roman', 10, 'bold'),
            align='center')
        time.sleep(5)
        t.undo()
        t.color('red')
        t.write('Ending 5: Friendly Fire Enabled',
                font=('Times New Roman', 30, 'bold'),
                align='center')
else:
  t.undo()
  t.pu()
  t.goto(130, 100)
  turtle.bgcolor("red")
  t.clear()
  t.goto(0, -150)
  m.color('orange')
  m.speed(1)
  m.turtlesize(2)
  m.goto(0, 100)
  m.write('No turtles shall enter...',
          font=('Times New Roman', 20, 'bold'),
          align='center')
  time.sleep(3)
  m.undo()
  t.write('Uhh... sorry?',
          font=('Times New Roman', 40, 'bold'),
          align='center')
  time.sleep(2)
  t.undo()
  m.write('Too late. We will compete in a...',
          font=('Times New Roman', 20, 'bold'),
          align='center')
  time.sleep(4)
  m.undo()
  m.write('Dice rolling contest! The weakling goes first.',
          font=('Times New Roman', 15, 'bold'),
          align='center')
  time.sleep(3)
  m.undo()
  t.write('Hey!', font=('Times New Roman', 60, 'bold'), align='center')
  time.sleep(2)
  t.undo()
  t.write('Enter to Roll',
          font=('Times New Roman', 40, 'bold'),
          align='center')
  time.sleep(2)
  t.undo()
  go = input("")
  roll1 = random.randint(1, 6)
  t.write(roll1, font=('Times New Roman', 40, 'bold'), align='center')
  time.sleep(2)
  roll2 = random.randint(1, 6)
  m.write(roll2, font=('Times New Roman', 40, 'bold'), align='center')
  time.sleep(2)
  t.clear()
  m.clear()
  if (roll2 > roll1):
    m.write('Haha, I won! Time to die. >:)',
            font=('Times New Roman', 20, 'bold'),
            align='center')
    time.sleep(3)
    m.undo()
    m.goto(0, -150)
    t.hideturtle()
    m.hideturtle()
    time.sleep(3)
    t.color('blue')
    t.goto(0, 0)
    t.write('Ending 6: Snake Eyes',
            font=('Times New Roman', 40, 'bold'),
            align='center')
    time.sleep(100)
    exit()
  if (roll1 == roll2):
    m.write('A tie???', font=('Times New Roman', 50, 'bold'), align='center')
    time.sleep(3)
    m.undo()
    m.write('You win if you can answer...',
            font=('Times New Roman', 25, 'bold'),
            align='center')
    time.sleep(3)
    m.undo()
    question = random.randint(1, 3)
    if (question == 1):
      quest = "What year was America born?"
    elif (question == 2):
      quest = "What is 11/16 in decimal format?"
    else:
      quest = "How many Harry Potter books are there?"
    m.write(quest, font=('Times New Roman', 20, 'bold'), align='center')
    answer = input("")
    m.clear()
    if (answer == "1776" or (answer == "0.6875") or (answer == "7")):
      pass
    else:
      m.write('WRONG! Time to die. >:)',
              font=('Times New Roman', 25, 'bold'),
              align='center')
      time.sleep(3)
      m.undo()
      m.goto(0, -150)
      t.hideturtle()
      m.hideturtle()
      time.sleep(3)
      t.color('blue')
      t.goto(0, 0)
      t.write('Ending 7: NOT Smarter than a Fifth Turtle',
              font=('Times New Roman', 20, 'bold'),
              align='center')
      time.sleep(100)
      exit()
  m.write('How did you win? Whaaaa',
          font=('Times New Roman', 30, 'bold'),
          align='center')
  time.sleep(3)
  t.pensize(5)
  m.undo()
  m.goto(500, 200)
  t.goto(0, 400)
  turtle.bgcolor("#7CFC00")
  t.goto(0, 100)
  t.pencolor('purple')
  t.fillcolor('blue')
  t.begin_fill()
  t.pd()
  t.circle(30)
  t.end_fill()
  t.pu()
  t.goto(0, 0)
  t.write('Ooh, a time machine! Should I use it?',
          font=('Times New Roman', 20, 'bold'),
          align='center')
  time.sleep(3)
  t.undo()
  t.color('orange')
  t.goto(0, 100)
  t.pd()
  t.write('1: Let er rip!',
          font=('Times New Roman', 50, 'bold'),
          align='center')
  t.pu()
  t.color('blue')
  t.goto(0, -100)
  t.pd()
  t.write('2: Stay Away!',
          font=('Times New Roman', 50, 'bold'),
          align='center')
  t.pu()
  t.goto(0, 0)
  second_choice = input()
  if (second_choice == "1"):
    t.goto(0, 100)
    time.sleep(3)
    turtle.bgcolor("Pink")
    t.clear()
    m.turtlesize(1)
    m.color('purple')
    m.goto(0, 0)
    t.write('She made the yummiest cookies. They were Turtastic!',
            font=('Times New Roman', 15, 'bold'),
            align='center')
    time.sleep(5)
    t.undo()
    m.pu()
    m.speed(1)
    m.pensize(5)
    m.goto(-100, -200)
    m.color('red')
    m.pd()
    m.goto(-100, -50)
    m.goto(-25, -200)
    m.goto(-25, -50)
    m.pu()
    m.goto(75, -200)
    m.pd()
    m.circle(75)
    m.pu()
    m.goto(0, 0)
    time.sleep(3)
    t.write('W... Wha... is happening???',
            font=('Times New Roman', 20, 'bold'),
            align='center')
    time.sleep(3)
    t.undo()
    t.color('orange')
    t.goto(0, 100)
    t.pd()
    t.write('1: She just wrote a love note!',
            font=('Times New Roman', 20, 'bold'),
            align='center')
    t.pu()
    t.color('blue')
    t.goto(0, -100)
    t.pd()
    t.write('2: Momma Abandon Me',
            font=('Times New Roman', 30, 'bold'),
            align='center')
    t.pu()
    t.goto(0, 100)
    m.clear()
    third_choice = input()
    t.clear()
    if (third_choice == "1"):
      m.write('You liar!',
              font=('Times New Roman', 60, 'bold'),
              align='center')
      time.sleep(3)
      m.undo()
      m.goto(0, -200)
      t.goto(0, 0)
      m.write('Feel the wrath of...',
              font=('Times New Roman', 30, 'bold'),
              align='center')
      time.sleep(3)
      m.undo()
      m.turtlesize(2)
      m.write('Wonder Turtle!!!',
              font=('Times New Roman', 40, 'bold'),
              align='center')
      time.sleep(3)
      m.undo()
      m.speed(1)
      m.goto(0, 0)
      t.speed(2)
      t.goto(0, 500)
      time.sleep(3)
      m.color('red')
      m.write('Ending 8: Pinocchio has his nose ripped off',
              font=('Times New Roman', 20, 'bold'),
              align='center')
    else:
      m.color('purple')
      m.write('Yes I left you.',
              font=('Times New Roman', 40, 'bold'),
              align='center')
      time.sleep(3)
      m.undo()
      t.write('But whyyyyyy?',
              font=('Times New Roman', 40, 'bold'),
              align='center')
      time.sleep(3)
      t.undo()
      m.write('You stole my time machine!',
              font=('Times New Roman', 30, 'bold'),
              align='center')
      time.sleep(3)
      m.undo()
      t.write('I never', font=('Times New Roman', 50, 'bold'), align='center')
      time.sleep(1)
      t.undo()
      t.write('Oh, I did.',
              font=('Times New Roman', 40, 'bold'),
              align='center')
      time.sleep(3)
      t.undo()
      m.write(
          'You also did tax evasion, mass murder, and destroyed a Pigeon Poop Shooting Range.',
          font=('Times New Roman', 8, 'bold'),
          align='center')
      time.sleep(6)
      m.undo()
      t.write('You gotta admit, the 360 before I got em was dope!',
              font=('Times New Roman', 14, 'bold'),
              align='center')
      time.sleep(4)
      t.undo()
      m.write('Person who is playing this game:',
              font=('Times New Roman', 20, 'bold'),
              align='center')
      time.sleep(3)
      m.undo()
      m.write('Why are you following a criminal?',
              font=('Times New Roman', 20, 'bold'),
              align='center')
      time.sleep(3)
      m.undo()
      m.write('You wont help him anymore, right?',
              font=('Times New Roman', 20, 'bold'),
              align='center')
      time.sleep(3)
      m.undo()
      l = turtle.Turtle()
      l.pu()
      l.turtlesize(2)
      l.shape('turtle')
      l.goto(250, 100)
      l.speed(1)
      m.write('Take em away!',
              font=('Times New Roman', 50, 'bold'),
              align='center')
      time.sleep(2)
      m.hideturtle()
      m.clear()
      t.write('NOOOOO', font=('Times New Roman', 50, 'bold'), align='center')
      l.goto(0, 100)
      time.sleep(3)
      t.clear()
      turtle.bgcolor("gray")
      l.pensize(20)
      t.goto(0, 200)
      l.goto(500, 150)
      l.color('silver')
      l.pd()
      l.goto(-500, 150)
      l.pu()
      l.goto(0, 0)
      l.color('black')
      l.write('And you will stay there!',
              font=('Times New Roman', 25, 'bold'),
              align='center')
      time.sleep(4)
      l.undo()
      l.goto(0, -500)
      t.write('So... um...',
              font=('Times New Roman', 40, 'bold'),
              align='center')
      time.sleep(2)
      t.undo()
      t.write('Nevermind',
              font=('Times New Roman', 40, 'bold'),
              align='center')
      time.sleep(2)
      t.undo()
      time.sleep(3)
      m.color('orange')
      m.goto(0, 150)
      m.pd()
      m.write('1: ...', font=('Times New Roman', 100, 'bold'), align='center')
      m.pu()
      m.color('blue')
      m.goto(0, 0)
      m.pd()
      m.write('2: Help him!',
              font=('Times New Roman', 50, 'bold'),
              align='center')
      m.pu()
      m.color('red')
      m.goto(0, -150)
      m.pd()
      m.write('3: BURN WITH FIRE',
              font=('Times New Roman', 40, 'bold'),
              align='center')
      m.pu()
      m.goto(0, 0)
      third_choice = input()
      m.clear()
      if (third_choice == "1"):
        time.sleep(10)
        m.color('red')
        m.write('Ending 16: Nothing',
                font=('Times New Roman', 40, 'bold'),
                align='center')
      elif (third_choice == "2"):
        l.clear()
        time.sleep(3)
        t.write('TYSM!!!',
                font=('Times New Roman', 50, 'bold'),
                align='center')
        time.sleep(3)
        t.undo()
        t.write('Ur da best!!! :)',
                font=('Times New Roman', 30, 'bold'),
                align='center')
        time.sleep(4)
        t.undo()
        t.goto(0, -500)
        turtle.bgcolor("#7CFC00")
        t.goto(0, 0)
        t.goto(-50, 100)
        t.pd()
        t.fillcolor('silver')
        t.pencolor('gray')
        t.pensize(3)
        t.begin_fill()
        t.goto(50, 100)
        t.goto(50, 200)
        t.goto(-50, 200)
        t.goto(-50, 100)
        t.end_fill()
        t.pu()
        t.goto(0, 130)
        t.color('green')
        t.write('$', font=('Times New Roman', 70, 'bold'), align='center')
        t.goto(0, 0)
        t.write('So, how shall we rob the bank?',
                font=('Times New Roman', 20, 'bold'),
                align='center')
        time.sleep(3)
        t.undo()
        t.color('red')
        t.goto(0, 100)
        t.pd()
        t.write('1: Ending 9',
                font=('Times New Roman', 40, 'bold'),
                align='center')
        t.pu()
        t.goto(0, -100)
        t.pd()
        t.write('2: TTA6 (Turtle Theft Auto 6)',
                font=('Times New Roman', 20, 'bold'),
                align='center')
        t.goto(0, 0)
      else:
        m.pd()
        m.color('orange')
        m.pensize(50)
        m.speed(5)
        m.goto(500, 0)
        m.goto(-300, 100)
        m.goto(200, -500)
        m.goto(400, -400)
        m.goto(-300, 0)
        m.goto(200, 200)
        m.goto(100, -400)
        m.goto(-500, 500)
        m.goto(200, 100)
        m.goto(0, 0)
        turtle.bgcolor("black")
        t.hideturtle()
        m.clear()
        l.clear()
        time.sleep(3)
        yvalue = 300
        m.color('red')
        m.pu()
        while True:
          if (yvalue == -350):
            break
          m.goto(0, yvalue)
          m.write('Ending 10: This girl is on FIRE',
                  font=('Times New Roman', 25, 'bold'),
                  align='center')
          yvalue = yvalue - 50
  else:
    t.clear()
    t.goto(0, -500)
    t.goto(0, 0)

    def draw_square(length, center_x, center_y):
      t.pu()
      t.begin_fill()
      t.goto(center_x, center_y)
      t.pd()
      t.goto(center_x, center_y + length)
      t.goto(center_x + length, center_y + length)
      t.goto(center_x + length, center_y)
      t.goto(center_x, center_y)
      t.end_fill()
      t.pu()

    t.width(5)
    t.pencolor('black')
    t.fillcolor('red')
    draw_square(100, -150, 150)
    t.pencolor('purple')
    t.fillcolor('orange')
    draw_square(100, 150, 150)
    t.pencolor('orange')
    t.fillcolor('yellow')
    draw_square(100, 0, 0)
    t.pencolor('black')
    t.fillcolor('green')
    draw_square(100, -150, -150)
    t.pencolor('blue')
    t.fillcolor('#ADD8E6')
    draw_square(100, 150, -150)
    t.color('black')
    t.goto(-100, 150)
    t.write('1', font=('Times New Roman', 50, 'bold'), align='center')
    t.goto(200, 150)
    t.write('2', font=('Times New Roman', 50, 'bold'), align='center')
    t.goto(50, 0)
    t.write('3', font=('Times New Roman', 50, 'bold'), align='center')
    t.goto(-100, -150)
    t.write('4', font=('Times New Roman', 50, 'bold'), align='center')
    t.goto(200, -150)
    t.write('5', font=('Times New Roman', 50, 'bold'), align='center')
    t.goto(50, -200)
    t.color('black')
    t.write('Type the number of what biome you want me to go to!',
            font=('Times New Roman', 15, 'bold'),
            align='center')
    time.sleep(3)
    t.undo()
    choice_two = input("")
    if (choice_two == '1'):
      t.goto(-150, 150)
      t.clear()
      turtle.bgcolor("red")
      t.write('AAH! THIS LAVA IS SO HOT!',
              font=('Times New Roman', 25, 'bold'),
              align='center')
      time.sleep(3)
      t.undo()
      time.sleep(2)
      t.hideturtle()
      time.sleep(3)
      t.goto(0, 0)
      t.write('Ending 11: Who let him cook?',
              font=('Times New Roman', 25, 'bold'),
              align='center')
    elif (choice_two == '2'):
      t.goto(150, 150)
      t.clear()
      turtle.bgcolor("orange")
      m.turtlesize(15)
      m.speed(0)
      m.showturtle()
      m.goto(-150, 0)
      a = turtle.Turtle()
      a.pu()
      a.turtlesize(15)
      a.shape('turtle')
      a.goto(0, 150)
      b = turtle.Turtle()
      b.pu()
      b.turtlesize(15)
      b.shape('turtle')
      b.goto(150, 0)
      c = turtle.Turtle()
      c.pu()
      c.turtlesize(15)
      c.shape('turtle')
      c.goto(0, -150)
      t.goto(0, 0)
      t.write('What???', font=('Times New Roman', 25, 'bold'), align='center')
      time.sleep(3)
      t.undo()
      time.sleep(3)
      t.turtlesize(15)
      t.pencolor('red')
      t.write('Ending 12: OooNNnnEEee oOff UUsss',
              font=('Times New Roman', 25, 'bold'),
              align='center')
      time.sleep(5)
      c.hideturtle()
      m.hideturtle()
      a.hideturtle()
      b.hideturtle()
      t.hideturtle()
    elif (choice_two == '3'):
      t.goto(0, 0)
      t.clear()
      turtle.bgcolor("yellow")
      t.write('What happened to all the waa waa?',
              font=('Times New Roman', 25, 'bold'),
              align='center')
      time.sleep(3)
      t.undo()
      time.sleep(2)
      t.hideturtle()
      time.sleep(3)
      t.goto(0, 0)
      t.write('Ending 13: Drier than a Popeyes Biscuit',
              font=('Times New Roman', 25, 'bold'),
              align='center')
    elif (choice_two == '4'):
      t.goto(-150, -150)
      t.clear()
      turtle.bgcolor("green")
      t.write('Ooh, a forest!',
              font=('Times New Roman', 25, 'bold'),
              align='center')
      time.sleep(3)
      t.undo()
      t.goto(0, 0)
      t.write('Lets party!!!',
              font=('Times New Roman', 50, 'bold'),
              align='center')
      time.sleep(3)
      t.undo()
      t.color('black')
      t.write('ENDING 14: LIFE OF THE PARTY',
              font=('Times New Roman', 30, 'bold'),
              align='center')
      while True:
        turtle.bgcolor("red")
        turtle.bgcolor("orange")
        turtle.bgcolor("yellow")
        turtle.bgcolor("green")
        turtle.bgcolor("blue")
        turtle.bgcolor("purple")
    else:
      t.goto(150, -150)
      t.clear()
      turtle.bgcolor("blue")
      t.write('I cant swim 5000 feet deep!',
              font=('Times New Roman', 20, 'bold'),
              align='center')
      time.sleep(3)
      t.undo()
      time.sleep(2)
      t.hideturtle()
      time.sleep(3)
      t.goto(0, 0)
      t.color('red')
      t.write('Ending 15: Nightmare at -5000 feet',
              font=('Times New Roman', 25, 'bold'),
              align='center')

turtle.mainloop()
