import random
current_num = 1
numA = 0
numB = 0
num = 0

class brGame():

    def __init__(self, Aplayer, Bplayer):
        self.Aplayer = Aplayer
        self.Bplayer = Bplayer

    def Aplayer(self):
        global current_num
        if current_num > 31:
            print('playerA win!')
            exit()
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

    def Computer(self):
        global current_num
        if current_num > 31:
            print('Computer win!')
            exit()
        else:
            num = random.randint(1, 3)
            numB = current_num + num
            for current_num in range(current_num, numB):
                print(f'Computer : {current_num}')
                current_num += 1   
        

brGame("Aplayer", "Computer")
while True:
    brGame.Aplayer("Aplayer")
    brGame.Computer("Computer")
