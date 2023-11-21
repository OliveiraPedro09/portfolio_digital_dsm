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
        {'titulo' : 'TRABALHO ACADÊMICO API FATEC-SJC', 'conteudo' : 'Metodologia', 'paragrafo' : 'SCRUM - O que é o Scrum? O Scrum é um framework de gerenciamento que as equipes usam para se auto-organizar e trabalhar em direção a um objetivo em comum. A estrutura descreve um conjunto de reuniões, ferramentas e funções para uma entrega eficiente de projetos.' },
        {'titulo1' : 'Sobre o Projeto', 'conteudo1' : 'Estou atualmente desenvolvendo com a minha equipe Code Nine um projeto onde devemos fazer um site informativo sobre nefrologia infantil, um assunto que é pouco abordado na sociedade brasileira.', 'paragrafo1' : 'Esse projeto foi desenvolvido com a finalidade de conscientizar, ampliar e facilitar a comunicação de pacientes e famílias que possuem Doença renal crônica(DRC).', },
        {'titulo2' : 'Oque é DRC ?', 'conteudo2': 'É uma doença de curso pronlongado, que pode parecer benigno, porém, na maioria das vezes se torna grave, além de ser uma doença silenciosa.'},
        {'titulo3' : 'Fatores de Risco:', 'conteudo3': 'Um dos principais fatores de risco para doença renal crônica é a diabetes e a hipertensão, ambas cuidadas na Atenção Básica, principal porta de entrada para o Sistema Único de Saúde (SUS), em uma das 42.885 Unidades Básicas de Saúde distribuídas em todo o Brasil.'}
        ]
    return render_template('trabalhos.html', trabalho = trabalho)

if __name__ == "__main__":
    app.run(debug=True)
