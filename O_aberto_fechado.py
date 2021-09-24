'''
Nesse exemplo, vamos tratar do segundo princíprio SOLID -> O - Princípio Aberto/Fechado. Esse princípio em resumo, diz que uma classe deve ser fechada para Mudanças/alterações, mas aberta para Extesão de funcionalidades.

1º -> Será crida uma classe levando em conta a Responsabilidade Única, porém, seguindo apenas o conceito Fechado de Classe.
2º -> Essa classe será refatorada para poder ser extendida e atender os critérios de uma classe Aberta/Fechada.
'''

class Palco:
    
    def show(self, tipo_show):
        if tipo_show == 1:
            self._cantor()
        if tipo_show == 2:
            self._comediante()

    def _cantor(self):
        print('Cantor(a) Está Apresentando Seu Show!')

    def _comediante(self):
        print('Comediante Está Apresentando Seu Show!')
    
'''
A Classe acima, leva em conta o princípio da Responsabilidade Única, porém, é uma classe Fechada, ou seja, aceita apenas tipos de shows pré definidos e caso seja necessário acrescentar mais tipos de shows, é necessário alterar a estrutura da classe, o que não é recomendado e nem sustentável para um programa maior.

O ideal é que essa classe pudesse receber n tipos de shows sem que fosse necessários alterar a estrura da classe.

Para poder adequar a classe ao princípio Aberto/Fechado, ela será refatorada e exemplificada abaixo:
'''

class NovoPalco:

    def show(self, dono_do_show: any):
        dono_do_show.apresentar_show()


class Cantor:

    def apresentar_show(self):
        print('O Cantor(a), Está Apresentando Seu Show de Música!')


class Comediante:

    def apresentar_show(self):
        print('O(a) Comediante, Está Apresentando Seu Show de Stand-up!')


class Palestrante:

    def apresentar_show(self):
        print('O(a) Palestrante, Está Apresentando sua Palestra!')


# Instanciando as Classes
cantora = Cantor()
comediante = Comediante()
palestra = Palestrante()

palco = NovoPalco()

# Utlizando a instancia da classe Palco para cada tipo de apresentação.
palco.show(palestra)
palco.show(comediante)
palco.show(cantora)

'''
Agora, a classe NovoPalco, está de acordo com o princípio Aberto/Fechado.

Abaixo, seguem OBSERVAÇÕES IMPORTANTES:

     1ª -> Na classe NovoPalco, é usada a tipagem ANY para dono_do_show. Isso faz com que essa classe agora, possa receber qualquer tipo de show e possa apresentá-lo no Palco.


     2ª -> O método apresentar_show(), obrigatóriamente, precisa ser implementado em cada classe nova para poder funcionar. Caso não seja implementado ou implementado com nome diferente, vai gera ERRO e não funcionara.
     Esse é um conceito presente em classes e métodos abstratos, que devem ser sempre implementados em classes que herdam classes abstratas por padrão.


    3ª -> Mesmo estando com confirmidada com o S e O do SOLID, ou seja, princípios da reponsabilidade única e aberto/fechado, essa classe ainda demonstra uma falha, que é a obrigatoriedade da implementação do método apresentar_show().
        ** O ideal, seria que para essa classe, tivéssemos uma INTERFACE, e atráves dessa interface, outras classes se conectacem aos métodos necessários para utilização e apresentação dos shows.
        
            *** Vamos abordar o conceito de interface em outros exemplos e nos outros príncípios e isso vai ficar expliícito em sua utilização. No momento, vamos manter para esse exemplo, apenas responsabilidade única e Aberto/Fechado.
'''