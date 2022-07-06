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
    global p1
    p1 = anvil.server.call("pri_ini")
    self.text_box_1.text=p1['gen']['cui']    
    self.text_box_2.text=p1['gen']['name'] 
    
    self.text_box_3.text=p1['gen']['codj']   
    self.text_box_4.text=p1['gen']['adress']  
    self.text_box_5.text=p1['gen']['tel']   
    self.text_box_6.text=p1['gen']['email']
    self.text_box_7.text=p1['gen']['caen'] 
    self.text_box_8.text=p1['gen']['d_caen']    
    self.con_drop1()
    self.drop_down_1.selected_value = p1['gen']['tip']
       
    self.text_area_1.text= p1['asoc_pf']
    p1['asoc_pf'] = self.text_area_1.text
    
  def con_drop1(self):
    self.drop_down_1.items = []
    for art in [' ', 'S.R.L.', 'S.A', 'PFA', 'II', 'SRL-D']:
      self.drop_down_1.items.append(art)
      self.drop_down_1.items = self.drop_down_1.items

  def text_box_1_pressed_enter(self, **event_args):
    grup = anvil.server.call("gr", self.text_box_1.text)    
    p1['gen']['cui'] = self.text_box_1.text
    self.text_box_2.text=grup["soc"][0]["name"]    
    p1['gen']['name'] = self.text_box_2.text
    self.text_box_3.text=grup["soc"][0]["codj"]
    self.text_box_4.text=grup["soc"][0]["adress"]
    self.text_box_5.text=grup["soc"][0]["tel"]
    self.text_box_6.text=grup["soc"][0]["email"]
    self.text_box_7.text=grup["soc"][0]["caen"]
    self.text_box_8.text=grup["soc"][0]["d_caen"]
    te = ""
    for i in range(0, len(grup["asoc_pf"])):
      te = str(te) + str(grup["asoc_pf"][i]["nume"]) + "-" + str(grup["asoc_pf"][i]["cota"] +"%; ")               
    self.text_area_1.text= te
    print(p1)
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    print(p1['gen'])
    pass

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    p1['gen']['tip'] = self.drop_down_1.selected_value
    pass

  def text_box_2_pressed_enter(self, **event_args):
    p1['gen']['name'] = self.text_box_2.text
    pass





