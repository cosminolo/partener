from ._anvil_designer import critTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import stripe.checkout
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json
class crit(critTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    global c1
    c1 = json.loads(anvil.server.call("get_crit", self.ups()))
    #print(c1)
    self.item = c1
    #print(c1['crit'])
  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          return us
      pass 
    
 
    
  def button_1_click(self, **event_args):
    open_form('init')
    pass

  def check_box_5_change(self, **event_args):
    anvil.server.call("upc", self.ups(), c1)
    pass

  def button_2_click(self, **event_args):
    open_form('init.verific')
    pass

  def button_3_click(self, **event_args):
    open_form('init.analiza')
    pass

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    a = "True"
    self.check_box_1.checked = eval(a)
    pass

  def check_box_1_change(self, **event_args):
   anvil.server.call("upc", self.ups(), c1)
   pass

  def check_box_2_change(self, **event_args):
    anvil.server.call("upc", self.ups(), c1)
    pass

  def check_box_3_change(self, **event_args):
    anvil.server.call("upc", self.ups(), c1)
    pass

  def check_box_4_change(self, **event_args):
    anvil.server.call("upc", self.ups(), c1)
    pass

  def check_box_6_change(self, **event_args):
    anvil.server.call("upc", self.ups(), c1)
    pass

  def check_box_7_change(self, **event_args):
    anvil.server.call("upc", self.ups(), c1)
    pass

  def check_box_8_change(self, **event_args):
    anvil.server.call("upc", self.ups(), c1)
    pass

  def check_box_9_change(self, **event_args):
    anvil.server.call("upc", self.ups(), c1)
    pass

  def check_box_10_change(self, **event_args):
    anvil.server.call("upc", self.ups(), c1)
    pass

  def check_box_12_change(self, **event_args):
    anvil.server.call("upc", self.ups(), c1)
    pass

  def check_box_13_change(self, **event_args):
    anvil.server.call("upc", self.ups(), c1)
    pass

  def check_box_14_change(self, **event_args):
    anvil.server.call("upc", self.ups(), c1)
    pass

  def check_box_15_change(self, **event_args):
    anvil.server.call("upc", self.ups(), c1)
    pass

  def button_8_click(self, **event_args):
    p1 = anvil.server.call("get_p1", self.ups())
    cui = p1['gen']['cui']
    #cui = 33741906
    conf = confirm("Consult prin Risco?")
    c =""
    if conf == True:
         c= stripe.checkout.charge(amount=300,
                           currency="RON",
                           title="Raport",
                           description="verificari insolventa")
    try:
       if c["result"] == "succeeded":
        chk = anvil.server.call("insolventa", cui)
        if chk == False:
           c1['crit']['h'] = True
           self.check_box_8.checked =  True
           anvil.server.call("upc", self.ups(), c1) 
        if chk == True:
           c1['crit']['h'] = False
           self.check_box_8.checked =  False
           anvil.server.call("upc", self.ups(), c1)  
    except:
      pass
    pass

  




















