from gevent.pywsgi import WSGIServer


def hello(environ, start_response):
    if(environ['PATH_INFO'] == '/' and environ['REQUEST_METHOD'] == 'GET'):
        status = '200 OK'
        text = "Hello world!"
    else:
        status = '404 Not Found'
        text = "Not Found"

    body = text.encode('utf-8')
    response_headers = [
        ('Content-type', 'text/plain; charset=utf-8'),
        ('Content-Length', str(len(body)))]
    start_response(status, response_headers)
    return [body]


WSGIServer(('0.0.0.0', 8080), hello, log=None).serve_forever()
