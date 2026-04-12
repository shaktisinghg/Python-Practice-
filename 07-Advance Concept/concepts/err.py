while True:
    try:
        a = int(input('inter number 1:- '))
        b = int(input('inter number 2:- '))
        print(f'sum is {a + b}')

    except Exception as e:
        print('Unknown error occured!', e)