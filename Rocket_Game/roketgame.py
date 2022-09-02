
import turtle
import random
import time

speed = 0.005

turtle.register_shape("fuzes45.gif")    #|
turtle.register_shape("fuzef45.gif")    #|        
turtle.register_shape("fuze0.gif")      #|
turtle.register_shape("roketatar.gif")  #|  Burada resimleri Modüle kayıt ediyoruz.
turtle.register_shape("radar.gif")      #|
turtle.register_shape("nısangah.gif")   #|
turtle.register_shape("dusman.gif")     #|
turtle.register_shape("arkaplan2.gif")  #|

# Pencere

pencere = turtle.Screen()
pencere.title("Roket Oyunu")
pencere.bgpic("arkaplan2.gif")
pencere.setup(width=700,height=700)
pencere.tracer(0)

# Roketatar
  
roketatar = turtle.Turtle()
roketatar.shape("roketatar.gif")
roketatar.speed(0)
roketatar.penup()
roketatar.color("blue")
roketatar.goto(-280,-200)
roketatar.direction = "stop"
rx = roketatar.xcor() # roketatar x kordinat
ry = roketatar.ycor() # roketatar y kordinat

# Roket

roket =turtle.Turtle()
roket.shape("fuzes45.gif")
roket.speed(0)
roket.penup()
roket.goto(rx,ry)
roket.hideturtle()
roket.direction = "stop"

# Düşman uçaklar

dusman = turtle.Turtle()
dusman.shape("dusman.gif")
dusman.speed(0)
dusman.penup()
dusman.color("black")
ix = list(range(100, 350, 10)) 
iy = list(range(-90, 130, 10)) 
dusman.goto(random.choice(ix),random.choice(iy)) # başlangıçta rastgele belirli bir bölgeye uçak gönderiyor.

# Radar

radar = turtle.Turtle()
radar.shape("radar.gif")
radar.speed(0)
radar.penup()
radar.goto(-150,-190)
radar.direction = "stop"

# Nişangah

nısangah = turtle.Turtle()
nısangah.shape("nısangah.gif")
nısangah.speed(0)
nısangah.penup()
nısangah.direction = "stop"
nısangah.hideturtle()

# Ekrandaki yazılar

yaz = turtle.Turtle()
yaz.hideturtle()
yaz.color("black")
yaz.speed(0)
yaz.penup()
yaz.goto(-130,325)
yaz.write(f'Yeni duşman bulundu, kordinatları bulmak için -R-',align="center",font=("courier",10, 'normal'))

dkor = turtle.Turtle()
dkor.hideturtle()
dkor.color("black")
dkor.speed(0)
dkor.penup()
dkor.goto(-130,310)

dusmansayı = turtle.Turtle()
dusmansayı.hideturtle()
dusmansayı.color("black")
dusmansayı.speed(0)
dusmansayı.penup()
dusmansayı.goto(225,325)
ds = random.randint(8,13)
puan = 0
dusmansayı.write(f'Bölgedeki düşman sayısı: {puan}/{ds}',align="center",font=("courier",10, 'normal'))

kilitlen = turtle.Turtle()
kilitlen.hideturtle()
kilitlen.color("black")
kilitlen.speed(0)
kilitlen.penup()
kilitlen.goto(-130,295)

win = turtle.Turtle()
win.hideturtle()
win.color("black")
win.speed(0)
win.penup()
win.goto(0,100)

# Roketin hareket algoritması

def move():
    if roket.direction == "right":
        x = roket.xcor()
        roket.setx(x+5)
    if roket.direction == "up":
        x= roket.xcor()
        y= roket.ycor()
        roket.setx(x+5)
        roket.sety(y+5)
    if roket.direction == "down":
        x = roket.xcor()
        y= roket.ycor()
        roket.setx(x+5)
        roket.sety(y-5)

# Radar Düşman uçakalrı kordinatları bulması için;

def bulucu():
    dy = dusman.ycor()
    dx = dusman.xcor()
    nısangah.goto(dx,dy)
    nısangah.showturtle()
    yaz.clear()
    dkor.clear()
    yaz.write(f'Yeni duşman bulundu, kordinatları bulmak için -R-',align="center",font=("courier",10, 'normal'))
    dkor.write(f'\n---dusman kordinatları ==> ({dx},{dy})',align="center",font=("courier",10, 'normal'))
    kilitlen.write('Düşmana kilitlenildi ateşleme için -A-',align="center",font=("courier",10, 'normal'))

# Roketin hareket algoritması

def missile():
    dx = dusman.xcor()
    if nısangah.xcor() == dx :
        if roket.ycor() < dusman.ycor():
            roket.showturtle()
            roket.direction = "up"
            roket.shape("fuzes45.gif")
        else:
            roket.showturtle()
            roket.direction = "down"
            roket.shape("fuzef45.gif")


# Klavyeyi dinlememizi sağlayan method

pencere.listen()
pencere.onkey(missile,"a")
pencere.onkey(bulucu,"r")

while True:
    pencere.update()    
    move()
    dy = dusman.ycor()
    if roket.ycor() == dy:
        roket.shape("fuze0.gif")
        roket.direction = "right"

    # Roketle düşmanın karşılaşma algoritması 

    if roket.distance(dusman) < 20:
        roket.hideturtle()
        nısangah.hideturtle()
        dkor.clear()
        kilitlen.clear()
        puan = puan + 1
        dusmansayı.clear()
        dusmansayı.write(f'Bölgedeki düşman sayısı: {puan}/{ds}',align="center",font=("courier",10, 'normal'))
        ix = range(100, 330, 10)
        iy =range(-90, 130, 10)   
        dusman.goto(random.choice(ix),random.choice(iy))
        dy = dusman.ycor()
        roket.goto(rx,ry) 
        roket.direction = "stop"  

    if puan == ds :
        win.write(f'            DÜŞMANLAR YOK EDİLDİ \n Bu yazılım 3 saniye içinde kendini imha edecek',align="center",font=("courier",15, 'normal'))
        time.sleep(3) 
        break   
    time.sleep(speed)
   
    