'''
Para esse Exemplo, será montado:

1º -> Uma classe que não segue o primeiro princípio do SOLID - Responsabilidade Única.
2º -> A Adequação dessa classe ao princípio da responsabilidade única.
'''

# Classe que não segue o Princípio da Responsabilidade Única.
class SistemaDeCadastro:

    def cadastro(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print('Aguarde!  Acessando o Banco de Dados...')
            print(f'Úsuário: {nome}, Idade: {idade} -> \033[1;32mCadastrado com Sucesso!\033[m')
        else:
            print('\033[1;31m Dados Inválidos! Por favor Verifique os Dados e tente Novamente.\033[m')


'''
A Classe acima tem mais de uma responsabilidade. Ela verifica os dados, "acessa o banco" e mostra mensagem de sucesso e erro.


-> Abaixo, essa mesma classe, será modificada para seguir o Princípio da Responsabilidade Única.
'''
class NovoSistemaDeCadastro:

    def cadastro(self, nome: str, idade: int) -> None:
        if self.__verifica_os_dados(nome, idade):
            self.__cadastra_no_DB(nome, idade)
        else:
            self.__erro_no_cadastro()


    def __verifica_os_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False


    def __cadastra_no_DB(self, nome: str, idade: int) -> None:
        print('\033[1;33mAguarde!  Acessando o Banco de Dados...\033[m')
        print(f'Úsuário: {nome}, Idade: {idade} -> \033[1;32mCadastrado com Sucesso!\033[m')


    def __erro_no_cadastro(self) -> None:
        print('\033[1;31mDados Inválidos! Por favor, verifique os dados e tente novamente.\033[m')


# Instanciando e usando a Classe NovoSistemeDeCadastro, que Segue o Princípio da Responsabilidade Única."
usr = NovoSistemaDeCadastro()

# Exemplo com dados corretos.
usr.cadastro('Eliel', 27)

print('-' * 50)

# Exemplo com dados errados.
usr.cadastro('Eliel', '27')


'''
Observação: Esse é um exemplo Simples. Cada um dos métodos privados criados para atender a necessidade de adequação dessa classe, poderia ser criado dentro de outras classes, em sistemas mais robustos e complexos.
'''