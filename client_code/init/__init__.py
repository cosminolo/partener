from ._anvil_designer import initTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..init.start import start
from datetime import datetime, date
import json
class init(initTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
    self.ups()
    #self.column_panel_2.visible=False
    
  def ups(self):
      # Get the currently logged in user (if any)
      self.login_status.text = ""
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          self.login_status.text = us
          anvil.server.call("add_user", us)

  

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self.login_status.text != "": 
        anvil.server.call("app_new", self.login_status.text)      
        open_form("init.start")
        #new_form = start()
        #self.column_panel_2.clear()
        #self.column_panel_2.add_component(new_form)
    else:
        anvil.users.login_with_form()
        self.ups()
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    self.ups()
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    self.ups()
    pass

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self.login_status.text != "":             
        open_form("init.start")
        #new_form = start()
        #self.column_panel_2.clear()
        #self.column_panel_2.add_component(new_form)
    else:
        anvil.users.login_with_form()
        self.ups()
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.visib(1)
    us = self.login_status.text
    self.text_box_3.text = us
    self.text_box_4.text = "{:%d.%m.%Y}".format(datetime.now())
    js = anvil.server.call("prel_js_gol", us, 2)    
    self.item = js
    
    #self.text_box_1.text = js['den']
    #self.text_box_2.text = js['facilit']
    pass
  def visib(self, param):
    if param == 1:
      self.label_2.visible = True
      self.label_3.visible = True
      self.label_4.visible = True
      self.label_5.visible = True
      self.text_box_1.visible = True
      self.text_box_2.visible = True
      self.text_box_3.visible = True
      self.text_box_4.visible = True
      self.button_3.visible = True
      
    else:
      self.label_2.visible = False
      self.label_3.visible = False
      self.label_4.visible = False
      self.label_5.visible = False
      self.text_box_1.visible = False
      self.text_box_2.visible = False
      self.text_box_3.visible = False
      self.text_box_4.visible = False
      self.button_3.visible = False
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.visib(2)
    pass









