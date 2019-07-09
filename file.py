import os

# print(os.listdir())
# os.rename('dog.py', 'hello.py')
# print(os.listdir())
# os.chdir('report')
# os.system('rm a.txt')


#200번 반복하여 파일을 생성
for i in range(200):
    os.system('touch ./report/samsung_report{0}.txt'.format(i))


#200개의 파일의 이름 수정
for i in range(200):
    name_b = './report/samsung_report{0}.txt'.format(i)
    name_after = name_b.replace('samsung', 'SSAFY')
    os.rename(name_b, name_after)



