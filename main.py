def gather_data():
    n1 = int(input('first value:'))
    n2 = int(input('second value:'))

    return n1,n2

def main():
    n1,n2 = gather_data()
    print(n1*n2)
    return None

if __name__ == '__main__':
    main()