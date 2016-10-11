from http.server import BaseHTTPRequestHandler,HTTPServer
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

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
				output += "<html><body>Hello!"
				output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
				output += "</body></html>"
				self.wfile.write(bytes(output, 'utf-8'))
				print(output)
				return			
			if self.path.endswith("/hola"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>&#161Hola!<a href=\"hello\">Back to hello!<a/>"
				output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
				output += "</body></html>"
				self.wfile.write(bytes(output, 'utf-8'))
				print(output)
				return

			if self.path.endswith("/restaurants"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = ""
				output += "<html><body>"
				output += "<h1>&#161 Hola !</h1>"
				
				restaurants = session.query(Restaurant).all()
				for i in restaurants:
					output += '<div>'
					output += i.name
					output += '</div>'               
				output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
				output += "</body></html>"
				self.wfile.write(bytes(output, 'utf-8'))
				print(output)
				return

		except IOError:
			self.send_error(404, "File not found {}".format(self.path))

	def do_POST(self):
		self.send_response(301)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		#you have to replace .getheader() method by .get() method because in Python 3 method getheader() was deleted.
		ctype, pdict = cgi.parse_header(
		    self.headers.get('content-type'))
		#python3 need this parameter converted to bytes.
		pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
		if ctype == 'multipart/form-data':
		    fields = cgi.parse_multipart(self.rfile, pdict)
		    messagecontent = fields.get('message')
		output = ""
		output += "<html><body>"
		output += " <h2> Okay, how about this: </h2>"
		output += "<h1> %s </h1>" % messagecontent[0]
		output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
		output += "</body></html>"
		self.wfile.write(bytes(output, 'utf-8'))
		print(output)

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
		server.socket.close()

if __name__ == '__main__':
	main()