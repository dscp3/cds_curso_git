def gather_data():
    n1 = input('first value: ')
    n2 = input('second value: ')

    return n1,n2

def print_message(n1,n2):
    print(f'os valores {n1} e {n2} somados dão {n1+n2}')

def main():
    n1,n2 = gather_data()
    print_message(n1,n2)
    return None

if __name__ == '__main__':
    main()