#내용 변경이나 추가 불가능 / 속도가 리스트보다 빠름

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")  #튜플은 더하거나 뺴지 못함 ㅇㅇ

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")   # 튜플은 이렇게 가능
print(name, age, hobby)