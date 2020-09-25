#1
'''  
print("환영합니다.")
print("파이썬의 세계에 오신 것을 환영합니다.")
print("파이썬은 강력합니다.")
'''
#2
'''
답:
1. 반갑습니다. 파이썬
2. 0.6
3. Hello world !!!
'''
'''
print("반갑습니다. 파이썬")
print(2*3/10)
print("Hello", "world", "!!!")
'''
#3
'''
hour = 24
week = 7
print("한 주는 총",str(hour*week)+"시간 입니다.")
'''

#4
'''
import turtle
turtle.Turtle()
turtle.shape("turtle")

turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)

turtle.done()
'''
#5
'''
import turtle
turtle.Turtle()
turtle.shape("turtle")

turtle.width(10)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)


turtle.done()
'''

#6
'''
import turtle
turtle.Turtle()
turtle.shape("turtle")

turtle.color("blue")
turtle.forward(100)

turtle.done()
'''

#7
'''
import turtle
turtle.Turtle()
turtle.shape("square")
turtle.forward(100)

turtle.done()
'''

#8
'''
import turtle
turtle.Turtle()
turtle.shape("turtle")

turtle.forward(100)
turtle.up()
turtle.goto(0,100)
turtle.down()
turtle.forward(100)

turtle.done()
'''

#9
'''
import turtle
turtle.Turtle()
turtle.shape("turtle")

turtle.circle(100)
turtle.up()
turtle.forward(180)
turtle.down()
turtle.circle(100)
turtle.up()
turtle.forward(180)
turtle.down()
turtle.circle(100)
turtle.up()
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(90)
turtle.right(180)
turtle.down()
turtle.circle(100)
turtle.up()
turtle.right(180)
turtle.forward(160)
turtle.right(180)
turtle.down()
turtle.circle(100)
turtle.done()
'''

#10
'''
name=input("이름을 입력하시오 : ")
age=int(input("나이를 입력하시오 : "))
year=int(input("지금 연도는? "))

print(name,"씨는",year+(100-age),"년에","100살이시네요")
'''

#11
'''
firstnum=int(input("첫 번째 숫자를 입력하시오 : "))
secondnum=int(input("두 번째 숫자를 입력하시오 : "))
thirdnum=int(input("세 번째 숫자를 입력하시오 : "))

print(firstnum,secondnum,thirdnum,"의 평균은 ",(firstnum+secondnum+thirdnum)/3,"입니다")
'''

#12
'''
radius=int(input("반지름을 입력하시오 : "))
print("반지름이",radius,"인 원의 넓이 =",3.14*(radius)**2)
'''

#13
'''
radiu=int(input("반지름을 입력하시오: "))
import turtle
turtle.Turtle()
turtle.shape("turtle")
turtle.circle(radiu)
turtle.up()
turtle.goto(100,0)
turtle.down()
turtle.circle(radiu+20)
turtle.up()
turtle.goto(200,0)
turtle.down()
turtle.circle(radiu+20*2)  

turtle.done()
'''

#14 #15
'''
side=int(input("한 변의 길이: "))
import turtle
turtle.Turtle()
turtle.shape("turtle")

for _ in range(3):
    turtle.forward(side)
    turtle.left(90+30)

turtle.done()
'''

#16
'''
side=int(100)
angle=int(90)

import turtle
turtle.Turtle()
turtle.shape("turtle")

for _ in range(4):
    turtle.forward(side)
    turtle.left(angle)

turtle.right(angle)
for _ in range(3):
    turtle.forward(side)
    turtle.left(angle)

turtle.right(angle*2)
for _ in range(3):
    turtle.forward(side)
    turtle.left(angle)

turtle.up()
turtle.forward(side)
turtle.down()
for _ in range(3):
    turtle.forward(side)
    turtle.left(angle)
turtle.up()
turtle.forward(side)
turtle.right(angle)
turtle.done()
'''

#17
'''
378-09=int(input("x : "))
y=int(input("y : "))
print("두 수의 합 :",x+y)
print("두 수의 차 :",x-y)
print("두 수의 곱 :",x*y)
print("두 수의 평균 :",(x+y)/2)
print("큰 수 :",max(x,y))
print("큰 수 :",min(x,y))
'''

#18
'''
r=int(input("r : "))
h=int(input("h : "))
print("원기둥의 부피 :",float(3.14*(r**2)*h))
'''

#19
'''
num=int(input("정수를 입력하시오 : "))   #1234

result=0
for i in range(2,-1,-1):
    result += num // 10**(i+1)
    num = num % 10**(i+1)
result += num / 1
print("자리 수의 합: ", int(result))
'''




#20
'''
x1=int(input("x1 : "))
y1=int(input("y1 : "))
x2=int(input("x2 : "))
y2=int(input("y2 : "))
print("두점 사이의 거리 =",((x1-x2)**2+(y1-y2)**2)**(1/2))
'''

#21
'''
import turtle
turtle.Turtle()
turtle.shape("turtle")

turtle.goto(100,0)
turtle.goto(100,100)
turtle.right(90+45)
turtle.forward(141.4213562373095)

turtle.done()
'''

#22
'''
import turtle

turtle.Turtle()
turtle.shape("turtle")

x1=int(input("x1 : "))
x2=int(input("x2 : "))
y1=int(input("y1 : "))
y2=int(input("y2 : "))

distance == (((x1-x2)**2+(y1-y2)**2)**(1/2))
turtle.up()
turtle.goto(x1,y1)
turtle.down()
turtle.goto(y1,y2)
turtle.write("점 사이의 길이 = ",distance)


turtle.done()
'''

#23
'''
print(time())
'''
#24
'''
m=int(input("물체의 무게를 입력하시오 (킬로그램) : "))
v=int(input("물체의 속도를 입력하시오 (미터/초) : "))

energy = (1/2)*m*v**2

print("물체는",energy,"(줄)의 에너지를 가지고 있다.")

'''
#25
'''
print('나는',12,'개의 사과를 먹었다.')
'''
#26
'''
print('apple'+'grape')
print('apple'*3)
'''

#27
'''
sentence=input("문자열을 입력하시오: ")
print(sentence[0:2]+sentence[-2:])
'''

#28
'''
sentence=input("문자열을 입력하시오: ")
print(str(sentence)+"하는중")
'''

#29
'''
기호=input("기호를 입력하시오: ")
문자열=input("중간에 삽입할 문자열을 입력하시오 : ")
print(기호[0]+문자열+기호[-1])
'''

#30
'''
a=int(input("첫번째 숫자: "))
b=int(input("두번째 숫자: "))
c=int(input("세번째 숫자: "))
d=int(input("네번째 숫자: "))

list=[a,b,c,d]
print("리스트 숫자들의 합 = ",list[0]+list[1]+list[2]+list[3])
'''
#31
'''
import turtle
turtle.Turtle()
turtle.shape("turtle")

color1=input("색상 #1을 입력하시오 : ")
color2=input("색상 #2을 입력하시오 : ")
color3=input("색상 #3을 입력하시오 : ")

turtle.fillcolor(color1)
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.up()
turtle.forward(100)
turtle.down()
turtle.fillcolor(color2)
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.up()
turtle.forward(100)
turtle.down()
turtle.fillcolor(color3)
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.done()
'''

#32
'''
x1=int(input("x1 :"))
y1=int(input("y1 :"))
x2=int(input("x2 :"))
y2=int(input("y2 :"))
x3=int(input("x3 :"))
y3=int(input("y3 :"))

import turtle
turtle.Turtle()
turtle.shape("turtle")
turtle.up()
turtle.goto(x1,y1)
turtle.down()
turtle.goto(x2,y2)
turtle.goto(x3,y3)

turtle.done()
'''
#33
'''
age= 20
if age < 20:
    print("20살 미만")
else:
    print("20살 이상")
'''

#34
'''
age= 67
if age < 20:
    print("20살 미만")
elif age >30 and age <50:
    print("30살 이상 50 이하")
else:    
    print("20살 이상")
'''

#35
'''
temp=int(input("현재 온도를 입력하시오: "))
if temp >= 25:
    print("반바지를 입으세요.")
else: 
    print("긴바지를 입으세요")
'''

#36
'''
grade=int(input("성적을 입력하시오: "))
if grade >= 90:
    print("A 학점입니다.")
elif grade >= 80:
    print("B 학점입니다.")
elif grade >= 70:
    print("C 학점입니다.")
elif grade >= 60:
    print("D 학점입니다.")
else:
    print("F 학점입니다.")
'''

#37
'''
import random
firstnum=random.randint(1,100)
secondnum=random.randint(1,100)

minus=int(input(str(firstnum)+"-"+str(secondnum)+"="))

if minus == firstnum-secondnum:
    print("맞았습니다.")
else:
    print("틀렸습니다.")
'''

#38
'''
integer=int(input("정수를 입력하시오 : "))

if integer%2 == 0 and integer%3 == 0:
    print("2와 3으로 나누어 떨어집니다.")
else:
    print("2와 3으로 나누어 떨어지지않습니다.")
'''
#39
#num=import(int(복권번호를 입력하시오(10에서 99사이)))

#40
'''
import turtle
turtle.Turtle()
turtle.shape("turtle")

x1=int(input("작은원 x: "))
y1=int(input("작은원 y: "))
x2=int(input("큰원 x: "))
y2=int(input("큰원 y: "))
radius1=int(input("작은 반지름의 크기: "))
radius2=int(input("큰 반지름의 크기: "))


turtle.up()
turtle.goto(x1,y1)
turtle.down()
turtle.circle(radius1)

turtle.up()
turtle.goto(x2,y2)
turtle.down()
turtle.circle(radius2)

#여기서 x y가 달ㄹ른데 radius가 같으면 좀 햇갈;;


turtle.done()
'''




#41
'''
for even in range(2,101,2):
    print(even,end='\t')
'''

#42
'''
year = 0
balance = 1000

while balance >= 2000:
    year += 1
    interest = balance * 0.07
    balance += interest
    
    break

print(year, "년이 걸립니다.")
'''

#43
'''
n=1234
sum=0

while n>0:
    digit = n %10
    sum+=digit
    n//=10

print(sum)

'''
#44
'''
import random

while True:
    num1=random.randint(11,19)
    num2=random.randint(11,19)
    mult=int(input(str(num1)+"*"+str(num2)+"는 :"))
    if mult == num1 * num2:
        print("맞았습니다람쥐~.~")
        break
  '''  
#45


#47
'''
import turtle
turtle.Turtle()
turtle.shape("circle")
turtle.color("blue")

for _ in range(1,7,1):
    turtle.forward(200)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.up()
    turtle.right(15)
    turtle.goto(0,0)
    turtle.down()
    

turtle.done()
'''

#48
'''
import turtle
turtle.Turtle()
turtle.shape("turtle")
turtle.color("red")



for _ in range(10):
    turtle.left(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(141.4213526)
    turtle.right(135)
    turtle.forward(100)
    turtle.right(190)



turtle.done()
'''
#50
'''
import turtle
turtle.Turtle()
turtle.shape("turtle")
turtle.color("blue")

for _ in range(6):
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.done()
'''

