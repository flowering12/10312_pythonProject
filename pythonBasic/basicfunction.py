#f(x) = 3x + 5

def tmFunction(x):
    return  3 * x + 5

print(tmFunction(5))

#게임
# 랜던 값 할당받기 <- 기능
#사용자 입력받기
#값이랑 사용자 입력 비교하기
# 행맨
# _____
# 있으면 통과, 없으면 1 데카
# 데카가 n개 이상이면 out


# 게임선택 - 1. 행맨 2. up down, 3. 종료
# "행맨"
# -> 랜덤으로 단어 선정
# -> 사용자 입력을 받기
# -> 결과판단

# def menuPrint():
#     print("================GAME=================="0)
#     print("행맨")
#     print( "업다운")
#     print( "종료")
def runUpDown():
    answer = random.randrange(0, 10)
    chance = 3

    # 사용자가 answer 맞출때까지 반복
    # 1. 사용자에게 기회주기(3번)
    # 2. 틀렸을때 updown 출력해주기
def MenuPrint ():
    print("=======GAME=======")
    print("1. 행맨")
    print("2. 업다운")
    print("0. 종료")
    print("==================")

userIinput = -1


def getRandownWord():
    words = ["hang", "pretty", "apple", "and", "water", "samsung", "MCdonalds", "fluent", "voca", "galaxy"]
    return words[random.randrange(0, len(words))]

hangman_input_history =[]


def getHangManInput():
    while True:
        user_input =input("Input alphabet :::")
        if(hangmanuser_input_history.index(alphabet)):
            print("이미 입력한 값입니다. 새로운 알파벳을 입력해주세요")
        else:
            return alphabet
def runHangMan():
    user_input_history = []
    word = getRandownWord()
    print("_"*len(word))

    user_input = getHangmanInput(hangman_input_history)


def runUpDown():
    def runUpDown():
    answer = random.randrange(0, 10)
    chance = 3

    # 사용자가 answer 맞출때까지 반복
    # 1. 사용자에게 기회주기(3번)
    # 2. 틀렸을때 updown 출력해주기

    while chance > 0:
        user_input = int(input("값을 입력하세요 >>"))

        if user_input == answer:
            print("정답입니다!")
            break
        else:
            chance = chance - 1
            if user_input > answer:
                print("down")
            else:
                print("up")

while userIinput != 0:
    MenuPrint()
    userInput = int(input("SELECT MENU :::"))

    if userInput == 1:
        runHangMan()
    elif userInput ==2:
        runUpDown()