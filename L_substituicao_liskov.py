'''
Aqui vamos tratar de exemplos que seguem o terceiro princípio do SOLID -> L - Princípio de Substituição de Liskov.

Resumindo: Esse princípio diz respeito a herança de classes e a medida que as classes vão hedando umas as outras e criando funções mais específicas, as açoes originais das classes herdadas devem permanecer inalterados, ao mesmo tempo que podem ser utilizados pelas classes que herdam as funcionalidades da classe mãe.
        ** Por isso é importante que uma classe "Mãe", seja mais genérica e a medida que classes que heram elas, vão afunilando e tornando suas ações mais específicas.

Para os exemplos, vamos seguir a seguinte linha de raciocínio:

1º -> Montar uma Classe simples para exemplificar o princípio de Liskov;
2º -> Demonstrar com essa classe, a QUEBRA do princípio de Liskov;
3º -> Montar uma estrutura de código para exemplificar o Princípio de Liskov de maneira mais didática.

Vamos ao Código:
'''

# 1º Exemplo -> Seguindo o Princípio de Liskov
class PrimeiraClasse:

    def __init__(self):
        pass

    def metodo_1(self):
        print('Esse é o Métodos Original!')


class SegundaClasse(PrimeiraClasse):

    def __init__(self):
        super().__init__()

    def metodo_1(self) -> str:
        return super().metodo_1()

'''
O Exemplo acima segue o princípo de Liskov, visto que o método herdado da PrimeiraClasse, não é Alterado na SegundaClasse e Funciona para a SegundaClasse, tranquilamente.
'''

# 2º Exemplo -> Quebrando o Princípo de Liskov
class PrimeiraClasse:

    def __init__(self) -> None:
        pass

    def metodo_1(self) -> None:
        print('Esse é o Métodos Original!')


class SegundaClasse(PrimeiraClasse):

    def __init__(self) -> None:
        super().__init__()

    def metodo_1(self) -> None:
        print('Esse é o Método Implementado na Segunda Classe!')

'''
O exemplo acima, QUEBRA o Princípio de Liskov, visto que o Metodo_1() da SegundaClasse, é alterado na implementação e não segue mais o comportamento original. E se outra classe herdam a SegundaClasse, também vai serguir alterando os métodos e assim se perder do princípio de Liskov.

<<<<<<< HEAD
<<<<<<< HEAD
Esse tipo de alteração no Código, depois de herdar uma classe mãe, é relacionado ao Polimorfismo das Classes. Outro Conceito de Orientação a Objetos.
=======
Esse tipo de alteração no Código depois de herdar uma classe mãe, é relacionado ao Polimorfismo das Classes. Outro Conceito de Orientação a Objetos.
>>>>>>> 43fed14c1594ab07fa27d7aa0560e5c104c883b1
=======
Esse tipo de alteração no Código, depois de herdar uma classe mãe, é relacionado ao Polimorfismo das Classes. Outro Conceito de Orientação a Objetos.
>>>>>>> 9859810 (Código 3ºPrinc SOLID - Subistituição de Liskov.)
'''


# Para o próximo exemplo, vamos ver classes que interagem entre si e seguem o princípo de Liskov.

# Os métodos teram prints, para título de exemplificação, e não uma implementação real de código.

# 3º Exemplo -> Princípio de Liskov

from typing import Type

class Animal:

    def __init__(self):
        pass

    def comer(self) -> None:
        print('O Animal Está Comendo!')

    def andar(self) -> None:
        print('O Animal Está Andando!')

    def dormir(self) -> None:
        print('O Animal Está Dormindo!')


class Lobo(Animal):

    def __init__(self):
        super().__init__()

    def uivar(self) -> None:
        print('O Lobo Está Uivando!')


class Ave(Animal):

    def __init__(self):
        super().__init__()

    def cantar(self) -> None:
        print('A Ave Está Cantando!')

class Pinguim(Ave):

    def __init__(self):
        super().__init__()

    def nadar(self):
        print('O Piguim Está Nadando!')

class Falcao(Ave):

    def __init__(self):
        super().__init__()

    def voar(self) -> None:
        print('O Falcão Está Voando!')

class Pessoa:
    
    def __init__(self, nome: str) -> None:
       self.nome = nome

    def observar(self, animal: Type[Lobo]) -> None:
        animal.uivar()
        animal.comer()
        animal.andar()
        animal.dormir()


# Instanciando as Classes e rodando o Programa
animal = Animal()
lobo = Lobo()
ave = Ave()
pinguim = Pinguim()
falcao = Falcao()

eliel = Pessoa('Eliel')
eliel.observar(lobo)

'''
E Aqui vemos o Exemplo do Princípo de Liskov funcionando. =)

    Se mudar o tipo do animal no método observar() na Classe Pessoa, ainda assim, vamos poder usar os métodos de comer, andar, dormir, enquanto podemos também usar os métodos uivar, para o Lobo, cantar, para Ave, nadar para pinguim e etc.

    Ou seja, as classes ficam intercabiáveis entre si sem prejudicar o funcionamento de nenhuma delas e principalmente, sem causar problemas ou confitos com a classe principal que é a Animal.
'''