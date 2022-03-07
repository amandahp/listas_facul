# Programação Orientada a Objetos
# AC03 ADS-EaD - Implementação de classes, herança, polimorfismo e lançamento de exceções. # noqa
#
# Email Impacta: amanda.hoffmann@aluno.faculdadeimpacta.com.br


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise TypeError
        if novo_nome == '' or len(novo_nome) == 0:
            raise ValueError("Nome inválido.")
        self.__nome = novo_nome

    @preco.setter
    def preco(self, novo_preco):
        if isinstance(novo_preco, int) or isinstance(novo_preco, float): # noqa
            if novo_preco > 0:
                self.__preco = novo_preco
            else:
                raise ValueError("Número menor que 0.")
        else:
            raise TypeError
        self.__preco = novo_preco

    def calcular_preco_com_frete(self):
        return self.__preco


class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso):
        super().__init__(nome, preco)
        self.peso = peso

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, novo_peso):
        if isinstance(novo_peso, int):
            if novo_peso > 0:
                self.__peso = novo_peso
            else:
                raise ValueError("Número menor que 0.")
        else:
            raise TypeError("")
        self.__peso = novo_peso

    def peso_em_kg(self):
        self.__peso /= 1000
        return self.__peso

    def calcular_preco_com_frete(self):
        return (super().calcular_preco_com_frete() + (self.peso_em_kg()*5))


class ProdutoEletronico(ProdutoFisico):
    def __init__(self, nome, preco, peso, tensao, tempo_garantia):
        super().__init__(nome, preco, peso)
        self.tensao = tensao
        self.__tempo_garantia = tempo_garantia

    @property
    def tensao(self):
        return self.__tensao

    @property
    def tempo_garantia(self):
        return(self.__tempo_garantia)

    @tensao.setter
    def tensao(self, nova_tensao):
        if isinstance(nova_tensao, int):
            if nova_tensao == 0 or nova_tensao == 127 or nova_tensao == 220:
                self.__tensao = nova_tensao
            else:
                raise ValueError("Valor inválido")
        else:
            raise TypeError
        self.__tensao = nova_tensao

    def calcular_preco_com_frete(self):
        frete = super().calcular_preco_com_frete()
        valor_final = frete + (frete * 0.01)
        return valor_final


class Ebook(Produto):
    def __init__(self, nome, preco, autor, numero_paginas):
        super().__init__(nome, preco)
        self.__autor = autor
        self.numero_paginas = numero_paginas

    @property
    def autor(self):
        return self.__autor

    @property
    def nome_exibicao(self):
        return f"{self.nome} ({self.__autor})"

    @property
    def numero_paginas(self):
        return self.__numero_paginas

    @numero_paginas.setter
    def numero_paginas(self, valor):
        if valor > 0:
            self.__numero_paginas = valor
        else:
            raise ValueError("Dado inválido")
        self.__numero_paginas = valor
