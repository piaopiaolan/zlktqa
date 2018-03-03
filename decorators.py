from functools import wraps
from flask import session,url_for,redirect
#登录限制装饰器
def login_required(func):
    @wraps(func)
    def wrappper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrappper
