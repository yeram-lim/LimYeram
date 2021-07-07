#6 -> 7
current_num = 1
numA = 0
numB = 0
num = 0
your_num = 0
who = 0
A = 0
B = 0

def brGame(your_num, current_num, who):
    your_num = current_num + num
    for current_num in range(current_num, your_num):
        print(f'player{who} : {current_num}')
        current_num += 1


while current_num <= 32:
    if current_num > 31:
        print('playerA win!')
        break
    else:
        while True:
            try:
                num = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
                if num >=4:
                    raise TypeError
                break
            except ValueError:
                print('정수를 입력하세요')
            except TypeError:
                print('1, 2, 3만 입력 가능')    
        brGame(numA, current_num, A)
    
    if current_num > 31:
        print('playerB win!')
        break
    else:
        while True:
            try:
                num = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
                if num >=4:
                    raise TypeError
                break
            except ValueError:
                print('정수를 입력하세요')
            except TypeError:
                print('1, 2, 3만 입력 가능')
        brGame(numB, current_num, B)