def app(environ, start_response):
	status = '200 OK'
	output = 'HELLO WORLD: \n'

	requestmethod = environ.get('REQUEST_METHOD')
	output += (requestmethod + '\n')

	if requestmethod == "GET":
		querystring = environ.get('QUERY_STRING')
		params = querystring.split("&")
		for i in params:
			output += "%s\n" % ( i )
	elif requestmethod == "POST":
		length = int(environ.get('CONTENT_LENGTH',0))
		if length !=0:
			querystring = environ['wsgi.input'].read(length)
			params = querystring.split("&")
		for i in params:
			output += "%s\n" % ( i )
	response_headers = [('Content-type', 'text/plain'), ('Context-Length', str(len(output)))]
	start_response(status, response_headers)
	return (output)
