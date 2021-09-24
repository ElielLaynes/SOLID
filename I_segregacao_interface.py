'''
Nesses exemplos vamos falar do 4º princípio do SOLID -> Segregação de Interface.

Resumo do Princípio:  Uma classe não deve ser forçada a implementar interfaces e métodos que não irão utilizar.

Aqui, vamos abordar exemplos que forçam a implementação de métodos, mesmo ele sendo dispesável para a classe e outro seguindo o princípo da segregação de interface.

Vamos utlizar o conceito de animais que fazem parte do grupo de aves e dessas, vamos ter as que voam e as que não voam.

1º -> Criar uma classe que não segue os princípios da segregação de classes.
2º -. Refatorar esse conjunto de código para adequar ao Princípio da seguregação de classes.
'''
from abc import ABC, abstractmethod


# 1º Exemplo -> Impementando interface de Classe sem seguir o Princípio da Segregação de Interfaces.
class AvesInterface(ABC):

    @abstractmethod
    def comer(self) -> None:
        print('A Ave está Comendo!')
        raise NotImplementedError
    

    @abstractmethod
    def voar(self) -> None:
        print('A Ave está Voando!')
        raise NotImplementedError
    

    @abstractmethod
    def cantar(self) -> None:
        print('A Ave está Cantando!')
        raise NotImplementedError



class Canarinho(AvesInterface):

    def comer(self) -> None:
        print('A Ave está Comendo!')
    

    def voar(self) -> None:
        print('A Ave está Voando!')
    

    def cantar(self) -> None:
        print('A Ave está Cantando!')



class Pinguim(AvesInterface):

    def comer(self) -> None:
        print('A Ave está Comendo!')
    

    def voar(self) -> None:
        return None
    

    def cantar(self) -> None:
        print('A Ave está Cantando!')
'''
Como a Classe Aves é uma classe apenas com métodos abstratos, as classes que herdam dela, precisam obrigatoriamente implementar os métodos contidos na Classe Aves. Se isso não acontecer vai levantar um ERRO e não vai rodar o código.

Como Pinguim é uma Ave que não voa, precisou implementaro o métodos voar() retornando None. E isso nem de longe é o ideal, porque deixa o código sujo e com métodos inutilizaveis.

No exemplo a seguir, vamos corrigir isso com a Segregação de interfaces.
'''

# 2º Exemplo -> Impementando as interfaces seguindo o Princípio da Segregação de Interfaces.
class AvesInterface(ABC):

    @abstractmethod
    def comer(self) -> None:
        print('A Ave está Comendo!')
        raise NotImplementedError
    

    @abstractmethod
    def cantar(self) -> None:
        print('A Ave está Cantando!')
        raise NotImplementedError



class AvesQueVoamInterface(ABC):

    @abstractmethod
    def comer(self) -> None:
        print('A Ave está Comendo!')
        raise NotImplementedError


    @abstractmethod
    def voar(self) -> None:
        print('A Ave está Voando!')
        raise NotImplementedError


    @abstractmethod
    def cantar(self) -> None:
        print('A Ave está Cantando!')
        raise NotImplementedError



class Canarinho(AvesQueVoamInterface):

    def comer(self) -> None:
        print('A Ave está Comendo!')
    

    def voar(self) -> None:
        print('A Ave está Voando!')
    

    def cantar(self) -> None:
        print('A Ave está Cantando!')



class Pinguim(AvesInterface):

    def comer(self) -> None:
        print('A Ave está Comendo!')
    

    def cantar(self) -> None:
        print('A Ave está Cantando!')
'''
Agora, no exemplo acima, adequados as classes ao contexto de Segregação de Interfaces. Visto que separamos uma interface genérica para todas as Aves e uma mais específica para as Aves que Voam. Dessa forma, a Classe Canarinho, implementa todos os métodos da Interface AvesQueVoam e a Classe Pinguim, implementa os métodos da classe Aves.
'''

# ---- Instanciando e demonstrando o programa genérico construído funcionando ----

# Instanciando as Classes
canarinho = Canarinho()
pinguim = Pinguim()

# Chamando os métodos
print('\n', '-' * 50, '\n Métodos do Canarinho \n')
canarinho.comer()
canarinho.cantar()
canarinho.voar()

print('\n', '-' * 50, '\n Métodos do Pinguim \n')
pinguim.comer()
pinguim.cantar()
