#-*-encoding=UTF-8 -*-
from flask import Flask,render_template,request,make_response,redirect

app = Flask(__name__) #定义一个应用
app.jinja_env.line_statement_prefix='#' #设置jinja2行表达式

@app.route('/')#是一个装饰器，如果我访问的地址是/helloworld这个函数来处理
def hello_world():#首页
    return 'Hello World!'
#后面不加/，输入是浏览器是会出错。
@app.route('/profile/<uid>/',methods=['GET','POST'])#访问胡URL:127.0.0.1:5000/profile1/google/,google为uid,请求支持get和POST方法
def profile(uid):
    return 'profile:'+uid

@app.route('/profile1/<int:uid>/')#设置ID为int型
def profile1(uid):
    return 'profile:'+str(uid)

@app.route('/profile2/<uid>/',methods=['GET','POST'])#访问胡URL:127.0.0.1:5000/profile1/google/,google为uid,请求支持get和POST方法
def profile2(uid):
    colors=['geen','red','bule']
    infos={'name':'wshe','ID':'google'}
    return render_template('profile.html',uid=uid,colors=colors,infos=infos)#调用template,传入uid
@app.route('/request')
def resquest_demo():
    key=request.args.get('key','defaultkey')#获得key
    res=request.args.get('key','defaultkey')
    res=res+request.url+'+++'+request.path+'<br>'

    for property in dir(request):
        res=res+str(property)+'<br>'+str(eval('request.'+property))+'<br>'
        #res = res + str(property) + '<br>' + str(request.property)#error
    response = make_response(res)
    response.set_cookie('ID',key)
    response.status='200'
    response.headers['ID']='heoll world'#信息隐藏在头部
    return response

@app.route('/newpath')
def newpath():
    return 'hello newpath'

@app.route('/re/<int:code>')#重定向，到newpath,code:301 or 302
def redirect_demo(code):
    return redirect('/newpath',code=code)
#当找不到url是发生404.，捕获404跳转到指定的页面。
@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html',url=request.url),404

@app.errorhandler(400)
def exception_page(error):
    response=make_response('error.....!')
    return response

@app.route('/admin')
def admin():
    if request.args['key']=='admin':
        return 'hello admin'
    else:
        raise Exception()#没有解决这个问题。

if __name__ == '__main__':
    app.run(debug=True) #
