from http.server import BaseHTTPRequestHandler,HTTPServer

# This class will handle any incoming request from
# a browser 
class webserverHandler(BaseHTTPRequestHandler):
	# Handler for the GET requests
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>Hello!</body></html>"
				self.wfile.write(bytes(output, 'utf-8'))
				print(output)
				return			
			if self.path.endswith("/hola"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>&#161Hola!<a href=\"hello\">Back to hello!<a/></body></html>"
				self.wfile.write(bytes(output, 'utf-8'))
				print(output)
				return
		except IOError:
			self.send_error(404, "File not found %s" % self.path)


def main():
	# Create a web server and define the handler to manage the
    # incoming request
	try:
		port = 8080
		server = HTTPServer(('', port), webserverHandler)
		print("Web server running on port %s" % port)
		server.serve_forever()

	except KeyboardInterrupt:
		print("^C entered, stopping web server...")
		server.socet.close()

if __name__ == '__main__':
	main()