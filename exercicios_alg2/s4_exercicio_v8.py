class FilaDeAtendimento():
    def __init__(self):
        self.data = []

    def adicionar_chamado(self, cliente):
        self.data.append(cliente)

    def atender_proximo(self):
        if len(self.data) > 0:
            cliente_atendido = self.data.pop(0)
            return cliente_atendido
        else:
            print(f'Fila Vazia')

    def ver_fila(self):
        return self.data