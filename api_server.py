from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_command_line



class LoginHander(RequestHandler):
    def get(self):
        self.write('<h3>get 请求</3>')

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


def make_app():
    return Application(
        handlers=[
            ('/login', LoginHander)
        ], default_host=options.h)


if __name__ == '__main__':
    define('p', default=8000, type=int, help='绑定的端口')
    define('h', default='localhost', type=str, help='绑定的主机')

    parse_command_line()
    app = make_app()
    app.listen(options.p)
    IOLoop.current().start()
