from flask import Flask,render_template,request,session,redirect
from flask_app import app
from flask_app.models import adventurer,user

@app.route('/home')
def home():
    data = {
        'id':session['user_id']
    }
    return render_template ('home.html',user = user.User.get_by_id(data),adventurers=adventurer.Adventurer.getAll())

@app.route('/create')
def create():
    if 'user_id' not in session:
        return redirect('/')
    data = { 'id':session['user_id']}
    return render_template('createAdventurer.html',user=user.User.get_by_id(data))

@app.route('/createadventurer', methods = ['POST'])
def createAdventurer():
    if 'user_id' not in session:
        return redirect('/')
    user_id = session['user_id']
    data={
        "name":request.form['name'],
        "age":request.form['age'],
        "race":request.form['race'],
        "weapon":request.form['weapon'],
        'user_id':user_id
    }
    adventurer.Adventurer.save(data)
    return redirect('/home')

@app.route('/editadventurer/<int:id>', methods = ['POST'])
def editAdventurer(id):
    if 'user_id' not in session:
        return redirect('/')
    if not adventurer.Adventurer.validate_adventurer(request.form):
        return redirect(f'/edit/{id}')
    data={
        "name":request.form['name'],
        "age":request.form['age'],
        "race":request.form['race'],
        "weapon":request.form['weapon'],
        "id":id
    }
    adventurer.Adventurer.update(data)
    return redirect('/myadventurers')


@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        "id":id
    }
    return render_template('editAdventurer.html',adventurer = adventurer.Adventurer.getById(data))


@app.route('/myadventurers')
def myAdventures():
    if 'user_id' not in session:
        return redirect('/')
    Userdata = { 'id':session['user_id']}
    adventurerData = {'user_id':session['user_id']}
    return render_template('myAdventurers.html',user=user.User.get_by_id(Userdata),adventurers=adventurer.Adventurer.getByUserId(adventurerData))

@app.route("/journey/<int:id>")
def journeystart(id):
    if 'user_id' not in session:
        return redirect('/')
    session['adventurer_id']=id
    return render_template('journeystart.html',adventurer= adventurer.Adventurer.getById({'id':id}))

@app.route('/delete/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/')
    adventurer.Adventurer.delete({'id':id})
    return redirect('/home')

@app.route("/tavern/<int:id>")
def tavern(id):
    if 'user_id' not in session:
        return redirect('/')
    session['adventurer_id']=id
    return render_template('tavern.html',adventurer= adventurer.Adventurer.getById({'id':id}))

@app.route("/stealfood/<int:id>")
def stealfood(id):
    if 'user_id' not in session:
        return redirect('/')
    session['adventurer_id']=id
    return render_template('stealfood.html',adventurer= adventurer.Adventurer.getById({'id':id}))

@app.route("/stuffed/<int:id>")
def stuffed(id):
    if 'user_id' not in session:
        return redirect('/')
    session['adventurer_id']=id
    return render_template('stuffed.html',adventurer= adventurer.Adventurer.getById({'id':id}))

@app.route("/starlight/<int:id>")
def starlight(id):
    if 'user_id' not in session:
        return redirect('/')
    session['adventurer_id']=id
    return render_template('starlight.html',adventurer= adventurer.Adventurer.getById({'id':id}))

@app.route("/leavetown/<int:id>")
def leavetown(id):
    if 'user_id' not in session:
        return redirect('/')
    session['adventurer_id']=id
    return render_template('leavetown.html',adventurer= adventurer.Adventurer.getById({'id':id}))

@app.route("/cellar/<int:id>")
def tavernstart(id):
    if 'user_id' not in session:
        return redirect('/')
    session['adventurer_id']=id
    return render_template('cellar.html',adventurer= adventurer.Adventurer.getById({'id':id}))
