import random
random_number = random.randint(1, 100)
x = ''
count = 0

def Answer(x):
    print('다시 하시겠습니까? (y/n)')
    ans = input()
    if ans == 'y':
        random_number = random.randint(1, 100)
        count = 0
        UpDown(x)
    elif ans == 'n':
        print('게임을 종료합니다.')
    else:
        print('y와 n 중 하나를 입력해 주십시오.')
        Answer(x)

def UpDown(num):
    print('숫자를 입력하세요: ')
    num = input()
    if int(num) < 0 or int(num) > 100:
        print('유효한 범위 내의 숫자를 입력하세요.')
        UpDown(x)
    global count
    global random_number
    if int(num) > random_number:
        print('다운')
        count += 1
        UpDown(x)
    elif int(num) < random_number:
        print('업')
        count += 1
        UpDown(x)
    else:
        print('정답입니다.')
        print(f'시도한 횟수: {count}')
        Answer(x)

UpDown(x)