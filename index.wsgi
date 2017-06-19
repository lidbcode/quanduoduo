import sae
from coupon import wsgi

application = sae.create_wsgi_app(wsgi.application)