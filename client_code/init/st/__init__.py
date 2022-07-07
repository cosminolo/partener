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
    self.item = p1
    #self.text_box_1.text=p1['gen']['cui']    
    #self.text_box_2.text=p1['gen']['name'] 
    
    #self.text_box_3.text=p1['gen']['codj']   
    #self.text_box_4.text=p1['gen']['adress']  
    #self.text_box_5.text=p1['gen']['tel']   
    #self.text_box_6.text=p1['gen']['email']
    #self.text_box_7.text=p1['gen']['caen'] 
    #self.text_box_8.text=p1['gen']['d_caen']    
    #self.con_drop1()
    #self.drop_down_1.selected_value = p1['gen']['tip']
       
    #self.text_area_1.text= p1['asoc_pf']
    #p1['asoc_pf'] = self.text_area_1.text
    
  def con_drop1(self):
    self.drop_down_1.items = []
    for art in [' ', 'S.R.L.', 'S.A', 'PFA', 'II', 'SRL-D']:
      self.drop_down_1.items.append(art)
      self.drop_down_1.items = self.drop_down_1.items

  def text_box_1_pressed_enter(self, **event_args):
    grup = anvil.server.call("gr", self.text_box_1.text)    
    p1['gen']['cui'] = self.text_box_1.text
    self.text_box_2.text = grup["soc"][0]["name"]    
    p1['gen']['name'] = grup["soc"][0]["name"]  
    self.text_box_3.text = grup["soc"][0]["codj"]
    p1['gen']['codj'] = grup["soc"][0]["codj"]
    self.text_box_4.text = grup["soc"][0]["adress"]
    p1['gen']['adress'] = grup["soc"][0]["adress"]
    self.text_box_5.text = grup["soc"][0]["tel"]
    p1['gen']['tel'] = grup["soc"][0]["tel"]
    self.text_box_6.text = grup["soc"][0]["email"]
    p1['gen']['email'] = grup["soc"][0]["email"]
    self.text_box_7.text = grup["soc"][0]["caen"]
    p1['gen']['caen'] = grup["soc"][0]["caen"]
    self.text_box_8.text=grup["soc"][0]["d_caen"]
    p1['gen']['d_caen'] = grup["soc"][0]["d_caen"]
    for i in range (0, len(grup['asoc_pf'])):
      p1['asoc'].append(grup['asoc_pf'][i])    
    
    
    row = len(p1["asoc"])
    self.gru(row, p1["asoc"])    
    print(p1['asoc'])
    pass
  def gru(self, rows, ex):
    self.grid_panel_1.clear()
    global txb
    txb = self.txb = {}
    global i
    global j
    i = 1
    j = 0    
    k=10                          
    for j in range (2,rows+2): # rows 
       for i in range(1, 4): # col 
          k=j*10+i        
          if i ==1 :   
            self.txb[k] = TextArea(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              #width=100,
                              foreground="#000",background="#fff"")
            self.txb[k].role = "scroll"
            self.txb[k].tag.name = k                           
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=0, width_xs=4)
          if i ==2 :   
            self.txb[k] = TextArea(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              #width=100,
                              foreground="#000",background="#fff")
            self.txb[k].role = "form-control"
            self.txb[k].tag.name = k                           
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=4, width_xs=7)
          if i ==3 :   
            self.txb[k] = Button(background="#fff", width=10) 
            #self.txb[k] = RadioButton()               
            self.txb[k].tag.name = k   
            self.txb[k].text = "X"                                
            self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=8, width_xs=1)
            #self.txb[k].set_event_handler('clicked', self.clicked)            
    i=1
    k=21                    
    for i in range(0,rows):
         try:                   
          self.txb[k].text = ex[i]["nume"]
          self.txb[k+1].text = ex[i]["detalii"]                
          k=k+10
         except:
          pass  
       
    pass 
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.gru(3,10)
    pass

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    p1['gen']['tip'] = self.drop_down_1.selected_value
    pass

  def text_box_2_pressed_enter(self, **event_args):
    p1['gen']['name'] = self.text_box_2.text
    pass

  def button_2_click(self, **event_args):
    #print(p1['asoc'])                               
    g =  {"nume": "", "cota":"", "detalii": ""}
    p1['asoc'].append(g)                               
    
    row = len( p1['asoc'])
    print(row)                               
    self.gru(row,  p1['asoc'])                               
    pass






