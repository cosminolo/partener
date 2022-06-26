import anvil.users
import json
from anvil import *
import stripe.checkout
import anvil.server

def global_us(us):
     v = us + "bal"
     vv = "Global" + " " + v
     return vv
   
