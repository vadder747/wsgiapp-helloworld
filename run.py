from datetime import datetime
import sys
import os

def app(environ, start_response):  
  data = '\n'.join(get_data(environ))
  data = data.encode(encoding='UTF-8')
  status = '200 OK'
  response_headers = [
      ('Content-type', 'text/plain'),
      ('Content-Length', str(len(data)))
  ]
  start_response(status, response_headers)
  return iter([data])

def get_data(environ):
  now = datetime.now()
  data = []
  data.append('Hello, World!')
  data.append(environ.get('HTTP_HOST'))
  data.append(now.strftime('%d/%m/%Y %H:%M:%S')) # dd/mm/YY H:M:S
  data.append('\n')
  data.append(syspath_dump())
  data.append('\n')
  data.append(osenviron_dump())
  data.append('\n')
  data.append(environ_dump(environ))
  return data

def syspath_dump():
  res = 'sys.path=[\n'
  res += "    "+"\n    ".join(sys.path)
  res += '\n]'
  return res

def osenviron_dump():
  res = 'os.environ={\n'
  for k, v in os.environ.items():
    res += f'    {k}: {v}\n'
  res += '}'
  return res

def environ_dump(environ):
  res = 'environ={\n'
  for k, v in environ.items():
    res += f'    {k}: {v}\n'
  res += '}'
  return res
