#무작위로 뽑는것 랜덤 library 사용 하기

from random import *

# print(random())   # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()*10)  # 0.0 ~ 10.0 미만의 임의의 값 생성                                      # V
# print(int(random()*10))   # 0 ~ 10 미만의 임의의 값 생성

# print(int(random()*10) + 1)  # 1 ~ 10 이하의 임의의 값 생성
# print(int(random()*10))


print(int(random() * 45) + 1)    # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)

print(randrange(1, 46))    # 1 부터 46 미만(45이하)의 임의의 값을 생성
print(randint(1, 45))   # 1 부터 45 이하의 임의의 값 생성