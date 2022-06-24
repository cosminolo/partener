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
import json
from ... import My_globals
class fin(finTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.   
    
    My_globals.bal = anvil.server.call("get_bal",self.ups())
    #print (My_globals.bal)
    self.grid_panel_1.visible 
    global txb
    txb = self.txb = {}
    global i
    global j
    My_globals.z = 0
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
    for i in range(1, 12): # col 
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
    m=0  
    k=14                      
    for j in range (3,50): # rows
        k=k+16
                            
        for i in range(1, 12): # col 
          m=k+i                            
          if i == 1 :   
            self.txb[m] = TextBox(type="text", font="Arial", font_size="10",
                              spacing_above = "none",
                              spacing_below = "none",
                              width=50,
                              border="solid black 1px",
                              foreground="#000",background="#fff",placeholder=f"pl{m}")
            self.txb[m].role = "input" #"form-control"
            self.txb[m].tag.name = m           
                          
            self.grid_panel_1.add_component(self.txb[m], row=j, col_xs=-4, width_xs=1)
          if i == 2:
            self.txb[m] = TextBox(type="text", font="Arial", font_size="10",
                              spacing_above = "none",
                              spacing_below = "none",
                              width=150,
                              border="solid black 1px",
                              foreground="#000",background="#fff",placeholder=f"pl{m}")
            self.txb[m].role = "input" #"form-control"
            self.txb[m].tag.name = m                              
            self.grid_panel_1.add_component(self.txb[m], row=j, col_xs=-4, width_xs=2)
          if i == 3 :
            self.txb[m] = TextBox(type="text", font="Arial", font_size="10",
                              spacing_above = "none",
                              spacing_below = "none",
                              width=50,
                              border="solid blue 1px",
                              align="right",    
                              foreground="#000",background="#fff",placeholder=f"pl{m}")
            self.txb[m].role = "input" #"form-control"
            self.txb[m].tag.name = m                             
            self.grid_panel_1.add_component(self.txb[m], row=j, col_xs=0, width_xs=1)
            #self.txb[k].set_event_handler('lost_focus', self.l_focus)  
          if i == 4 :
            self.txb[m] = TextBox(type="text", font="Arial", font_size="10",
                              spacing_above = "none",
                              spacing_below = "none",
                              width=50,
                              border="solid blue 1px",
                              align="right",    
                              foreground="#000",background="#fff",placeholder=f"pl{m}")
            self.txb[m].role = "input" #"form-control"
            self.txb[m].tag.name = m                          
            self.grid_panel_1.add_component(self.txb[m], row=j, col_xs=0, width_xs=1)
            #self.txb[k].set_event_handler('lost_focus', self.l_focus)
          if i == 5 :
            self.txb[m] = TextBox(type="text", font="Arial", font_size="10",
                              spacing_above = "none",
                              spacing_below = "none",
                              width=50,
                              border="solid blue 1px",
                              align="right",    
                              foreground="#000",background="#fff",placeholder=f"pl{m}")
            self.txb[m].role = "input" #"form-control"
            self.txb[m].tag.name = m                          
            self.grid_panel_1.add_component(self.txb[m], row=j, col_xs=0, width_xs=1)
            #self.txb[k].set_event_handler('lost_focus', self.l_focus) 
          if i > 5 :
            self.txb[m] = TextBox(type="number", font="Arial", font_size="10",
                              spacing_above = "none",
                              spacing_below = "none",
                              width=100,
                              border="solid blue 1px",
                              align="right",    
                              foreground="#000",background="#fff",placeholder=f"pl{m}")
            self.txb[m].role = "input" #"form-control"
            self.txb[m].tag.name = m
                      
            self.grid_panel_1.add_component(self.txb[m], row=j, col_xs=0, width_xs=1)
            #self.txb[k].set_event_handler('lost_focus', self.l_focus)                  
    self.inc_pag(My_globals.z)    
                            
                            
  def button_1_click(self, **event_args):
      My_globals.z = My_globals.z+47
      print (My_globals.z)
      if My_globals.z <= 470:                       
        self.inc_pag(My_globals.z)                      
      pass
  def inc_pag(self, r): 
   self.clear_panel()                         
   try:                         
     j = int(31)
     r = int(r)                       
     for n in range (1,48):                           
       self.txb[j].text = My_globals.bal[r]["Cont"]                    
       self.txb[j+1].text = My_globals.bal[r]["DENUMIRE"]
       self.txb[j+2].text = My_globals.bal[r]["COD_a"]   
       self.txb[j+3].text = My_globals.bal[r]["COD_p"]  
       self.txb[j+4].text = My_globals.bal[r]["TIP"]       
       if My_globals.bal[r]["D1"] is not None:                   
        self.txb[j+5].text = My_globals.bal[r]["D1"]
       if My_globals.bal[r]["C1"] is not None:                    
        self.txb[j+6].text = My_globals.bal[r]["C1"]                     
       if My_globals.bal[r]["D2"] is not None:                   
        self.txb[j+7].text = My_globals.bal[r]["D2"]
       if My_globals.bal[r]["C2"] is not None:                    
        self.txb[j+8].text = My_globals.bal[r]["C2"]  
       if My_globals.bal[r]["D3"] is not None:                   
        self.txb[j+9].text = My_globals.bal[r]["D3"]
       if My_globals.bal[r]["C3"] is not None:                    
        self.txb[j+10].text = My_globals.bal[r]["C3"]                       
                         
       j = j + 16
       r = r + 1
                            
   except:
           pass                 
   pass 
                            
  def clear_panel (self):
     j = int(31)                        
     for n in range (1,48):
       self.txb[j].text = ""                
       self.txb[j+1].text = ""
       self.txb[j+2].text = ""  
       self.txb[j+3].text = "" 
       self.txb[j+4].text = ""    
       self.txb[j+5].text = ""               
       self.txb[j+6].text = ""            
       self.txb[j+7].text = ""                      
       self.txb[j+8].text = ""              
       self.txb[j+9].text = ""                     
       self.txb[j+10].text = ""
       j = j+16                     
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
          return user['email']


