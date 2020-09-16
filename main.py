def hello():
    print('Дарова ебать. Че хочешь сделать блять епта?')
    #print('Введите выражение через пробел. (Пример 2 * 2 / 4')

#def isok(_a,_b):
    #if _a.isNumeric() and _b.isNumeric():
    #    return True
    #return False


#def inputNum():
   

def sum(_a,_b):
    return (f'Сумма чисел равна {_a + _b} блять')


def mult(_a,_b):
    return (f'Произведение чисел равно {_a * _b} ебать')


def div(_a,_b):
    return (f'Частное чисел равно {_a // _b} сука')


def subtract(_a,_b):
    return (f'Разность чисел равно {_a - _b} пидар')


def main():
    hello()
    #inputNum()
    a, b = map(int, input().split())
    #if isok(a,b) == True:
    operation = input()
    if operation == '+':
        print(sum(a,b))
    elif operation == '-':
        print(subtract(a,b))
    elif operation == '*':
        print(mult(a,b))
    elif operation == '//':
        print(div(a,b))





if name == '__main__':
    main()