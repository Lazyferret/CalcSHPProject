def hello():
    print('������ �����. �� ������ ������� ����� ����?')
    #print('������� ��������� ����� ������. (������ 2 * 2 / 4')

#def isok(_a,_b):
    #if _a.isNumeric() and _b.isNumeric():
    #    return True
    #return False


#def inputNum():
   

def sum(_a,_b):
    return (f'����� ����� ����� {_a + _b} �����')


def mult(_a,_b):
    return (f'������������ ����� ����� {_a * _b} �����')


def div(_a,_b):
    return (f'������� ����� ����� {_a // _b} ����')


def subtract(_a,_b):
    return (f'�������� ����� ����� {_a - _b} �����')


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