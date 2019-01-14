# 참과 거짓 boolean
# if
# true, false
# and, or, not

a = True
b = False
# A가 참이고, 그리고 B가 참이라면 (A와 B가 둘다 참이여야 된다)
print(a and b)
# A가 참이거나 혹은 B가 참이라면 (A나 B 둘 중에 하나라도 참이면 된다)
print(a or b)

# ==
a = True # a에 True 값을 할당한다는 의미
a == True # a와 True가 동일하다는 의미
print(a == True)
print(a is True)

d = 7
if d > 10:
    print("숫자는 5보다 큽니다.")
elif d > 5 and d <=10:
    print("숫자는 10보다 작거나 같고, 5보다는 큽니다.")
else:
    print("숫자는 5보다 작거나 같습니다.")
