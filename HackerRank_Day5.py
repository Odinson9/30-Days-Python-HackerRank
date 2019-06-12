def multiples():
    N = int(input().strip())
    for number in range(1, 11):
        print('{0} x {1} = {2}'.format(N, number, N*number))

multiples()