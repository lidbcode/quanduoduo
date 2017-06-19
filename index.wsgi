import sae
import os,sys
root = os.path.dirname(__file__)
sys.path.insert(0,os.path.join(root,'site-packages'))
from coupon import wsgi

application = sae.create_wsgi_app(wsgi.application)