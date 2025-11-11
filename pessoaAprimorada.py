# POO - Criando uma classe de Pessoa
# Atributos: nome, idade, cargo
class Pessoa:
  def __init__(self, nome, idade, cargo):
    self.nome = nome
    self.idade = idade
    self.cargo = cargo

# Métodos
  def informacoes(self):
    print(f'Nome: {self.nome}')
    print(f'Idade: {self.idade}')
    print(f'Cargo: {self.cargo}')

# Método para promover a pessoa
  def promover(self, novo_cargo):
    print(f'{self.nome} foi promovido(a) para a nova função de {novo_cargo}')

# Método para atualizar a idade
  def atualizar_idade(self, nova_idade):
    if nova_idade > self.idade:
      print(f'Atualizando a idade {self.idade} para {nova_idade}')
    else:
      print('A nova idade tem que ser maior que a anterior')

# Criando objetos da classe Pessoa
colaborador1 = Pessoa('Ana', 45, 'Terceirizada')
colaborador2 = Pessoa('Sarah', 22, 'Secretaria')
colaborador1.atualizar_idade(55)

# Usando os métodos dos objetos
colaborador1.informacoes()
colaborador1.promover('CEO')