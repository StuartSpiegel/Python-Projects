import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import requests

''' 
Simple Web server application 
Stuart Spiegel 
'''
response = requests.get('http://sometestpage.com')
print("status code: " + response.status_code)
print("content length: " + response.headers['content-length'])
print(response.text)

status_code = 200
content_length = 64


# Handle a GET REQUEST
def do_GET(self):
    self.send_response(200)
    self.send_header("Content-Type", "text/html")
    self.send_header("Content-Length", str(len(self.Page())))
    self.end_headers()
    self.wfile.write(self.Page)


# ------------------------------------------------------------------------

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


# ----------------------------------------------------------------------------

def create_page(self):
    values = {
        'date_time': self.date_time.string(),
        'client_host': self.client_address[0],
        'client_port': self.client_address[1],
        'command': self.command,
        'path': self.path,
    }
    page = self.Page.format(**values)
    return page


def send_page(self, page):
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.send_header("Content-Length", str(len(page)))
    self.end_headers()
    self.wfile.write(page)


# Handle a static page and its resources
def do_GET(self):
    try:
        # Get the path of the requested object
        full_path = os.getcwd() + self.Path

        # The case that it does not exist
        if not os.path.exists(full_path):
            raise ServerException("'{0}' not found".format(self.path))

        # elif the object is a file
        elif os.path.isfile(full_path):
            self.handle_file(full_path)
        else:
            raise ServerException("Unknown Object '{0}'".format(self.path))

    # Handle an error
    except Exception as msg:
        self.handle_error(msg)


def handle_file(self, full_path):
    try:
        with open(full_path, 'rb') as reader:
            content = reader.read()
        self.send_content(content)
    except IOError as msg:
        self.handle_error(msg)

    Error_Page = '''\
    <html>
    <body>
    <h1>Error Accessing: {path}</h1>
    <p>(msg)</p>
    </body>
    </html>
    '''


# Serve an Error
def handle_error(self, msg):
    content_error = self.Error_Page.format(path=self.path, msg=msg)
    self.send_content(content_error)


# Handle an unknown object
def handle_error(self, msg):
    content = self.Error_Page.format(path=self, msg=msg)
    self.send_content(content, 404)


# Send the payload(bytes)
def send_content(self, content, status=200):
    self.send_response(status)
    self.send_header("Content-type", "text/html")
    self.send_header("Content-Length", str(len(content)))
    self.send_headers()
    self.wfile.write(content)
