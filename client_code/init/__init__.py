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
    global txb
    txb = self.txb = {}
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
    c = confirm("Do you wish to continue?")    
    if c == False :
       self.visib(2)
    if c== True:
       anvil.server.call("arh", us, self.text_box_4.text, self.text_box_1.text, self.text_box_2.text, js )
       self.visib(2)
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
    
      
    else:
      self.label_2.visible = False
      self.label_3.visible = False
      self.label_4.visible = False
      self.label_5.visible = False
      self.text_box_1.visible = False
      self.text_box_2.visible = False
      self.text_box_3.visible = False
      self.text_box_4.visible = False
    
    pass

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.grid_panel_1.clear()
    global txb
    txb = self.txb = {}
    global i
    global j
    i = 1
    j = 0    
    for i in range(1, 5): # col 
      k=10+i  
      if i == 1:
       self.txb[k] = Label(font="Arial", font_size="12",
                              spacing_above = "small",
                              spacing_below = "none",
                              width=80,
                              foreground="#000",background="#fff"")
       self.txb[k].tag.name = k
       self.txb[k].text = "Entitatea"
       self.grid_panel_1.add_component(self.txb[k], row=1, col_xs=0, width_xs=2)
      if i == 2:
       self.txb[k] = Label(font="Arial", font_size="12",
                              spacing_above = "small",
                              spacing_below = "none",
                              width=80,
                              foreground="#000",background="#fff"")
       self.txb[k].tag.name = k
       self.txb[k].text = "Facilitate"
       self.grid_panel_1.add_component(self.txb[k], row=1, col_xs=0, width_xs=2)
      if i == 3:
       self.txb[k] = Label(font="Arial", font_size="12",
                              spacing_above = "small",
                              spacing_below = "none",
                              width=80,
                              foreground="#000",background="#fff"")
       self.txb[k].tag.name = k
       self.txb[k].text = "Data"
       self.grid_panel_1.add_component(self.txb[k], row=1, col_xs=0, width_xs=2) 
      if i == 4:
       self.txb[k] = Label(font="Arial", font_size="12",
                              spacing_above = "small",
                              spacing_below = "none",
                              width=80,
                              foreground="#000",background="#fff"")
       self.txb[k].tag.name = k
       self.txb[k].text = "Alege"
       self.grid_panel_1.add_component(self.txb[k], row=1, col_xs=0, width_xs=2) 
    for j in range (2,4): # rows 
       for i in range(1, 6): # col 
          k=j*10+i        
          if i <4 :   
            self.txb[k] = TextBox(type="text", font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=80,
                              foreground="#000",background="#fff",placeholder=f"pl{k}")
            self.txb[k].role = "input" #"form-control"
            self.txb[k].tag.name = k
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=0, width_xs=2)
          if i ==5 :   
            self.txb[k] = RadioButton(background="#fff", width=80)                           
            self.txb[k].tag.name = k
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=0, width_xs=1)
    for txb in self.grid_panel_1.get_components():    
      if type(txb) is RadioButton:
           if txb.value == True:
               print("c")  
           else:
              print(txb.tag.name)
    






