import sae
from Web import wsgi

application = sae.create_wsgi_app(wsgi.application)