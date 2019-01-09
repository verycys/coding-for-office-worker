# 목록 list, tuple
# 사전 dict - dictionary
# 집합 set

# 파이썬 data-type 자료
# https://docs.python.org/3.6/library/datatypes.html

# 강의 관련 자료
# https://docs.python.org/3.6/library/stdtypes.html

# list
print("list")
print([1, 2, 3])
list_a = [1, 2, 3]
print(list_a)
print(type([1, 2, 3]))
# index는 0부터 시작합니다.
print(list_a[1])
print(list_a[0])
# slice는 list를 자른다는 의미
print(list_a[0:2])
# append는 추가한다는 의미
list_a.append(4)
print(list_a)
list_a.clear()
print(list_a)
list_a.remove(2)
print(list_a)

# tuple (1, )
# tuple는 한번 지정된 값을 변경할 수 없음, 안정성 강화
print("tuple")
tuple_a = (1, 2, 3)
print(tuple_a)
print(type(tuple_a))
tuple_a.append(4)

# dict (map)
# key & value (apple & a trpe of fruits)
dict_a = {
    "apple" : "a type of fruits",
    "pen" : "a thing to write"
}
print(dict_a)
print(dict_a["apple"])
# edit value
dict_a["pen"] = "something to write"
print(dict_a)

# set set([])
set_a = set([1, 2, 3, 3, 3, 2, 2, 1, 1])
set_b = set([2, 4, 6])
print(set_a)
print(set_b)
# 집합 - 교집합, 합집합, 차집합, 여집합
# set은 중복이 제거된다
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
