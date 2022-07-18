#!/usr/bin/env python
# coding: utf-8

# In[2]:


a,b = 100,200
print(a==b)


# In[5]:


a,b = 100,200
print(a==b , a!=b , a>=b , a<=b )


# In[6]:


bin(10)


# In[7]:


bin(123)


# In[8]:


10 & 7
123 & 456


# In[9]:


10 & 7 , 123 & 456


# In[10]:


10 & 7;
123 & 456


# In[11]:


10 & 7, 123 & 456


# In[12]:


0xFFFF & 0x0000


# In[13]:


10 | 8


# In[14]:


hex(10)


# In[15]:


bin(10)


# In[16]:


bin(8)


# In[17]:


a = 0xFF
print(a)


# In[18]:


oct(10)


# In[19]:


bin(0o12)


# In[20]:


bin(10)


# In[21]:


int(0b1010)


# In[22]:


10 | 7


# In[23]:


bin(10)


# In[24]:


bin(7)


# In[25]:


bin(1011)


# In[26]:


int(1011)


# In[27]:


int(0b1101)


# In[28]:


0b1010 | 0b111


# In[29]:


int(0b1100)


# In[30]:


bin(15)


# In[35]:


a = ord('A')
print("%d" %(a))
mask = 0x0F

print("%x & %x = %x" % (a,mask,a&mask))
print("%X & %X = %X" % (a,mask,a|mask))

mask = ord('a') - ord('A')

b = a ^ mask
print("%c ^ %d = %c" % (a,mask,b))
a = b ^ mask
print("%c ^ %d = %c" % (b,mask,a))


# In[36]:


a = 100
result = 0
i = 0

for i in range(1,5):
    result = a << i
    print("%d << %d = %d" %(a,i,result))
for i in range(1,5):
    result = a >> i
    print("%d >> %d = %d"%(a,i,result))


# In[39]:


a = int(input("시프트할 숫자는? "))
result = 0
i = 0
r = int(input("반복할 숫자는? "))

for i in range(1,r+1):
    result = a << i
    print("%d << %d = %d" %(a,i,result))
for i in range(1,r+1):
    result = a >> i
    print("%d >> %d = %d"%(a,i,result))


# In[49]:


a = 200

if a < 100:
    print("아닙니다.")
    print("거짓이므로 안보임???")
    

    
    print("프로그램 종료")    


# In[8]:


a = int(input("정수를 입력해보세요: "))

if a == 0:
    print("0을 제외한 다른 숫자를 입력해주세요.")
elif a % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")


# In[47]:


import turtle

swidth,sheight = 500,500
turtle.title('무지개색 원그리기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50 , height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.goto(0,-sheight / 2)
turtle.pendown()
turtle.speed(200)

for radius in range(1, 250):
    if radius % 6 == 0:
        turtle.pencolor('red')
        
    elif radius % 5 == 0:
        turtle.pencolor('purple')
    
    elif radius % 4 == 0:
        turtle.pencolor('black')
    
    elif radius % 3 == 0:
        turtle.pencolor('green')  
    
    elif radius % 2 == 0:
        turtle.pencolor('black')  
     
    elif radius % 1 == 0:
        turtle.pencolor('blue')
     
    else:
        turtle.pencolor('red')
        
    turtle.circle(radius)

turtle.done()


# In[49]:


fruit = ['사과','배','감']
if '사과' in fruit:
    print("사과가 있네요")


# In[52]:


import random

numbers = []
for num in range(0,10):
    numbers.append(random.randrange(0,10))

print("생성된 리스트",numbers)

for num in range(0,10):
    if num in numbers :
        print("숫자 %d은(는) 리스트에 있네요" %num)


# In[59]:


selelct,answer,numStr,num1,num2 = 0,0,"",0,0

select = int(input("1. 입력한 수식 계산, 2. 두 수 사이의 합계 : "))

if select == 1:
    numStr = input("수식을 입력하세요 : ")
    answer = eval(numStr)
    print("%s 결과는 %5.1f입니다." %(numStr,answer))
elif select == 2:
    num1 = int(input("첫번째 숫자를 입력해주세요 : "))
    num2 = int(input("두번째 숫자를 입력해주세요 : "))
    for i in range(num1,num2+1):
        answer = answer + i
    print("%d+...%d는 %d입니다." % (num1,num2,answer))
else : 
    print("1 또는 2를 입력해주세요")


# In[ ]:




