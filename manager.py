import tornado.web
import tornado.ioloop
import tornado.options
from tornado.httputil import HTTPServerRequest


class IndexHander(tornado.web.RequestHandler):
    def get(self):
        ww = self.get_argument('ww')
        print(ww)
        title = self.get_arguments('title')
        print(title)
        ww2 = self.get_query_argument('ww')
        print(ww2)
        title2 = self.get_query_arguments('title')
        print(title2)
        req: HTTPServerRequest = self.request
        ww3 = req.arguments.get('ww')
        print(ww3)
        self.write('<h3>我是主页</h3>')

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


def make_app():
    return tornado.web.Application([
        ('/', IndexHander)
    ], default_host=tornado.options.options.host)


if __name__ == '__main__':
    tornado.options.define('port', default=8000, type=int, help='bind socket port')

    tornado.options.define('host', default='localhost', type=str, help='设置host name')
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(tornado.options.options.port)

    print('启动服务%s：%s' % (
        tornado.options.options.host,
        tornado.options.options.port
    ))
    tornado.ioloop.IOLoop.current().start()


