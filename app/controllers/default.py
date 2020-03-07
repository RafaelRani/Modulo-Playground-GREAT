from flask import Flask, url_for, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
import json, random
from app import app
from app.models.User import User


@app.route("/playground")
def playground():
	if not session.get('logged_in'):
		return redirect(url_for('home'))
	else:
		# obter as disciplinas, tópicos e questionários disponíveis no arquivo 'disciplina-topicos-questionarios.json'
		quiz = json.loads(open('app/static/json/disciplinas-topicos-questionarios.json').read())
		# obter o nome de usuário da sessão atual
		user = session['user']
		# renderizar as informações obtidas no templete 'menu.html'
		return render_template("menu.html", quiz=quiz, user=user)

@app.route("/questionario/<string:idQuiz>")
def returnQuiz(idQuiz):
	if not session.get('logged_in'):
		return redirect(url_for('home'))
	else:
		# fazendo uma requisição remota à API do GREAT para obter as perguntas do questionário escolhido
		'''
		# fazendo uma requisição para obter o json do quiz de id informado (5bfac4715931000fa515341e):
		response = requests.get("http://200.137.131.118/classroom/api/tests/5bfac4715931000fa515341e/")
		if response.status_code != 200:
			resp = "A aplicação não pode obter os dados do servidor"
		quiz = json.loads(response.content)
		'''
		# fazendo a leitura do arquivo json do questionário escolhido para obter as perguntas do mesmo
		quiz = json.loads(open('app/static/json/' + idQuiz + '.json').read())
		# obtendo o número de questões do questionário
		numQuestions = len(quiz['questions'])
		# embaralhando a ordem de impressão das alternativas em cada questão:
		for i in quiz['questions']:
			random.shuffle(i['choices'])
		user = session['user']
		return render_template("quizz.html", quiz=quiz, user=user, numQuestions=numQuestions)

	
@app.route("/respostas/<int:iD>", methods=['GET', 'POST'])
def resposta(iD):
	if not session.get('logged_in'):
		return redirect(url_for('home'))
	else:
		iD = int(iD)
		cont = 0
		listResp = []
		if not session.get('logged_in'):
			return redirect(url_for('home'))
		else:
			user = session['user']
			quiz = json.loads(open('app/static/json/' + str(iD) + '.json').read())
			numQ = len(quiz['questions'])
			for i in range (0,numQ):
				# variável resp recebe do formulário o valor alti em string
				resp = (request.form.get("alt" + str(i)))
				listResp.append(resp)
				# se resp for igual ao correctAnswer correspondente: o contador de acertos incrementa
				if quiz['questions'][i]['correctAnswer'] == resp:
					cont += 1
			# se resp recebeu algo:
			if resp:
				return render_template("resposta.html", iD=iD, cont=cont, user=user, respostas=listResp)
				print(listResp)
			# caso as duas condições (if) não forem satisfeitas a função redireciona
			# de volta a função exercicio
			else:
				return redirect(url_for('.returnQuiz', iD))
			