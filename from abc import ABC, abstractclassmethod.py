from abc import ABC, abstractclassmethod, abstractproperty 
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereço = endereco
        self.contas = []
        self.indice_conta = 0

    
    def realizar_transacao(self, conta, transacao):
       if len(conta.historico.transacoes_do_dia()) >= 2:
           print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@" )
           return
        
        transacao.registrar(conta)
       
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self.__historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
       saldo = self.saldo
       excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('\n@@@ Operação falhou! Você não tem saldo suficiente. @@@')

       elif valor > 0:
            self.saldo -= valor
            print("\n ==== Saque realizado com sucesso! ====")
            return True

        else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return  False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite, limite=500, limite_saques=3)
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == saque.__name__]
            )
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.__name__]

        if excedeu_limite:
            print("\n@@@Operação falhou! Ovalor de saques excedeu o limite.@@@")

        elif excedeu_saques:
            print("\Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%Y %H:%M:%s"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or trasacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    def transacoes_do_dia(self):
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes
    

class Transacao(ABC):
    @property
    @abstractpropety
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(transacao):
    def __init__(self, valor):
        self.valor = Valor 

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Trasacao):
    
    def __init__(self, valor):
        self.valor = Valor 

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


