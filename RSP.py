import random
list_rsp = ['가위', '바위', '보']
game = True
win = lose = draw = 0

while game:
    num_cpu = random.randint(0, 2)
    print('가위, 바위, 보 중 하나를 입력하세요.')
    choice_user = input()
    if choice_user in list_rsp:
        num_user = list_rsp.index(choice_user)
        print(f'상대의 선택은 {list_rsp[num_cpu]},')
        if num_cpu == num_user:
            print('비겼습니다.')
            draw += 1
        elif num_user - num_cpu == 1 or num_user - num_cpu == -2:
            print('이겼습니다.')
            win += 1
        else:
            print('졌습니다.')
            lose += 1
        print('다시 하시겠습니까? (y/n)')
        while True:
            answer = input()
            if answer == 'n' or answer == 'N':
                game = False
                print('게임을 종료합니다.')
                print(f'게임 결과는 {win}승 {lose}패 {draw}무입니다.')
                break
            elif answer == 'y' or answer == 'Y':
                break
            else:
                print('y와 n 중 하나를 입력해 주십시오.')
    else:
        print('유효한 입력이 아닙니다.')