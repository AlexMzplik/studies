# -*- coding: UTF-8 -*-
def coroutine_decorator(func):
    def wrapper(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return wrapper

@coroutine_decorator
def counter(string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item, str):
                if item in string:
                    count += 1
                    print item
                else:
                    print 'Não encontrado'
            else:
                print 'Não é uma string'
    except GeneratorExit:
        print count


coroutine = counter('Python é bem diferente de Javascript')
coroutine.send('ana')
coroutine.send(3)
coroutine.send('ad')
coroutine.send('Java')