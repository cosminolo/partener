from ._anvil_designer import stTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json
class st(stTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    p_ini = anvil.server.call("pri_ini")
    global p1
    p1=p_ini['gen']
    self.text_box_1.text=p1["cui"]
    p1["cui"] = self.text_box_1.text  
    self.text_box_2.text=p1["name"]
    p1["name"] = self.text_box_2.text  
    self.text_box_3.text=p1["codj"]
    p1["codj"] = self.text_box_3.text
    self.text_box_4.text=p1["adress"]
    p1["adress"] = self.text_box_4.text
    self.text_box_5.text=p1["tel"]
    p1["tel"] = self.text_box_5.text
    self.text_box_6.text=p1["email"]
    p1["email"] = self.text_box_6.text
    self.text_box_7.text=p1["caen"]
    p1["caen"] = self.text_box_7.text
    self.text_box_8.text=p1["d_caen"]
    p1["d_caen"] = self.text_box_8.text
    self.con_drop1()
    self.drop_down_1.selected_value = p1["tip"] 
    
  
  def con_drop1(self):
    self.drop_down_1.items = []
    for art in [' ', 'S.R.L.', 'S.A', 'PFA', 'II', 'SRL-D']:
      self.drop_down_1.items.append(art)
      self.drop_down_1.items = self.drop_down_1.items

  def text_box_1_pressed_enter(self, **event_args):
    grup = anvil.server.call("gr", self.text_box_1.text)    
    #p1["cui"]=grup["soc"][0]["cui"]
    self.text_box_2.text=grup["soc"][0]["name"]
    self.text_box_3.text=grup["soc"][0]["codj"]
    self.text_box_4.text=grup["soc"][0]["adress"]
    self.text_box_5.text=grup["soc"][0]["tel"]
    self.text_box_6.text=grup["soc"][0]["email"]
    self.text_box_7.text=grup["soc"][0]["caen"]
    self.text_box_8.text=grup["soc"][0]["d_caen"]
    print(p1)
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    print(p1)
    pass

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    p1["tip"] = self.drop_down_1.selected_value
    pass




