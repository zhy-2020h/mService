from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler


class IndexHander(RequestHandler):
    def get(self):
        self.write('<h3>Hello, Tronado</h3>')


if __name__ == '__main__':
    app = Application([
        ('/', IndexHander)
    ])
    app.listen(7000)

    IOLoop.current().start()
