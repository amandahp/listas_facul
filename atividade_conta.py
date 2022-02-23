# Programação Orientada a Objetos
# AC02 ADS-EaD - Implementação de classes
#
# Email Impacta: amanda.hoffmann@aluno.faculdadeimpacta.com.br


class Conta:
    def __init__(self, titular, agencia, numero, saldo_inicial):
        self.__titular = titular
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo_inicial
        self.__ativa = False
        self.__operacoes = [('saldo inicial', saldo_inicial)]

    @property
    def titular(self):
        return self.__titular

    @property
    def agencia(self):
        return self.__agencia

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def ativa(self):
        return self.__ativa

    def operacoes(self):
        return self.__operacoes

    @ativa.setter
    def ativa(self, situacao: bool):
        if isinstance(situacao, bool):
            self.__ativa = situacao

    def depositar(self, valor):
        if self.ativa and valor > 0:
            self.__saldo = self.__saldo + valor
            self.__operacoes += [("deposito", valor)]

    def sacar(self, valor):
        if self.__ativa and self.__saldo >= valor:
            if valor > 0:
                self.__saldo = self.__saldo - valor
                self.__operacoes += [("saque", valor)]

    def transferir(self, conta_destino, valor):
        if self.__ativa and conta_destino.ativa and self.__saldo > 0 and  valor > 0 and self.__saldo >= valor: # noqa
            self.__saldo -= valor
            conta_destino.depositar(valor)
            self.__operacoes += [("transferencia", valor)]

    def tirar_extrato(self):
        return self.__operacoes

    def transformar_extrato(self):
        def buscar(valor):
            i = 0
            for sub in self.__operacoes:
                if valor in sub:
                    break
                i += 1
            else:
                return None
            return i

        def buscar_valor(tupla):
            indice = int()
            if buscar(tupla) is not None:
                indice1 = buscar(tupla)
                indice += indice1
                return (self.__operacoes[indice])
            else:
                return "0"
        return f'''
        -------------------------------------------------
        operação             |    entrada no extrato
        ---------------------|---------------------------
        * abertura da conta  | {self.__operacoes[0]}
        * depósito           | {buscar_valor("deposito")}
        * saque              | {buscar_valor("saque")}
        * transferencia      | {buscar_valor("transferencia")}
        -------------------------------------------------         '''
