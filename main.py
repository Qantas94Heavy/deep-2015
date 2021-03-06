import web, mimetypes, re, os
import generate_poem
        
urls = (
  '/poem', 'poem',
  '/(.*)', 'other'
)

class poem:        
  def GET(self):
    type = web.input().type
    if type == 'Limerick':
      result = generate_poem.limerick()
    elif type == 'Free verse':
      result = generate_poem.free_verse()
    else:
      return web.internalerror('Poem type not supported.')
    result = re.sub('\r?\n', '<br>', result)
    web.header('Content-Type', 'text/html');
    return result
    
class other:
  def GET(self, name):
    path = os.path.normpath('/' + name).lstrip('/')
    if path == '':
      path = 'index.html'
    try:
      f = open(os.path.join('site', path))
      web.header('Content-Type', mimetypes.guess_type(path));
      return f.read()
    except:
      return web.notfound('Sorry, the file you were looking for was not found on this server.')
  
  
if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
