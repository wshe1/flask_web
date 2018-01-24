#-*-encoding=UTF-8 -*-
from flask_script import Manager
from flask_web import app

manager=Manager(app) #通过命令行启动服务器

@manager.option('-n','--name',dest='name',default='wshe')#添加命令的参数
def hello(name):
    print 'hello',name

@manager.command #定义自己的相关的命令。
def initialize_database():
    'initialize database'
    print 'database ...'
if __name__=='__main__':
    manager.run()