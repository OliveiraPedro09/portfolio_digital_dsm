from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/trabalhos')
def trabalhos():
    trabalho = [
        {'titulo' : 'TRABALHO ACADÊMICO API FATEC-SJC 1º DSM', 'conteudo' : 'Metodologia', 'paragrafo' : 'SCRUM - O que é o Scrum? O Scrum é um framework de gerenciamento que as equipes usam para se auto-organizar e trabalhar em direção a um objetivo em comum. A estrutura descreve um conjunto de reuniões, ferramentas e funções para uma entrega eficiente de projetos.' },
        {'titulo1' : 'Sobre o Projeto', 'conteudo1' : 'Estou atualmente desenvolvendo com a minha equipe Code Nine um projeto onde devemos fazer um site informativo sobre nefrologia infantil, um assunto que é pouco abordado na sociedade brasileira.', 'paragrafo1' : 'Esse projeto foi desenvolvido com a finalidade de conscientizar, ampliar e facilitar a comunicação de pacientes e famílias que possuem Doença renal crônica(DRC).', },
        {'titulo2' : 'TRABALHO ACADÊMICO API FATEC-SJC 2º DSM', 'conteudo2': 'Desenvolvimento de um sistema de atendimento direcionado a uma empresa de transportes e fretes'},
        {'titulo3' : 'Sobre o Projeto', 'conteudo3': 'O projeto foi executando usando React Typescript, visando criar um site para atendimentos de uma empresa de entregas conectando o cliente, atendente e empresa. Possui um sitema de chat e tickets onde o atendente consegue se conectar de forma eficiênte ao cliente.'}
        ]
    return render_template('trabalhos.html', trabalho = trabalho)

if __name__ == "__main__":
    app.run(debug=True)
