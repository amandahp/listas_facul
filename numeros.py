# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: amanda.hoffmann@aluno.faculdadeimpacta.com.br

def eh_primo(n: int) -> bool:
    number_int = isinstance(n, int)
    if n >= 2 and number_int:
        div = 0
        for i in range(1, n):
            if (n % i) == 0:
                div += 1
        n_div = div
        return (n_div == 1)


def lista_primos(n: int) -> list:
    number_int = isinstance(n, int)
    if n >= 2 and number_int:
        numbers_list = list([])
        for i in range(2, n):
            eh_primo(i)
            if eh_primo(i):
                numbers_list.append(i)
    return numbers_list


def conta_primos(s) -> dict:
    if isinstance(s, list) or isinstance(s, tuple):
        if len(s) > 0:
            repeat_list = list([])
            prime_number_list = list([])
            for i in s:
                eh_primo(i)
                if eh_primo(i):
                    prime_number_list.append(i)
            for j in lista_primos:
                repeticoes = lista_primos.count(j)
                if repeticoes >= 1:
                    repeat_list.append(repeticoes)
            dicionario = dict(zip(lista_primos, repeat_list))
        return dicionario
    else:
        return {}


def eh_armstrong(n: int) -> bool:
    numero = n
    numero_int = isinstance(numero, int)
    if numero >= 0 and numero_int:
        qtia_digitos = len(str(numero))
        valores_digitos = [int(_) for _ in str(numero)]
        soma_digitos = 0
        for digito in valores_digitos:
            digito_elevado = digito**qtia_digitos
            soma_digitos += digito_elevado
    return (numero == soma_digitos)


def eh_quase_armstrong(n: int) -> bool:
    e_quase_armstrong = bool()
    numero = n
    numero_int = isinstance(numero, int)
    if numero >= 0 and numero_int and not eh_armstrong(numero):
        qtia_digitos = len(str(numero))
        valores_digitos = [int(_) for _ in str(numero)]
        soma_digitos = 0
        for digito in valores_digitos:
            digito_elevado = digito**qtia_digitos
            soma_digitos += digito_elevado
        if soma_digitos == (numero + 1) or soma_digitos == (numero - 1):
            e_quase_armstrong = bool(True)
        return e_quase_armstrong
    else:
        e_quase_armstrong = bool(False)
        return e_quase_armstrong


def lista_armstrong(n: int) -> list:
    numero = n
    numero_int = isinstance(numero, int)
    if numero >= 0 and numero_int:
        lista_armstrong = list([])
        for i in range(0, numero):
            eh_armstrong(i)
            if eh_armstrong(i):
                lista_armstrong.append(i)
        return lista_armstrong


def eh_perfeito(n: int) -> bool:
    numero = n
    numero_int = isinstance(numero, int)
    if numero >= 2 and numero_int:
        sum = 0
        for i in range(1, numero):
            valor = (numero % i)
            if valor == 0:
                sum += i
        return (sum == numero)


def lista_perfeitos(n: int) -> list:
    numero = n
    numero_int = isinstance(numero, int)
    if numero >= 2 and numero_int:
        lista_perfeitos = list([])
        for i in range(1, numero):
            eh_perfeito(i)
            if eh_perfeito(i):
                lista_perfeitos.append(i)
        return lista_perfeitos
