import random
random_number = random.randint(1, 100)
count = 0
game = True

while game:
    print('1 이상 100 이하의 숫자를 입력하세요: ')
    my_number = input()
    if  0 <= int(my_number) <= 100:
        if int(my_number) > random_number:
            print('다운')
            count += 1
        elif int(my_number) < random_number:
            print('업')
            count += 1
        else:
            print('정답입니다!')
            print(f'시도한 횟수: {count}')
            print('다시 하시겠습니까? (y/n)')
            while True:
                ans = input()
                if ans == 'y':
                    random_number = random.randint(1, 100)
                    count = 0
                    break
                elif ans == 'n':
                    print('게임을 종료합니다.')
                    game = False
                    break
                else:
                    print('y와 n 중 하나를 입력해 주십시오.')
    else:
        print('올바른 범위의 숫자를 입력해 주십시오.')