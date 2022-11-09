from ._anvil_designer import finTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class fin(finTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    global p1
    #p1 = anvil.server.call("pri_ini")
    p1 = anvil.server.call("get_p1", self.ups())
    self.item = p1
  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          return us
      pass     
  def text_box_108_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
  
  def v(self, tt):
   if self.text_box_4.enabled == True:
    s = self.text_box_4.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call('upp_bal', us, My_globals.bal)
        pass
    else:         
        self.text_box_4.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
   pass

  def text_box_1_lost_focus(self, **event_args):
   if self.text_box_1.enabled == True:
    s = self.text_box_1.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call("sp1", self.ups(), p1)
        pass
    else:         
        self.text_box_1.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
    
    pass

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def text_box_2_lost_focus(self, **event_args):
    if self.text_box_2.enabled == True:
        s = self.text_box_2.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call("sp1", self.ups(), p1)
        pass
    else:         
        self.text_box_2.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
    pass

  def text_box_3_lost_focus(self, **event_args):
    if self.text_box_3.enabled == True:
        s = self.text_box_3.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call("sp1", self.ups(), p1)
        pass
    else:         
        self.text_box_3.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
    pass

  def text_box_4_lost_focus(self, **event_args):
    if self.text_box_4.enabled == True:
        s = self.text_box_4.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call("sp1", self.ups(), p1)
        pass
    else:         
        self.text_box_4.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
    pass

  def text_box_5_lost_focus(self, **event_args):
    if self.text_box_5.enabled == True:
      s = self.text_box_5.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call("sp1", self.ups(), p1)
        pass
    else:         
        self.text_box_5.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
    pass

  def text_box_6_lost_focus(self, **event_args):
    if self.text_box_6.enabled == True:
      s = self.text_box_6.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call("sp1", self.ups(), p1)
        pass
    else:         
        self.text_box_6.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
    pass

  def text_box_7_lost_focus(self, **event_args):
    if self.text_box_7.enabled == True:
      s = self.text_box_7.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call("sp1", self.ups(), p1)
        pass
    else:         
        self.text_box_7.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
    pass

  def text_box_8_lost_focus(self, **event_args):
   if self.text_box_8.enabled == True:
        s = self.text_box_8.text
   if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call("sp1", self.ups(), p1)
        pass
   else:         
        self.text_box_8.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
   pass

  def text_box_9_lost_focus(self, **event_args):
    if self.text_box_9.enabled == True:
        s = self.text_box_9.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call("sp1", self.ups(), p1)
        pass
    else:         
        self.text_box_9.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
    pass

  def text_box_10_lost_focus(self, **event_args):
    if self.text_box_10.enabled == True:
      s = self.text_box_10.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call("sp1", self.ups(), p1)
        pass
    else:         
        self.text_box_10.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
    pass

  def text_box_11_lost_focus(self, **event_args):
    if self.text_box_11.enabled == True:
        s = self.text_box_11.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call("sp1", self.ups(), p1)
        pass
    else:         
        self.text_box_11.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
    pass

  def text_box_12_lost_focus(self, **event_args):
    if self.text_box_12.enabled == True:
        s = self.text_box_12.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call("sp1", self.ups(), p1)
        pass
    else:         
        self.text_box_12.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
    pass

  def button_2_click(self, **event_args):
    open_form('init.st')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('init')
    pass

  def button_3_click(self, **event_args):
    open_form('init.bal')
    pass

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    anvil.server.call("sp1", self.ups(), p1)
    print (p1["data_fin"]["d1"])
    pass


















