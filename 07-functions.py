# 함수 functions
# 입력값 parameters, 반환값 return

# 함수를 활용할 시 hi를 hello로 바꾸고 싶을 때 함수값만 바꾸면 전체 변경가능함.
def hello_friends(name):
    print("hi, {}".format(name))

name1 = "marco"
name2 = "jane"
name3 = "john"
name4 = "tom"
name5 = "marco"
name6 = "jane"
name7 = "john"
name8 = "tom"
# print("hi, {}".format(name1))
# print("hi, {}".format(name2))
# print("hi, {}".format(name3))
# print("hi, {}".format(name4))
# print("hi, {}".format(name5))
# print("hi, {}".format(name6))
# print("hi, {}".format(name7))
# print("hi, {}".format(name8))

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)

# 1) 입력값 o, 반환값 o 함수
def sum(a, b):
    return a + b

# 2) 입력값 o, 반환값 x 함수
def hello_friends(name):
    print("hello, {}".format(name))

# 3) 입력값 x, 반환값 o 함수
def return_1():
    return 1

# 4)입력값 x, 반환값 x 함수
def hello_world():
    print("hello world")

# num_1 = return_1()
# print(num_1)
