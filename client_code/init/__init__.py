from ._anvil_designer import initTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#from ..init.st import st
from datetime import datetime, date
import json
import time
from .. import My_globals
class init(initTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
    self.ups()
    self.grid_panel_1.clear()
    self.visib(2)
    global txb
    txb = self.txb = {}
  def ups(self):
      # Get the currently logged in user (if any)
      self.login_status.text = ""
      My_globals.us = ""
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          self.login_status.text = us
          My_globals.us =us
          anvil.server.call("add_user", us)
  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self.login_status.text != "": 
       us = self.login_status.text
       anvil.server.call("add_user", us)
       anvil.server.call("app_new", self.login_status.text)
       open_form("init.st")  
    else:
        anvil.users.login_with_form()
        self.ups()
    pass

  def button_1_click(self, **event_args):
    self.grid_panel_1.clear()
    self.visib(2)
    anvil.users.logout()
    self.ups()
    n = Notification("",
             title="Succes sign out!").show()
    time.sleep(1)
    n.hide()
    pass

  def button_2_click(self, **event_args):
    self.grid_panel_1.clear()
    self.visib(2)
    anvil.users.login_with_form()
    self.ups()
    pass

  def link_4_click(self, **event_args):
    self.visib(2)
    if self.login_status.text != "":             
        open_form("init.st")        
    else:
        anvil.users.login_with_form()
        self.ups()
    pass

  def link_1_click(self, **event_args):
    anvil.users.login_with_form()
    self.ups()
    self.grid_panel_1.clear()
    self.visib(1)
    us = self.login_status.text
    self.text_box_3.text = us
    self.text_box_4.text =datetime.now()
    p1 = anvil.server.call("get_p1", us)    
    self.item = p1
    c = confirm("Salvez in arhiva ?")    
    if c == False :
       cs = confirm("Sterg datele introduse ?")
       if cs == True:
        #preiau json_gol
        anvil.server.call("app_new", us)
        self.visib(2)
        if cs == False:
          self.visib(2)
    if c== True:
       anvil.server.call("arh2", us, self.text_box_4.text, self.text_box_1.text, self.text_box_2.text)
    self.grid_panel_1.clear()
    self.visib(2)
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
    anvil.users.login_with_form()
    self.ups()
    self.visib(2)
    self.grid_panel_1.clear()
    global txb
    txb = self.txb = {}
    global i
    global j
    i = 1
    j = 0    
    k=10
    us = self.login_status.text
    rows = anvil.server.call("nr_rows", us)   
   
    for j in range (2,rows+2): # rows 
       for i in range(1, 5): # col 
          k=j*10+i        
          if i ==1 :   
            self.txb[k] = Label(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=350,
                              foreground="#000",background="#fff"")
            self.txb[k].role = "form-control"
            self.txb[k].tag.name = k                           
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=0, width_xs=3)
          if i ==2 :   
            self.txb[k] = Label(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=400,
                              foreground="#000",background="#fff")
            self.txb[k].role = "form-control"
            self.txb[k].tag.name = k                           
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=0, width_xs=5)
          if i ==3 :   
            self.txb[k] = Label(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=150,
                              align="right",
                              foreground="#000",background="#fff")
            self.txb[k].role = "form-control"
            self.txb[k].tag.name = k                           
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=0, width_xs=3)
          if i ==4 :   
            self.txb[k] = RadioButton(background="#fff", width=15) 
            self.txb[k].tag.name = k                          
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=0, width_xs=1)
            self.txb[k].set_event_handler('clicked', self.clicked)              
       list_apl = json.loads(json.dumps(anvil.server.call("sele_us", us) ))                               
                 
       i=1
       k=21                    
       for i in range(0,rows):
         try:                   
          self.txb[k].text = list_apl[i]["soc"]
          self.txb[k+1].text = list_apl[i]["facilit"]
          self.txb[k+2].text = list_apl[i]["dat"]            
          k=k+10
         except:
          pass
       pass 
  def clicked (self, sender,**event_args):
      S = sender.value
      pl = str(sender.tag.name)                   
      linie = int(pl[:len(pl)-1]) *10+1
      us = self.login_status.text
      soc = self.txb[linie].text
      facilit = self.txb[linie+1].text
      dat = self.txb[linie+2].text                         
      c = confirm("Preiau in lucru pentru modificari ?")
      if c == False:                          
          cs = confirm("Sterg din arhiva iremediabil ?")
          if cs == True:
            anvil.server.call("sterge_arh",us, soc, facilit, dat)
            self.link_5_click()
          else:
            self.grid_panel_1.clear()                    
      if c == True:
          #preia in lucru                            
          anvil.server.call("preia_inlucru",us, soc, facilit, dat)
          self.link_4_click()                      
  pass                       
  def link_2_click(self, **event_args):
    anvil.users.login_with_form()
    self.ups()
    self.visib(2)
    self.grid_panel_1.clear()
    global txb
    txb = self.txb = {}
    global i
    global j
    i = 1
    j = 0    
    k=10
    us = self.login_status.text
    rows = anvil.server.call("nr_rows", us)                           
    for j in range (2,rows+2): # rows 
       for i in range(1, 5): # col 
          k=j*10+i        
          if i ==1 :   
            self.txb[k] = Label(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=350,
                              foreground="#000",background="#fff"")
            self.txb[k].role = "form-control"
            self.txb[k].tag.name = k                           
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=0, width_xs=3)
          if i ==2 :   
            self.txb[k] = Label(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=400,
                              foreground="#000",background="#fff")
            self.txb[k].role = "form-control"
            self.txb[k].tag.name = k                           
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=0, width_xs=5)
          if i ==3 :   
            self.txb[k] = Label(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=150,
                              align="right",
                              foreground="#000",background="#fff")
            self.txb[k].role = "form-control"
            self.txb[k].tag.name = k                           
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=0, width_xs=3)
          if i ==4 :   
            self.txb[k] = CheckBox(background="#fff", width=15) 
            self.txb[k].tag.name = k                          
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=0, width_xs=1)
            self.txb[k].set_event_handler('change', self.change)              
       list_apl = anvil.server.call("sele_us", us)
       i=1
       k=21                  
       for i in range(0,rows):
         try:                   
          self.txb[k].text = list_apl[i]["soc"]
          self.txb[k+1].text = list_apl[i]["facilit"]
          self.txb[k+2].text = list_apl[i]["dat"]            
          k=k+10
         except:
          pass
       pass 
  def change (self, sender,**event_args):
      S = sender.checked
      pl = str(sender.tag.name)                   
      linie = int(pl[:len(pl)-1]) *10+1
      us = self.login_status.text
      soc = self.txb[linie].text
      facilit = self.txb[linie+1].text
      dat = self.txb[linie+2].text                         
      c = confirm("Trimit email?")
      if c == False:                          
         alert("Email netransmis")  
         self.grid_panel_1.clear()                    
      if c == True:                      
          la = anvil.server.call("sentem", us, soc,facilit, dat)     
          alert("Facilitatea " + facilit + " pentru " + soc + " a fost transmisa la " + la)                      
          self.grid_panel_1.clear()                        
  pass                                                   
   







