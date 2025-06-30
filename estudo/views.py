from estudo import app, db
from flask import render_template, url_for, request, redirect

from estudo.models import Contato
from estudo.forms import ContatoForm

@app.route("/")
def homepage():
    usuario = 'Jonathas'
    idade = 34

    context = {
        'usuario': usuario,
        'idade': idade
    }
    return render_template("index.html", context=context)

@app.route("/contato/", methods=["GET", "POST"])
def contato():
    context = {}
    form = ContatoForm()
    
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
        
    return render_template('contato.html', form=form)

@app.route("/contato/lista")
def contatoLista():
    pesquisa = request.args.get('pesquisa', '')

    dados = Contato.query.order_by(Contato.nome)
    if pesquisa:
        dados = dados.filter(Contato.nome.ilike(f'%{pesquisa}%'))
    context = {'dados': dados.all()}
    
    return render_template('contato_lista.html', context=context)

@app.route('/contato/<int:id>/')
def contatoDetail(id):
    obj = Contato.query.get(id)

    return render_template('contatoDetail.html', obj=obj)

