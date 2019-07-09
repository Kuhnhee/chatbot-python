# 1 problem.txt 파일을 생성 후, 다음과 같은 내용을 작성
'''
0
1
2
3
'''
with open('problem.txt', 'w') as f:
    for i in range(4):
        f.write(str(i)+'\n')

# 2 problem.txt의 파일 내용을 다음과 같이 변경
'''
3
2
1
0
'''
with open('problem.txt', 'w') as f:
    for i in reversed(range(4)):
        f.write(str(i)+'\n')



# 3 proble.txt의 내용물을 역순으로 바꾸어 reverse.txt에 저장
with open('reverse.txt', 'w') as r, open('problem.txt', 'r') as p:
    text = p.readlines()
    text.reverse()
    for i in range(len(text)):
        r.write(text[i])