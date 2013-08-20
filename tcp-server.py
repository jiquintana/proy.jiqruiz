#!/usr/bin/python
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
	print(repr(self.request))

application = tornado.web.Application([
    (r"/", MainHandler),
])



def main():

    server = ProxyServer
    application.listen(8888, address='127.0.0.1')

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__": main()
