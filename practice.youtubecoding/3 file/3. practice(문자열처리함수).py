python = "Python is Amazing"
# print(python.lower())   # 소문자로 바꾸는 거임
# print(python.upper())      # 대문자로 바꾸는 거임
# print(python[0].isupper())    # 해당 함수의 0번째가 대문자인지 묻는 것
# print(len(python))    #길이를 의미함 
# print(python.replace("Python", "Java"))            # 대체하는 것 replace

index = python.index("n")   #n이 몇번쨰에 위치하는지 알려주는 함수
print(index)
index = python.index("n", index + 1)     # 앞에거 계산후, 그후의 자리수부터 숫자를 찾는 함수
print(index)

# print(python.find("Java"))     #내가 원하는 값이 없으면 -1로 알려줌
# print(python.index("Java"))       #오류남 / 그래서 뒤에 다른 문장이 있어도 진행이 안됨 ㅇㅇ

# print(python. count("n"))       # 해당 함수에 n이 몇번 들어있는지 counting

