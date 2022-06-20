from ._anvil_designer import finTemplate
from anvil import *
import stripe.checkout
import anvil.server
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
    self.ups()
    
   
    self.grid_panel_1.visible 
    global txb
    txb = self.txb = {}
    global i
    global j
    i = 1
    j = 0    
    for i in range(1, 9): # col 
      k=10+i  
      if i == 1:
       self.txb[k] = Label(font="Arial", font_size="12",
                              spacing_above = "small",
                              spacing_below = "none",
                              width=50,
                              foreground="#000",background="#fff"")
       self.txb[k].tag.name = k
       self.txb[k].text = "Cont"
       self.grid_panel_1.add_component(self.txb[k], row=1, col_xs=0, width_xs=1)
      if i == 2:
         self.txb[k] = Label(font="Arial", font_size="12",
                              spacing_above = "small",
                              spacing_below = "none",
                              width=150,
                              foreground="#000",background="#fff"")
         self.txb[k].tag.name = k
         self.txb[k].text = "Denumire"
         self.grid_panel_1.add_component(self.txb[k], row=1, col_xs=0, width_xs=2)
      if i == 3 or i == 5 or i == 7 or i == 9:       
         self.txb[k] = Label(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "none",
                              width=50,
                              foreground="#000",background="#fff"")
         self.txb[k].role = "input" #"form-control"
         self.txb[k].tag.name = k
         self.txb[k].text = "Bilant an"
         self.grid_panel_1.add_component(self.txb[k], row=1, col_xs=0, width_xs=1)
      if i == 4 or i == 6 or i == 8: 
         self.txb[k] = TextBox(type="text", font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "none",
                              width=80,
                              foreground="#000",background="#fff",placeholder=f"place{k}")
         self.txb[k].role = "input" #"form-control"
         self.txb[k].tag.name = k
         self.grid_panel_1.add_component(self.txb[k], row=1, col_xs=0, width_xs=1)
         self.txb[k].set_event_handler('lost_focus', self.l_focus)                       
    for i in range(1, 8): # col 
      k=20+i  
      if i == 1:
       self.txb[k] = Label(font="Arial", font_size="12",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=400,
                              foreground="#000",background="#fff"")
       self.txb[k].tag.name = k
       self.txb[k].text = "  "
       self.grid_panel_1.add_component(self.txb[k], row=2, col_xs=0, width_xs=3)
     
      if i == 2 or i == 4 or i == 6:
        self.txb[k] = Label(font="Arial", font_size="8",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=100,                              
                              foreground="#000",background="#fff"")
        self.txb[k].tag.name = k
        self.txb[k].text = "Debit"
        self.grid_panel_1.add_component(self.txb[k], row=2, col_xs=0, width_xs=1)                   
      
      if i == 3 or i == 5 or i >6 :
        self.txb[k] = Label(font="Arial", font_size="8",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=100,
                              foreground="#000",background="#fff"")
        self.txb[k].tag.name = k
        self.txb[k].text = "Credit"
        self.grid_panel_1.add_component(self.txb[k], row=2, col_xs=0, width_xs=1) 
                            
                            
    for j in range (3,700): # rows 
       for i in range(1, 11): # col 
          k=j*10+i        
          if i == 1 :   
            self.txb[k] = TextBox(type="text", font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=50,
                              border="solid black 1px",
                              foreground="#000",background="#fff",placeholder=f"pl{k}")
            self.txb[k].role = "input" #"form-control"
            self.txb[k].tag.name = k
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=-4, width_xs=1)
          if i == 2:
            self.txb[k] = TextBox(type="text", font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=150,
                              border="solid black 1px",
                              foreground="#000",background="#fff",placeholder=f"pl{k}")
            self.txb[k].role = "input" #"form-control"
            self.txb[k].tag.name = k
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=-4, width_xs=2)
          if i >2 :
            self.txb[k] = TextBox(type="text", font="Arial", font_size="10",
                              spacing_above = "none",
                              spacing_below = "small",
                              width=100,
                              border="solid blue 1px",
                              align="right",    
                              foreground="#000",background="#fff",placeholder=f"pl{k}")
            self.txb[k].role = "input" #"form-control"
            self.txb[k].tag.name = k
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=0, width_xs=1)
            self.txb[k].set_event_handler('lost_focus', self.l_focus)  
    def button_1_click(self, **event_args):
     pass     

  def l_focus (self, sender,**event_args):
    print(sender)
    print(sender.tag.name)    
    if not sender.text:
      pass
    else:
      S = sender.text
      if S.isdigit() or (S.startswith("-") and S[1:].isdigit()):
        pass
      else:         
        sender.text = 0     
        alert("Just numbers without decimal")        
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1')
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('init')
    pass
  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          self.ls.text = user['email']


