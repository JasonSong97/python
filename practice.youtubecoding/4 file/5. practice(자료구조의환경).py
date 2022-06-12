#자료구조의 변경

menu = {"커피", "우유", "주스"}   
print(menu, type(menu))     # set로 바뀜  /  중괄호

menu = list(menu)
print(menu, type(menu))    # lsit 로 변경  /  대괄호

menu = tuple(menu)
print(menu, type(menu))      #소괄호

menu = set(menu)
print(menu, type(menu))