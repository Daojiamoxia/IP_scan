import turtle as t

def hh(i,j,value):
  if value==1:t.color("black","yellow")
  else: t.color("black","red")
  t.penup()
  t.goto(j*(30),i*(-30))
  t.pendown()
  t.begin_fill()
  for k in range(4):
    t.fd(30)
    t.right(90)
  t.end_fill()

t.screensize(800,800,)
t.color("black","yellow")
t.speed(10)
t.hideturtle()

with open( './IP.txt', 'r' ) as f:
    data=f.readlines()
    dataIP=[]
    for i in range(48):
        dataIP.append(0)
    for i in range(len(data)):
        data[i]=data[i][0:-2]
        ans=int(data[i][-2:])
        dataIP[ans-1]=1;
    
    print(dataIP)
    pos=[]
    for i in range(6):
      pos.append(dataIP[0+8*i:0+8*i+8])
    print(pos)
    for i in range(6):
        for j in range(8):
            print(pos[i][j],end='')
        print()
    print("----------")
    
    for i in range(6):
      if i%2==1: pos[i]=pos[i][::-1]

    for i in range(6):
        for j in range(8):
            print(pos[i][j],end='')
        print()

    for i in range(6):
        for j in range(8):
            hh(i,j,pos[i][j])

i=input()