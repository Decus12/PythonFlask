from app import app
#render_template gives you access to Jinja2 template engine
from flask import render_template,request, make_response

@app.route('/')
def index():
    name = 'Hene'
    address='haakatu'
    response = make_response(render_template('index.html',name=name,title=address))
    response.headers.add('Cache-Control','no-cache')
    return response



@app.route('/user/<name>')
def user(user):
    return render_template('template_user.html',name=name)

#example how you can define route methods
@app.route('/user',methods=['GET','POST'])
def userParams():
    print(request.headers.get('User-agent'))
    name = request.args.get('name')
    return render_template('template_user.html',name=name)

#comment
"""multiline
comment"""