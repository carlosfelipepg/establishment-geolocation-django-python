import time


def challenge():
    print('Cada caso tem uma palavra de no mínimo, 9 e, no máximo 10000 letras.')
    qtd = input('Quantidade: ')
    try:
        qtd = int(qtd)
        print(qtd)
    except ValueError:
        print("Não é número")
        return

    times_list = []
    for i in range(int(qtd)):
        value = ''
        runtime = 0
        while not 10000 >= value.__len__() >= 9:
            start = time.time()
            value = input('Palavra ' + str(i + 1) + ': ')
            end = time.time()
            runtime = end - start
        times_list.append(round(runtime, 2))

    print(times_list)
    return times_list


if __name__ == '__main__':
    challenge()
