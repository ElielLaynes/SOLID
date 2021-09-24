'''
Nesse exemplos vamos falar de 5º Princípio SOLID -> D -> Inversão de Dependência.

Importante: Não confundir Inversão de Dependência com Injeção de Dependência.
        A INVERSÃO -> É um conceito de POO, enquanto,
        A INJEÇÃO -> É um Design Pattern de Projeto.

Para Ficar mais claro esse diferença, vamos tratar esses dois conceito com um exemplo onde:
    1º -> Vamos construir um código com injeção de Dependência;
    2º -> Adequar esse Código a Inversão de Dependência através de Interface.
'''
from typing import Type


# 1º Exemplo: Implementando uma Injeção de Dependência
class MySqlRepo:

    def inserir(self, info) -> None:
        print(f'O Dado: {info} -> Foi Inserido com Sucesso no Banco!')
    

    def deletar(self, info) -> None:
        print(f'O Dado: {info} -> Foi Deletado com Sucesso do Banco!')



class Usuario:

    def __init__(self, respositorio: Type[MySqlRepo]) -> None:
        self.__repositorio = respositorio


    def armazenar_dado(self, info: any) -> None:
        self.__repositorio.inserir(info)


    def remover_dado(self, info: any) -> None:
        self.__repositorio.deletar(info)
'''
No Exemplo acima, estamos fazendo uma injeção de depêndencia com sucesso. Na Classe Usuario, o atributo repositorio está sendo tipado como a classe MySqlRepo, o que permite ter acesso aos métodos do MySqlRepo e utilizar ele atráves do atributo self.__repositorio.

    Agora, imagine que é necessário trocar o banco de MySql para um PostegreSQL ou MongoDB ou qualqer outro banco. E também imagine que em vez dos dois métodos que exemplificamos, tenha 200 métodos. Isso acaba ficando muito custoso e pouco escalável.

Por isso, vamos refazer esse exemplo usando o conceito de Inversão de Dependências e usar uma interface para implementar os métodos e fazer a comunicação para os bancos de dados que forem necessários.
'''

# 2º Exemplo: Implementando a Inversão de Dependências
from abc import ABC, abstractmethod


class InterfaceRepositorio(ABC):

    @abstractmethod
    def inserir(self, info: any) -> None:
        raise NotImplementedError


    @abstractmethod
    def deletar(self, info: any) -> None:
        raise NotImplementedError



class MySqlRepo(InterfaceRepositorio):

    def inserir(self, info) -> None:
        print(f'O Dado: {info} -> Foi \033[1;32mInserido\033[m com Sucesso no Banco MySql!')
    

    def deletar(self, info) -> None:
        print(f'O Dado: {info} -> Foi \033[1;31mDeletado\033[m com Sucesso do Banco MySql!')



class MongoRepo(InterfaceRepositorio):

    def inserir(self, info) -> None:
        print(f'O Dado: {info} -> Foi \033[1;32mInserido\033[m com Sucesso no Banco MongoDB!')
    

    def deletar(self, info) -> None:
        print(f'O Dado: {info} -> Foi \033[1;31mDeletado\033[m com Sucesso do Banco MongoDB!')



class Usuario:

    def __init__(self, respositorio: Type[InterfaceRepositorio]) -> None:
        self.__repositorio = respositorio


    def armazenar_dado(self, info: any) -> None:
        self.__repositorio.inserir(info)


    def remover_dado(self, info: any) -> None:
        self.__repositorio.deletar(info)
'''
O código acima exemplifica a Inversão de Depêndencia. Onde através da injeção de uma Interface chamada InterfaceRepositorio na Classe Usuario, conseguimos ter acesso aos métodos da interface.

 Nesse caso, é a interface que vai nortear o desenvolvimento e implementação de outras classes de banco. 
 
 Dessa forma poderíamos implementar qualquer banco de dados que fosse necessário de maneira simples e bem mais estrututada.
'''

# Instanciando as Classes e rodando o exemplo para ver o funcionamento do código de exemplificação.

# Instanciando as classes dos bancos
mysql = MySqlRepo()
mongodb = MongoRepo()

# Usando o Mysql
print('\n', '-' * 50, '\n-> Trabalhando com o MySql \n' )
usr_1 = Usuario(mysql)
usr_1.armazenar_dado('Eliel')
usr_1.remover_dado(20)


# Usando o MongoDB
print('\n', '-' * 50, '\n-> Trabalhando com o MongoDB \n' )
usr_2 = Usuario(mongodb)
usr_2.armazenar_dado('Eliel')
usr_2.remover_dado(20)