from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from zlktqa import app
from exts import db
from models import User,Question,Answer

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

#然后进入venv 的scripts 激活 虚拟环境，退出到manage.py 的文件路径 ，
#使用 python manage.py db inti (生成migrations文件夹)
#python manage.py db migrate
#python manage.py db upgrade
#h后续更改了模型只需要migrate和upgrade即可

if __name__ == '__main__':
    manager.run()



