import urlparse
import cgi
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cookielib
import Cookie

# http://pymotw.com/2/BaseHTTPServer/
class GetHandler(BaseHTTPRequestHandler):
    def do_GET_chunked(self, filename, contentType, responseCode):
	self.send_response(responseCode)
	self.send_header('Content-Type', contentType)
        self.send_header('Last-Modified', 'Sun, 13 Feb 2022 03:14:06 GMT')
        self.send_header('Transfer-Encoding', 'chunked')
	self.end_headers()
	print("chunked!!")
	print(filename)
	with open(filename, 'rb') as file: 
            file_contents = file.read();
            r = file_contents.encode('utf-8')
            l = len(r)
            formatted_contents = '{:X}\r\n{}\r\n'.format(l, r).encode('utf-8');
            print(formatted_contents)
            self.wfile.write(formatted_contents)
            
        return   
 
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        filename = parsed_path.path[1:]
	queryDict = dict(urlparse.parse_qsl(parsed_path.query))
	contentType = 'text/plain'
        responseCode = 200	
        location = None
	cookie = Cookie.SimpleCookie()
	cookieString = None
	customHeaderString = None

        if 'contenttype' in queryDict:
	    contentType = queryDict['contenttype']
	if 'cookie' in queryDict:
	    cookieString = queryDict['cookie']
	if 'header' in queryDict:
	    customHeaderString = queryDict['header']
	if 'responsecode' in queryDict:
            responseCode = int(queryDict['responsecode']);
        if 'redirect' in queryDict:
            responseCode = 301
            location = queryDict['redirect']
        if 'chunked' in queryDict and queryDict['chunked'] == '1':
    	    print("chunked!")
	    self.do_GET_chunked(filename, contentType, responseCode)
	    return

        #handle non-chunked requests
        self.send_response(responseCode)
	if cookieString != None:
	    self.send_header("Set-Cookie", cookieString)
	if customHeaderString != None:
	    headerKeyValue = customHeaderString.split(':')
	    self.send_header(headerKeyValue[0], headerKeyValue[1])
        if location != None:
            self.send_header("Location", location)
        self.send_header('Content-Type', contentType)
        self.send_header('Last-Modified', 'Sun, 13 Feb 2022 03:14:06 GMT')
#	self.end_headers()
        with open(parsed_path.path[1:], 'rb') as file:
            contents = file.read();
            self.send_header('Content-Length', len(contents))
	    self.end_headers()
	    self.wfile.write(contents);
        return

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
