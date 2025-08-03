class funcionario():
    def __init__(self, nome = 'Sem_Nome', salario = 0.0, data_admissao = 'DD/MM/AAAA'):
        self.salario = salario
        self.nome = nome
        self.data_admissao = data_admissao

    def __repr__(self):
        return (f'Funcionário {self.nome}, com salário de R$ {self.salario:.2f}, admitido em {self.data_admissao}.')

    def definir_salario(self, salario):
        self.salario = salario


    def definir_nome(self, nome):
        self.nome = nome

    def definir_data_admissao(self, data):
        self.data_admissao = data

    def __add__(self, other):
        if isinstance(other, funcionario):
            return self.salario + other.salario
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, funcionario):
            return abs(self.salario - other.salario)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, funcionario):
            return self.salario == other.salario
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, funcionario):
            return self.salario != other.salario
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, funcionario):
            return self.salario > other.salario
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, funcionario):
            return self.salario >= other.salario
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, funcionario):
            return self.salario < other.salario
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, funcionario):
            return self.salario <= other.salario
        else:
            return NotImplemented

class gerente(funcionario):
    def __init__(self, nome = 'Sem_Nome', salario = 0.0, data_admissao = 'DD/MM/AAAA', bonus = 0.0):
        super().__init__(nome, salario, data_admissao)
        self.bonus = bonus

    def definir_salario_final(self):
        salario_final = self.salario * (( self.bonus / 100) + 1)
        return salario_final