#!/usr/bin/env python

from cgi import parse_qs
from lib import basreng,cilok,sampeu

def application(environ, start_response):
	## passing environ uwsgi PARAM
	try:
		request_body_size = int(environ.get('CONTENT_LENGTH', 0))
	except (ValueError):
		request_body_size = 0
	origin = environ['REQUEST_URI']
	request_body = environ['wsgi.input'].read(request_body_size)
	post = parse_qs(request_body)
	## Menu Logic
	url=cilok.urlDecode16(origin[1:])
	uri=url.split('%')
	if sampeu.getMenu(uri[0])=="key":
		mod = 'apps.controllers.'+uri[1]
		func = uri[2]
		a = __import__(mod,fromlist=['Controller'])
		b = getattr(a,'Controller')()
		rep=getattr(b,func)(uri[3])
		text = sampeu.getHtml(uri[1])
		
		result = basreng.dictView(rep,text)

		hbegin = sampeu.getHtmlBegin()
		hend = sampeu.getHtmlEnd()

		respon = hbegin + result + hend
	elif sampeu.getMenu(uri[0])=="token":
		mod = 'apps.api.'+uri[1]
		func = uri[2]
		a = __import__(mod,fromlist=['Api'])
		b = getattr(a,'Api')()
		respon = getattr(b,func)(uri[3],post)
	else:
		respon = """
		<html>
		<head><title>403 Porbidden</title></head>
		<body bgcolor="white">
		<center><h1>403 Porbidden</h1></center>
		<hr><center>peuyeum/bdg</center>
		</body>
		</html>
		"""
	## Passing HTML to client
	start_response('200 OK', [('Content-Type', 'text/html'),('Content-Length', str(len(respon)))])
	return [respon]

