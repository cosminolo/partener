from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import stripe.checkout
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
   self.init_components(**properties)
   try:
    lit1=["a", "b", "c", "d", "f", "g", "h", "k", "m", "n", "o", "p", "r", "s", "t"]
    lit2=["e", "i", "j", "l", "x", "y"]
    if self.label_1.text[0] in lit1:
      self.label_1.background="#F8F7CA"
      self.text_box_1.background="#CAECF8"
      self.text_box_2.background="#CAECF8"
      self.text_box_3.background="#CAECF8"
      self.text_box_4.background="#CAECF8"
      self.text_box_5.background="#CAECF8"
      self.text_box_6.background="#CAECF8"
      self.text_box_7.background="#CAECF8"
      self.text_box_8.background="#CAECF8"
      self.text_box_9.background="#CAECF8"
      self.text_box_10.background="#CAECF8"
      self.text_box_11.background="#CAECF8"
      self.text_box_12.background="#CAECF8"
      self.text_box_13.background="#CAECF8"
      self.text_box_14.background="#CAECF8"
      self.text_box_15.background="#CAECF8"
      self.text_box_16.background="#CAECF8"
      self.text_box_17.background="#CAECF8"
      
    if self.label_1.text[0] in lit2:
      self.label_1.background="#E3F9A9"
      self.text_box_1.background="#E3F9A9"
      self.text_box_1.enabled = False
      self.text_box_2.background="#E3F9A9"
      self.text_box_2.enabled = False
      self.text_box_3.background="#E3F9A9"
      self.text_box_3.enabled = False
      self.text_box_4.background="#E3F9A9"
      self.text_box_4.enabled = False
      self.text_box_5.background="#E3F9A9"
      self.text_box_5.enabled = False
      self.text_box_6.background="#E3F9A9"
      self.text_box_6.enabled = False
      self.text_box_7.background="#E3F9A9"
      self.text_box_7.enabled = False
      self.text_box_8.background="#E3F9A9"
      self.text_box_8.enabled = False
      self.text_box_9.background="#E3F9A9"
      self.text_box_9.enabled = False
      self.text_box_10.background="#E3F9A9"
      self.text_box_10.enabled = False
      self.text_box_11.background="#E3F9A9"
      self.text_box_12.enabled = False
      self.text_box_12.background="#E3F9A9"
      self.text_box_12.enabled = False
      self.text_box_13.background="#E3F9A9"
      self.text_box_13.enabled = False
      self.text_box_14.background="#E3F9A9"
      self.text_box_14.enabled = False
      self.text_box_15.background="#E3F9A9"
      self.text_box_15.enabled = False
      self.text_box_16.background="#E3F9A9"
      self.text_box_16.enabled = False
      self.text_box_17.background="#E3F9A9"
      self.text_box_17.enabled = False
      
   except:
    pass      

  def text_box_1_lost_focus(self, **event_args):   
   if self.text_box_1.enabled == True:
    s = self.text_box_1.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
    else:
        self.text_box_1.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_ant']=0
        self.text_box_1_lost_focus()
    pass

  def text_box_2_lost_focus(self, **event_args):
   if self.text_box_2.enabled == True:
    s = self.text_box_2.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
    else:
        self.text_box_2.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_c']=0
        self.text_box_2_lost_focus()  
    pass

  def text_box_3_lost_focus(self, **event_args):
    if self.text_box_3.enabled == True:
     s = self.text_box_3.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_3.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_2']=0
        self.text_box_3_lost_focus() 
    pass

  def text_box_4_lost_focus(self, **event_args):
    if self.text_box_4.enabled == True:
     s = self.text_box_4.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_4.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_3']=0
        self.text_box_4_lost_focus() 
    pass

  def text_box_5_lost_focus(self, **event_args):
    if self.text_box_5.enabled == True:
     s = self.text_box_5.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_5.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_4']=0
        self.text_box_5_lost_focus()
    pass

  def text_box_6_lost_focus(self, **event_args):
    if self.text_box_6.enabled == True:
     s = self.text_box_6.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_6.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_5']=0
        self.text_box_6_lost_focus()
    pass

  def text_box_7_lost_focus(self, **event_args):
    if self.text_box_7.enabled == True:
     s = self.text_box_7.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_7.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_6']=0
        self.text_box_7_lost_focus()
    pass

  def text_box_8_lost_focus(self, **event_args):
    if self.text_box_8.enabled == True:
     s = self.text_box_8.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_8.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_7']=0
        self.text_box_8_lost_focus()
    pass

  def text_box_9_lost_focus(self, **event_args):
    if self.text_box_9.enabled == True:
     s = self.text_box_9.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_9.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_8']=0
        self.text_box_9_lost_focus()
    pass

  def text_box_10_lost_focus(self, **event_args):
    if self.text_box_10.enabled == True:
     s = self.text_box_10.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_10.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_9']=0
        self.text_box_10_lost_focus()
    pass

  def text_box_11_lost_focus(self, **event_args):
    if self.text_box_11.enabled == True:
     s = self.text_box_11.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_11.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_10']=0
        self.text_box_11_lost_focus()
    pass

  def text_box_12_lost_focus(self, **event_args):
    if self.text_box_12.enabled == True:
     s = self.text_box_12.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_12.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_11']=0
        self.text_box_12_lost_focus()
    pass

  def text_box_13_lost_focus(self, **event_args):
    if self.text_box_13.enabled == True:
     s = self.text_box_13.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_13.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_12']=0
        self.text_box_13_lost_focus() 
    pass

  def text_box_14_lost_focus(self, **event_args):
    if self.text_box_14.enabled == True:
     s = self.text_box_14.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_14.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_13']=0
        self.text_box_14_lost_focus()
    pass

  def text_box_15_lost_focus(self, **event_args):
    if self.text_box_15.enabled == True:
     s = self.text_box_15.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_15.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_14']=0
        self.text_box_15_lost_focus()
    pass

  def text_box_16_lost_focus(self, **event_args):
    if self.text_box_16.enabled == True:
     s = self.text_box_16.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_16.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_15']=0
        self.text_box_16_lost_focus()
    pass

  def text_box_17_lost_focus(self, **event_args):
    if self.text_box_17.enabled == True:
     s = self.text_box_17.text
     if s.isdigit() or (s.startswith("-") and s[1:].isdigit()): 
       get_open_form('cf').refr() 
     else:
        self.text_box_17.text=0
        alert("Doar numar fara zecimale sau separatori!")
        self.item['an_16']=0
        self.text_box_17_lost_focus()
    pass

  


















  
  
  
