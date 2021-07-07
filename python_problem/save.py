#6단계까지 저장본
current_num = 1
numA = 0
numB = 0
num = 0

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

        numA = current_num + num
        for current_num in range(current_num, numA):
            print(f'playerA : {current_num}')
            current_num += 1
    
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

        numB = current_num + num
        for current_num in range(current_num, numB):
            print(f'playerB : {current_num}')
            current_num += 1