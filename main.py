import test

def get_operation():
    op = input('operacao: ')

    return op


def gather_data():
    n1 = input('first value: ')
    n2 = input('second value: ')
    op = input('operation: ')

    return n1,n2,op

def main():
    n1,n2,op = gather_data()
    print(eval(n1+op+n2))
    return None

if __name__ == '__main__':
    main()