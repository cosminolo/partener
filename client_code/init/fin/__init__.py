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
from datetime import datetime
class fin(finTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    global p1
    #p1 = anvil.server.call("pri_ini")
    p1 = anvil.server.call("get_p1", self.ups())
    self.item = p1
    try:
      d1 = p1['data_fin']['d1']
      d2 = p1['data_fin']['d2']
      d3 = p1['data_fin']['d3']
      c1 = datetime.strptime(d1, '%Y-%m-%d')
      c2 = datetime.strptime(d2, '%Y-%m-%d')
      c3 = datetime.strptime(d3, '%Y-%m-%d')
      self.text_box_118.text =c1.strftime('%d-%m-%Y')
      self.text_box_119.text =c2.strftime('%d-%m-%Y')
      self.text_box_120.text =c3.strftime('%d-%m-%Y')
    except:
      pass
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
    self.lf(self.text_box_1)
    pass

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def text_box_2_lost_focus(self, **event_args):
    self.lf(self.text_box_2)
    pass

  def text_box_3_lost_focus(self, **event_args):
    self.lf(self.text_box_3)
    pass

  def text_box_4_lost_focus(self, **event_args):
    self.lf(self.text_box_4)
    pass

  def text_box_5_lost_focus(self, **event_args):
    self.lf(self.text_box_5)
    pass

  def text_box_6_lost_focus(self, **event_args):
    self.lf(self.text_box_6)
    pass

  def text_box_7_lost_focus(self, **event_args):
    self.lf(self.text_box_7)
    pass

  def text_box_8_lost_focus(self, **event_args):
   self.lf(self.text_box_8)
   pass

  def text_box_9_lost_focus(self, **event_args):
    self.lf(self.text_box_9)
    pass

  def text_box_10_lost_focus(self, **event_args):
    self.lf(self.text_box_10)
    pass

  def text_box_11_lost_focus(self, **event_args):
    self.lf(self.text_box_11)
    pass

  def text_box_12_lost_focus(self, **event_args):
    self.lf(self.text_box_12)
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
    p1["data_fin"]["d1"] = str(self.date_picker_1.date)
    anvil.server.call("sp1", self.ups(), p1) 
    d1 = p1['data_fin']['d1']
    c = datetime.strptime(d1, '%Y-%m-%d')
    self.text_box_118.text =c.strftime('%d-%m-%Y')  
    pass

  def date_picker_2_change(self, **event_args):
    p1["data_fin"]["d2"] = str(self.date_picker_2.date)
    anvil.server.call("sp1", self.ups(), p1) 
    d1 = p1['data_fin']['d2']
    c = datetime.strptime(d1, '%Y-%m-%d')
    self.text_box_119.text =c.strftime('%d-%m-%Y')  
    pass

  def date_picker_3_change(self, **event_args):
    p1["data_fin"]["d3"] = str(self.date_picker_3.date)
    anvil.server.call("sp1", self.ups(), p1) 
    d1 = p1['data_fin']['d1']
    c = datetime.strptime(d1, '%Y-%m-%d')
    self.text_box_120.text =c.strftime('%d-%m-%Y')  
    pass

  
  def lf(self, sender,**event_args):
    #sender.enabled = True
    s = sender.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call("sp1", self.ups(), p1)
        pass
    else:         
        sender.text = 0   
      
        alert("Doar numar fara zecimale sau separatori!") 
    pass

  def text_box_13_lost_focus(self, **event_args):
    self.lf(self.text_box_13)
    pass

  def text_box_14_lost_focus(self, **event_args):
    self.lf(self.text_box_14)
    pass

  def text_box_15_lost_focus(self, **event_args):
    self.lf(self.text_box_15)
    pass

  def text_box_16_lost_focus(self, **event_args):
    self.lf(self.text_box_16)
    pass

  def text_box_17_lost_focus(self, **event_args):
    self.lf(self.text_box_17)
    pass

  def text_box_18_lost_focus(self, **event_args):
    self.lf(self.text_box_18)
    pass

  def text_box_19_lost_focus(self, **event_args):
    self.lf(self.text_box_19)
    pass

  def text_box_20_lost_focus(self, **event_args):
    self.lf(self.text_box_20)
    pass

  def text_box_21_lost_focus(self, **event_args):
    self.lf(self.text_box_21)
    pass

  def text_box_22_lost_focus(self, **event_args):
    self.lf(self.text_box_22)
    pass

  def text_box_23_lost_focus(self, **event_args):
    self.lf(self.text_box_23)
    pass

  def text_box_24_lost_focus(self, **event_args):
    self.lf(self.text_box_24)
    pass

  def text_box_25_lost_focus(self, **event_args):
    self.lf(self.text_box_25)
    pass

  def text_box_26_lost_focus(self, **event_args):
    self.lf(self.text_box_26)
    pass

  def text_box_27_lost_focus(self, **event_args):
    self.lf(self.text_box_27)
    pass

  def text_box_28_lost_focus(self, **event_args):
    self.lf(self.text_box_28)
    pass

  def text_box_29_lost_focus(self, **event_args):
    self.lf(self.text_box_29)
    pass

  def text_box_30_lost_focus(self, **event_args):
    self.lf(self.text_box_30)
    pass

  def text_box_31_lost_focus(self, **event_args):
    self.lf(self.text_box_31)
    pass

  def text_box_32_lost_focus(self, **event_args):
    self.lf(self.text_box_32)
    pass

  def text_box_33_lost_focus(self, **event_args):
    self.lf(self.text_box_33)
    pass

  def text_box_34_lost_focus(self, **event_args):
    self.lf(self.text_box_34)
    pass

  def text_box_35_lost_focus(self, **event_args):
    self.lf(self.text_box_35)
    pass

  def text_box_36_lost_focus(self, **event_args):
    self.lf(self.text_box_36)
    pass

  def text_box_37_lost_focus(self, **event_args):
    self.lf(self.text_box_37)
    pass

  def text_box_38_lost_focus(self, **event_args):
    self.lf(self.text_box_38)
    pass

  def text_box_39_lost_focus(self, **event_args):
    self.lf(self.text_box_39)
    pass

  def text_box_40_lost_focus(self, **event_args):
    self.lf(self.text_box_40)
    pass

  def text_box_41_lost_focus(self, **event_args):
    self.lf(self.text_box_41)
    pass

  def text_box_42_lost_focus(self, **event_args):
    self.lf(self.text_box_42)
    pass

  def text_box_43_lost_focus(self, **event_args):
    self.lf(self.text_box_43)
    pass

  def text_box_44_lost_focus(self, **event_args):
    self.lf(self.text_box_44)
    pass

  def text_box_45_lost_focus(self, **event_args):
    self.lf(self.text_box_45)
    pass

  def text_box_46_lost_focus(self, **event_args):
    self.lf(self.text_box_46)
    pass

  def text_box_47_lost_focus(self, **event_args):
    self.lf(self.text_box_47)
    pass

  def text_box_48_lost_focus(self, **event_args):
    self.lf(self.text_box_48)
    pass

  def text_box_49_lost_focus(self, **event_args):
    self.lf(self.text_box_49)
    pass

  def text_box_50_lost_focus(self, **event_args):
    self.lf(self.text_box_50)
    pass

  def text_box_51_lost_focus(self, **event_args):
    self.lf(self.text_box_51)
    pass

  def text_box_52_lost_focus(self, **event_args):
    self.lf(self.text_box_52)
    pass

  def text_box_53_lost_focus(self, **event_args):
    self.lf(self.text_box_53)
    pass

  def text_box_54_lost_focus(self, **event_args):
    self.lf(self.text_box_54)
    pass

  def text_box_55_lost_focus(self, **event_args):
    self.lf(self.text_box_55)
    pass

  def text_box_56_lost_focus(self, **event_args):
    self.lf(self.text_box_56)
    pass

  def text_box_57_lost_focus(self, **event_args):
    self.lf(self.text_box_57)
    pass































































