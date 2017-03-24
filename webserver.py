from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
logging.basicConfig(level=logging.DEBUG)


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            output = ""
            output += "<html><body>Hello!</body></html>"
            self.wfile.write(output.encode())
            logging.debug(output)
            return
        else:
            self.send_response(404, "File Not Found: {}".format(self.path))
            return


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        logging.info("Web server running on port: {}".format(port))
        server.serve_forever()

    except KeyboardInterrupt:
        logging.info("Stopping web server")
        server.socket.close()

if __name__ == '__main__':
    main()
