# Modulo-Playground-GREAT
<h3>Projeto de Monografia do Curso de Ciência da Computação</h3><br>
<h4>Módulo Playground da ferramenta de criação de jogos educacionais, GREAT.</h4><br>
<h4>Features:</h4><br>
- Cadastro de usuários;<br>
- Login;<br>
- Exibição de disciplinas, tópicos, questionários e perguntas cadastradas no sistema;<br>
- Permite ao usuário responder as perguntas e enviar as respostas;<br>
- Exibição do relatório ao final do questiónario contendo o número de acertos e respostas de cada pergunta.

# Como rodar a aplicação

1. Criar a máquina virtual:<br>
	$ virtualenv -p python venv
	
2. Ativar a máquina virtual:<br>
	$ cd venv/Scripts<br>
	$ activate  (no windows)<br>
  <br>
  $ source venv/bin/activate (no linux)
	
3. Voltar para o diretório do projeto:<br>
	$ cd ../..
	
4. Instalar as bibliotecas necessárias para a aplicação:<br>
	$ pip install -r requirements.txt
	
5. Rodar a aplicação:<br>
	$ python run.py
	
## OBS: A aplicação faz a leitura do arquivo 'disciplinas-topicos-questionarios.json' simulando o consumo de uma API, para fins de teste.
