#imported turtle moudule
import random
import turtle
#اعداد الشاشة الي بدا تطلع فيه اللعبة
wind = turtle.Screen()
#تعريف مكتبة الشاشة بمتحول اسمو wind
wind.title("ping pong by jounait")
#الاسم الي بدو يطلع على نافذة اللعبة 
wind.bgcolor('black')
#لون خلفية شاشة اللعبة
wind.setup(width=800,height=600)
#اعدادات الطول والعرض للشاشة 
wind.tracer(0)
#هي مشان نحدد تجديد الاطارات وفيا منتحكم بسرعة اللعبة 
 #انشاء مضرب اللعبة الاول
modrab_1 = turtle.Turtle()
#سرعة المضرب في التحديث  هي اسرع شيئ وهي 0 
turtle.speed(0)
#اختيار شكل المضرب 
modrab_1.shape("square")
#اختيار لون المضرب 
modrab_1.color("blue")
#نداء هذا الفنكشن هو لتجنب رسم خطوط وبقاءها على الشاشة يما انا المكتبة المستخدمة هي ترتل 
modrab_1.penup()
#تحديد مكان المضرب اقصى اليسار(-350=x,y=0)) 
modrab_1.goto(-350,0)
#حجم المضرب يكون افتراضيا بحدود 20 بكسل وسوف نقوم بزيادته
modrab_1.shapesize(stretch_wid=5,stretch_len=1)




#انشاء مضرب اللعبة الثاني 
modrab_2 = turtle.Turtle()
#سرعة المضرب في التحديث  هي اسرع شيئ وهي 0 
turtle.speed(0)
#اختيار شكل المضرب 
modrab_2.shape("square")
#اختيار لون المضرب 
modrab_2.color("red")
#نداء هذا الفنكشن هو لتجنب رسم خطوط وبقاءها على الشاشة يما انا المكتبة المستخدمة هي ترتل 
modrab_2.penup()
#تحديد مكان المضرب اقصى اليسار(350=x,y=0)) 
modrab_2.goto(350,0)
#حجم المضرب يكون افتراضيا بحدود 20 بكسل وسوف نقوم بزيادته
modrab_2.shapesize(stretch_wid=5,stretch_len=1)






# انشاء الكرة   
kora =turtle.Turtle()
#شكل الكرة
kora.shape("square")
#اختيار لون الكرة
kora.color("white")
#نداء هذا الفنكشن هو لتجنب رسم خطوط وبقاءها على الشاشة يما انا المكتبة المستخدمة هي ترتل 
kora.penup()
#تحديد مكان الكرة اقصى اليسار(0=x,y=0)) 
kora.goto(0,0)
#تحديد عامل تغيرالكرة  اي كب مرة تتغير الكرة مكانها بمقدار 2.5 وطبعا للاعلى واليمين 
kora.dx = 0.3
kora.dy = 0.3



# حساب السكور للاعبين 
scor1 = 0
scor2 = 0

scor = turtle.Turtle()
scor.speed(0)
scor.color("white")
scor.penup()
#استخدمنا هذه التعليمة لاخفاء الترتل لانو نحنا بس بتحاجة لنشوف النتيجة 
scor.hideturtle()
scor.goto(0,260)
scor.write("player (1) : 0   player (2) : 0  ", align="center", font=("Courier",24 ,"normal"))






#انشاء فانكشن لتحديد حركة اللعبة بالنسبة للمضرب الاول 
def modrab1_up():
    #لتحديد مكان المضرب بالنسبة للمححور (y)
    y = modrab_1.ycor()
    #لو حركت المضرب لفوق رح زود من قيمة ال الواي  بقيمة 20 بيكسل
    y += 60
    #نحن بحاجة لتزويد الفانكشن بمكان الواي الجديد وذلك من خلال
    modrab_1.sety(y)
def modrab1_dwon():
    #لتحديد مكان المضرب بالنسبة للمححور (y)
    y = modrab_1.ycor()
    #لو حركت المضرب لفوق رح زود من قيمة ال الواي  بقيمة 20 بيكسل
    y -= 60
    #نحن بحاجة لتزويد الفانكشن بمكان الواي الجديد وذلك من خلال
    modrab_1.sety(y)







def modrab2_up():
    #لتحديد مكان المضرب بالنسبة للمححور (y)
    y = modrab_2.ycor()
    #لو حركت المضرب لفوق رح زود من قيمة ال الواي  بقيمة 20 بيكسل
    y += 60
    #نحن بحاجة لتزويد الفانكشن بمكان الواي الجديد وذلك من خلال
    modrab_2.sety(y)
def modrab2_dwon():
    #لتحديد مكان المضرب بالنسبة للمححور (y)
    y = modrab_2.ycor()
    #لو حركت المضرب لفوق رح زود من قيمة ال الواي  بقيمة 20 بيكسل
    y -= 60
    #نحن بحاجة لتزويد الفانكشن بمكان الواي الجديد وذلك من خلال
    modrab_2.sety(y)
    


#تعريف ازار الكيبور وعملها 
wind.listen()
#رفع المضرب الاول للاعلى 
wind.onkey(modrab1_up,"w")
#تنزيل المضرب الاول للاسفل  
wind.onkey(modrab1_dwon,"s")
#تنزيل المضرب الثاني
wind.onkey(modrab2_up,"Up")
#رفع المضرب الاول
wind.onkey(modrab2_dwon,"Down")



#الحلقة التكرارية للعبة
while True:
    #في كل مرة اللعبة رح تعيد اللوب رح تعمل الشاشة update
    wind.update()
    #تحريك الكرة 
    kora.setx(kora.xcor() + kora.dx)
    kora.sety(kora.ycor() + kora.dy)
    #انشاء الحدود من الاعلى و الاسفل 
    if kora.ycor() > 290:
        kora.sety(290)
        kora.dy *= -1
    if kora.ycor() < -290:
        kora.sety(-290)
        kora.dy *= -1
    #تحديد الحدث الذي يمثل عبور الكرة من الحدول اليمين والشمال 
    if kora.xcor() > 390:
        kora.goto(0,0)
        kora.dx *= -1
        scor1 +=1
        scor.clear()
        scor.write("player (1) : {}   player (2) : {}  ".format(scor1 , scor2), align="center", font=("Courier",24 ,"normal"))


    if kora.xcor() < -390:
        kora.goto(0,0)
        kora.dx *= -1
        scor2 +=1
        scor.clear()
        scor.write("player (1) : {}   player (2) : {}  ".format(scor1 , scor2), align="center", font=("Courier",24 ,"normal"))


    # الانشاء حالة اصتطتدام المرة بالمضرب  اليمين 
    if ((kora.xcor() >340) and (kora.xcor()< 350) and kora.ycor() < (modrab_2.ycor() + 40) and (kora.ycor() > modrab_2.ycor() -40) ):
        kora.setx(340)
        kora.dx *= -1
    #حالة الاصتطدام بالمضرب اليمين
    if ((kora.xcor() < -340) and (kora.xcor() > -350) and kora.ycor() < (modrab_1.ycor() + 40) and (kora.ycor() > modrab_1.ycor() -40) ):
        kora.setx(-340)
        kora.dx *= -1
    





   









