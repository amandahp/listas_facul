# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: amanda.hoffmann@aluno.faculdadeimpacta.com.br

# ---------------------------------------
# Função que verifica se o número é primo

def prime_number(num: int) -> bool:
    mult = 0
    for i in range(2, num):
        if (num % i) == 0:
            mult += 1
    n_mult = mult
    return (n_mult == 0)


def ind_out_if_the_number_is_prime(value):
    number_int = isinstance(value, int)
    if value >= 2 and number_int:
        prime_number(value)
        if prime_number(value):
            print(f'O número {value} é primo')
        else:
            print(f'O número {value} não é primo')
    else:
        print(f'O número {value} é inválido')


def input_insertion_prime_number(value: int):
    ind_out_if_the_number_is_prime(value)


# Caso prefira adicionar seus valores manualmente,
# comente a linha 38 e descomente a linha 37

def test_prime_number():
    # inputs = []
    inputs = ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 6, 9, 9.8, 0.3, -98]) # noqa E501
    if len(inputs) > 0:
        for i in inputs:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print(f"Digite um número: {i}")
            ind_out_if_the_number_is_prime(i)
            print("\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("---------------Fim do teste------------------")
    else:
        number = int(input("Digite um número:"))
        input_insertion_prime_number(number)


test_prime_number()
print("----------------------------------------------------------\n")

# ------------------------------------------
# Função que retorna lista de números primos


def list_prime_numbers(x: int):
    number_int = isinstance(x, int)
    if x >= 2 and number_int:
        numbers_list = list([])
        for i in range(2, x):
            prime_number(i)
            if prime_number(i):
                numbers_list.append(i)
        if len(numbers_list) == 0:
            print('Não há números primos menores que 2')
        else:
            print(f'Os números primos menores que {x} são: {numbers_list}')
    else:
        print(f'O número {x} é inválido')


def input_insertion_prime_number_for_list(value: int):
    list_prime_numbers(value)


# Caso prefira adicionar seus valores manualmente, comente a linha 78 e
# descomente a linha 77

def test_list_prime_number():
    # inputs = []
    inputs = [2, 3, 5, 7, 11, 13, 9.8, 0.3, -98, 4, 6, 8, 10]
    int_list = list(map(int, inputs))
    if len(int_list) > 0:
        for i in inputs:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print(f"Digite um número: {i}")
            list_prime_numbers(i)
            print("\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("---------------Fim do teste------------------")
    else:
        number = int(input("Digite um número:"))
        input_insertion_prime_number_for_list(number)


test_list_prime_number()
print("----------------------------------------------------------\n")


# --------------------------------------------------------
# Função que conta a quantidade de primos em uma sequência

def counting_the_number_of_prime(numbers_of_list):
    list_without_repetition = list(dict.fromkeys(numbers_of_list))
    values_repetitions = list([])
    for i in list_without_repetition:
        repetition = (numbers_of_list.count(i))
        values_repetitions.append(repetition)
    dict_from_list = dict(zip(list_without_repetition, values_repetitions))
    print(dict_from_list)


def creating_the_dict(list_numbers):
    _list = list_numbers.split()
    user_list = list(_list)
    if len(user_list) > 1:
        list_numbers_prime = list([])
        for i in user_list:
            characters = ","
            for x in range(len(characters)):
                i = i.replace(characters[x], "")
            num = int(float(i))
            number_int = isinstance(num, int)
            if num >= 2 and number_int:
                prime_number(num)
                if prime_number(num):
                    list_numbers_prime.append(i)
        if len(list_numbers_prime) > 0:
            counting_the_number_of_prime(list_numbers_prime)
        else:
            print("Näo há números primos nessa sequência")
            print("{}")
    else:
        print('Número inválido')


def input_insertion_list_number(itens: str):
    creating_the_dict(itens)


# Caso prefira adicionar seus valores manualmente, comente a linha 78 e
# descomente a linha 77

def test_dict_prime_number():
    # inputs = []
    inputs = [["3 5 7"], ["11 13 9.8 0.3"], ["-98 4 6 8 10"], [("1, 2, 4,5")]]
    if len(inputs) > 0:
        for i in inputs:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            for j in i:
                print(f'Digite uma sequência de números: {i}')
                creating_the_dict(j)
                print("\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("---------------Fim do teste------------------")
    else:
        number = input(str("Digite uma sequência de números:"))
        input_insertion_list_number(number)


test_dict_prime_number()
print("----------------------------------------------------------\n")


# -----------------------------------------------
# Função que verifica se um número é de Armstrong


def check_if_it_is_armstrong_number(val: int) -> bool:
    digits = [int(_) for _ in str(val)]
    number_of_digits = len(str(val))
    counter = 0
    for _ in digits:
        counter += _**number_of_digits
    return (counter == val)


def check_the_number(number: int):
    number_int = isinstance(number, int)
    if number >= 0 and number_int:
        check_if_it_is_armstrong_number(number)
        if check_if_it_is_armstrong_number(number):
            print(f"O número {number} é um número de Armstrong")
        else:
            print(f"O número {number} não é um número de Armstrong")
    else:
        print("Número inválido")


def print_number(value: int):
    check_the_number(value)


# Para fazer a entrada manual, comente a linha 182 e 183, e descomente a linha
# 181


def test_armstrong_number():
    # inputs = []
    inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817, # noqa E501
    9926315, 24678050, 24678051, 88593477, 146511208, 472335975, 534494836, 912985153, 4679307774, 32164049650, 32164049651, -1, 9.87, 78, 97, 22] # noqa E501
    if len(inputs) > 0:
        int_list = list(map(int, inputs))
        for i in int_list:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print(f'Digite um número: {i}')
            check_the_number(i)
            print("\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("---------------Fim do teste------------------")
    else:
        number = int(input("Digite um número:"))
        print_number(number)


test_armstrong_number()
print("----------------------------------------------------------\n")


# -----------------------------------------------------
# Função que verifica se um número é quase de Armstrong

def check_if_it_is_almost_armstrong_number(val: int) -> bool:
    counter_2 = 0
    result = check_if_it_is_armstrong_number(val)
    if result == bool(False):
        digits = [int(_) for _ in str(val)]
        number_of_digits = len(str(val))
        for _ in digits:
            counter_2 += _**number_of_digits
    return (counter_2 == val + 1 or counter_2 == val - 1)


def check_the_number_input(number: int):
    number_int = isinstance(number, int)
    if number >= 0 and number_int:
        check_if_it_is_almost_armstrong_number(number)
        if check_if_it_is_almost_armstrong_number(number):
            print(f"O número {number} é quase um número de Armstrong")
        elif check_if_it_is_armstrong_number(number):
            print(f"O número {number} é um número de Armstrong")
        else:
            print(f"O número {number} não é um número de Armstrong")
    else:
        print("Número inválido")


def input_number_armstrong(value: int):
    check_the_number_input(value)


# Para fazer a entrada manual, comente a linha 165 e 166, e descomente a linha
# 164


def test_almost_armstrong_number():
    # inputs = []
    inputs = [2, 3, 4, 5, 817, 10, 37, 75] # noqa e501
    if len(inputs) > 0:
        int_list = list(map(int, inputs))
        for i in int_list:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print(f'Digite um número: {i}')
            check_the_number_input(i)
            print("\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("---------------Fim do teste------------------")
    else:
        number = int(input("Digite um número:"))
        input_number_armstrong(number)


test_almost_armstrong_number()
print("----------------------------------------------------------\n")


# --------------------------------------------------------
# Função que lista os números e Armstrong até n


def list_armstrong_numbers(number_input: int):
    number_int = isinstance(number_input, int)
    if number_input > 0 and number_int:
        numbers_list_armstrong = list([])
        for i in range(1, number_input):
            check_if_it_is_armstrong_number(i)
            if check_if_it_is_armstrong_number(i):
                numbers_list_armstrong.append(i)
        if len(numbers_list_armstrong) == 0:
            print('Não há números de Armstrong nesse intervalo')
        else:
            print(f'Os números de Armstrong menores que {number_input} são: {numbers_list_armstrong}') # noqa E501
    else:
        print(f'O número {number_input} é inválido')


def input_insertion_armstrong_number_for_list(value: int):
    list_armstrong_numbers(value)


# Caso prefira adicionar seus valores manualmente, comente a linha 289 e
# descomente a linha 288

def test_list_armstrong_number():
    # inputs = []
    inputs = [2, 3, 5, 7, 11, 13, 9.8, 0.3, -98, 4, 6, 8, 10, 999, 99999]
    int_list = list(map(int, inputs))
    if len(int_list) > 0:
        for i in inputs:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print(f'Digite um número: {i}')
            list_armstrong_numbers(i)
            print("\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("---------------Fim do teste------------------")
    else:
        number = int(input("Digite um número:"))
        input_insertion_armstrong_number_for_list(number)


test_list_armstrong_number()
print("----------------------------------------------------------\n")


# ----------------------------------------------
# Função que verifica se um número é dito perfeito


def perfect_number(num: int) -> bool:
    div = list([])
    for i in range(1, num):
        if (num % i) == 0:
            div.append(i)
    sum_div = sum(div)
    return (num == sum_div)


def ind_out_if_the_perfect_number(value):
    number_int = isinstance(value, int)
    if value >= 2 and number_int:
        perfect_number(value)
        if perfect_number(value):
            print(f'O número {value} é perfeito')
        else:
            print(f'O número {value} não é perfeito')
    else:
        print(f'O número {value} é inválido')


def input_insertion_perfect_number(value: int):
    ind_out_if_the_perfect_number(value)


# Caso prefira adicionar seus valores manualmente, comente a linha 38 e
# descomente a linha 37

def test_perfect_number():
    # inputs = []
    inputs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 6, 9, 9.8, 0.3, -98, 6, 28, 496, 8128, 33550336] # noqa E501
    if len(inputs) > 0:
        for i in inputs:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print(f'Digite um número: {i}')
            ind_out_if_the_perfect_number(i)
            print("\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("---------------Fim do teste------------------")
    else:
        number = int(input("Digite um número:"))
        input_insertion_perfect_number(number)


test_perfect_number()
print("----------------------------------------------------------\n")


# -----------------------------------------------
# Função que lista os números ditos perfeitos até n


def list_perfect_numbers(x: int):
    number_int = isinstance(x, int)
    if x >= 2 and number_int:
        numbers_list = list([])
        for i in range(2, x):
            perfect_number(i)
            if perfect_number(i):
                numbers_list.append(i)
        if len(numbers_list) == 0:
            print('Não há números perfeitos menores que 6')
        else:
            print(f'Os números perfeitos menores que {x} são: {numbers_list}')
    else:
        print(f'O número {x} é inválido')


def input_insertion_perfect_number_for_list(value: int):
    list_perfect_numbers(value)


# Caso prefira adicionar seus valores manualmente, comente a linha 78 e
# descomente a linha 77

def test_list_perfect_number():
    # inputs = []
    inputs = [2, 3, 5, 7, 11, 13, 9.8, 0.3, -98, 4, 6, 8, 10, 496, 8128]
    int_list = list(map(int, inputs))
    if len(int_list) > 0:
        for i in inputs:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print(f'Digite um número: {i}')
            list_perfect_numbers(i)
            print("\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("---------------Fim do teste------------------")
    else:
        number = int(input("Digite um número:"))
        if number >= 5000:
            print("Isso pode demorar um pouco :/")
            print("-----------------------------")
        input_insertion_perfect_number_for_list(number)


test_list_perfect_number()
print("----------------------------------------------------------\n")
