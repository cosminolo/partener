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
    self.con_drop3()
    
    global p1
    #p1 = anvil.server.call("pri_ini")
    p1 = anvil.server.call("get_p1", self.ups())
    self.item = p1
    try:
      row = len(p1['admin'])
      self.admin(row, p1['admin'])
    except:
      pass
    try:
      row = len(p1['asoc'])
      self.asoc(row, p1['asoc'])      
    except:
      pass
    try:
      row = len(p1['grp'])
      self.grup(row, p1['grp'])      
    except:
      pass
    try:
      row = len(p1['garantii'])
      self.gar(row, p1['garantii'])      
    except:
      pass
    
    
  def text_box_1_pressed_enter(self, **event_args):
   try: 
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
    p1["admin"] = []    
    for i in range (0, len(grup['admin'])):      
      p1["admin"].append({"nume": grup['admin'][i]['nume']})
    row = len(p1['admin'])
    self.admin(row, p1['admin'])
    
    p1["asoc"] = []
    for i in range (0, len(grup['asoct'])): 
      n = {"nume": grup['asoct'][i]['nume'], "tara": grup['asoct'][i]['tara'], "info": grup['asoct'][i]['info']}
      p1["asoc"].append(n)      
    row = len(p1['asoc'])
    self.asoc(row, p1['asoc']) 
    anvil.server.call("sp1", self.ups(), p1)
    
    p1["grp"] = []    
    for i in range (0, len(grup['gr'])):
      nu = grup['gr'][i]['nume']
      det = grup['gr'][i]['detalii']
      obs = "x"
      try:
        obs = grup['gr'][i]['obbs']
      except:
        pass
      n = {"nume": nu, "detalii": det, "obs": obs}
      p1["grp"].append(n)      
    row = len(p1['grp'])
    self.grup(row, p1['grp']) 
    anvil.server.call("sp1", self.ups(), p1)
   except:
    pass
   pass
  def admin(self, rows, ex):
    self.grid_panel_1.clear()
    global txb
    txb = self.txb = {}    
    i = 1
    j = 0    
    k=10                          
    for j in range (2,rows+2): # rows       
      for i in range(1,3):
        if i ==1:
          k=j*10+i        
          self.txb[k] = TextArea(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=300,
                              foreground="#000",background="#fff"")
          self.txb[k].role = "scroll"
          self.txb[k].tag.name = k                           
          self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=0, width_xs=7)
        if i == 2:  
          k=j*10+i                       
          self.txb[k] = Button(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=10,                              
                              align = "centre",  
                              foreground="#000",background="#fff"")
          self.txb[k].tag.name = k
          self.txb[k].text = "X"
          self.txb[k].role = "raised"                     
          self.grid_panel_1.add_component(self.txb[k], row=j, col_xs=8, width_xs=1)
          self.txb[k].set_event_handler('click', self.l_focus)                                               
    i=1
    k=21                    
    for i in range(0,rows):
      try:                   
          self.txb[k].text = ex[i]["nume"]                         
          k=k+10
      except:
          pass       
    pass
  def l_focus (self, sender,**event_args):
    tg = int(sender.tag.name)
    self.txb[tg-1].text = ""
    pass                                 
  

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_1.selected_value:
        anvil.server.call("sp1", self.ups(), p1)                           
                             
    pass

  

  def button_2_click(self, **event_args):                                  
    g =  {"nume": " "}
    p1['admin'].append(g)                               
    row = len( p1['admin'])                                 
    self.admin(row,  p1['admin'])                               
    pass
  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          return us
      pass     
  def asoc(self, rows, ex):
    self.grid_panel_3.clear()    
    #tb = self.tb = {}   
    i = 1
    j = 0    
    k=100                          
    for j in range (2,rows+2): # rows
      for i in range (1,5):
        if i == 1:                      
          k=100+j*10+i          
          self.txb[k] = TextArea(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=280,
                              align = "left",    
                              foreground="#000",background="#fff"")
          self.txb[k].role = "scroll"
                                 
          self.txb[k].tag.name = k                           
          self.grid_panel_3.add_component(self.txb[k], row=j, col_xs=0, width_xs=6)
          #self.txb[k].set_event_handler('lost_focus', self.ll_focus)
        if i == 2:
          k=100+j*10+i        
          self.txb[k] = TextArea(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=80,
                              align = "left",   
                              foreground="#000",background="#fff"")
          self.txb[k].role = "scroll"
          self.txb[k].tag.name = k                           
          self.grid_panel_3.add_component(self.txb[k], row=j, col_xs=6, width_xs=2)
          #self.txb[k].set_event_handler('lost_focus', self.ll_focus)                        
        if i == 3:
          k=100+j*10+i        
          self.txb[k] = TextArea(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=90,
                              align = "left",   
                              foreground="#000",background="#fff"")
          self.txb[k].role = "scroll"
          self.txb[k].tag.name = k                           
          self.grid_panel_3.add_component(self.txb[k], row=j, col_xs=8, width_xs=2)
          #self.txb[k].set_event_handler('lost_focus', self.ll_focus) 
        if i == 4:
          k=100+j*10+i        
          self.txb[k] = Button(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=10,                              
                              align = "centre",  
                              foreground="#000",background="#fff"")
          self.txb[k].tag.name = k
          self.txb[k].text = "X"
          self.txb[k].role = "raised"                     
          self.grid_panel_3.add_component(self.txb[k], row=j, col_xs=10, width_xs=1)
          self.txb[k].set_event_handler('click', self.ll_focus)                        
                                 
    i=1
    k=100+21    
    for i in range(0,rows):
      try:                              
          self.txb[k].text = ex[i]["nume"]         
          self.txb[k+1].text = ex[i]["tara"]
          self.txb[k+2].text = ex[i]["info"]                       
          k=k+10
      except:
          pass       
    pass                            
  def ll_focus(self, sender,**event_args):
    tg = int(sender.tag.name)
    self.txb[tg-1].text = ""
    self.txb[tg-2].text = ""
    self.txb[tg-3].text = ""                     
    
    pass
  def button_3_click(self, **event_args):
    g =  {"nume": " ", "tara": " ", "info": " "}
    p1['asoc'].append(g)                               
    row = len( p1['asoc'])                                 
    self.asoc(row,  p1['asoc'])                                  
    pass

  def button_5_click(self, **event_args):
    c =0
    li =[]                           
    for it in self.grid_panel_3.get_components():       
       if type(it) == TextArea:
          c = c+1                     
          if it.text !="":
              if c ==1:                 
                nume = it.text
              if c ==2:
                 tara = it.text
              if c == 3:
                 info = it.text                               
                 li.append({"nume": nume, "tara": tara, "info": info})
                 nume = ""
                 tara = "" 
                 info = ""
                 c = 0              
    p1['asoc'] = li                             
    anvil.server.call("sp1", self.ups(), p1)   
    row = len(p1['asoc'])
    self.asoc(row, p1['asoc'])  
    pass

  def button_6_click(self, **event_args):
    li = []
    for it in self.grid_panel_1.get_components():
       if type(it) == TextArea:
         if it.text != "":                          
          ta = {"nume": it.text}
          li.append(ta)
    p1['admin'] = li
    anvil.server.call("sp1", self.ups(), p1)   
    row = len(p1['admin'])
    self.admin(row, p1['admin'])                           
    pass
  def grup(self, rows, ex):
    self.grid_panel_2.clear()    
    #tb = self.tb = {}   
    i = 1
    j = 0    
    k=200                          
    for j in range (2,rows+2): # rows
      for i in range (1,5):
        if i == 1:                      
          k=200+j*10+i          
          self.txb[k] = TextArea(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=280,
                              align = "left",    
                              foreground="#000",background="#fff"")
          self.txb[k].role = "scroll"
          self.txb[k].tag.name = k                           
          self.grid_panel_2.add_component(self.txb[k], row=j, col_xs=0, width_xs=4)
          #self.txb[k].set_event_handler('lost_focus', self.ll_focus)
        if i == 2:
          k=200+j*10+i        
          self.txb[k] = TextArea(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=400,
                              align = "left",   
                              foreground="#000",background="#fff"")
          self.txb[k].role = "scroll"
          self.txb[k].tag.name = k                           
          self.grid_panel_2.add_component(self.txb[k], row=j, col_xs=0, width_xs=4)
          #self.txb[k].set_event_handler('lost_focus', self.ll_focus)                        
        if i == 3:
          k=200+j*10+i        
          self.txb[k] = TextArea(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=100,
                              align = "left",   
                              foreground="#000",background="#fff"")
          self.txb[k].role = "scroll"
          self.txb[k].tag.name = k                           
          self.grid_panel_2.add_component(self.txb[k], row=j, col_xs=0, width_xs=3)
          #self.txb[k].set_event_handler('lost_focus', self.ll_focus) 
        if i == 4:
          k=200+j*10+i        
          self.txb[k] = Button(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=10,                              
                              align = "centre",  
                              foreground="#000",background="#fff"")
          self.txb[k].tag.name = k
          self.txb[k].text = "X"
          self.txb[k].role = "raised"                     
          self.grid_panel_2.add_component(self.txb[k], row=j, col_xs=0, width_xs=1)
          self.txb[k].set_event_handler('click', self.ll_focus)                       
    i=1
    k=200+21    
    for i in range(0,rows):
      try:                              
          self.txb[k].text = ex[i]["nume"]         
          self.txb[k+1].text = ex[i]["detalii"]
          self.txb[k+2].text = ex[i]["obs"]                       
          k=k+10
      except:
          pass       
    pass                                                         

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    g =  {"nume": " ", "detalii": " ", "obs": " "}
    p1['grp'].append(g)                               
    row = len( p1['grp'])                                 
    self.grup(row,  p1['grp'])                             
    pass

  def button_7_click(self, **event_args):
    c =0
    li =[]
    nume = ""
    detalii = "" 
    obs = ""                           
    for it in self.grid_panel_2.get_components():       
       if type(it) == TextArea:
          c = c+1                     
          if it.text !="":
              if c ==1:                 
                nume = it.text
              if c ==2:
                 detalii = it.text
              if c == 3:
                 obs = it.text                               
                 li.append({"nume": nume, "detalii": detalii, "obs": obs})
                 nume = ""
                 detalii = "" 
                 obs = ""
                 c = 0             
    p1['grp'] = li                             
    anvil.server.call("sp1", self.ups(), p1)   
    row = len(p1['grp'])
    self.grup(row, p1['grp'])  
    pass

  
  def drop_down_8_change(self, **event_args):
    if self.drop_down_8.selected_value:
        anvil.server.call("sp1", self.ups(), p1)
    pass
  
  def drop_down_2_change(self, **event_args):
    if self.drop_down_2.selected_value == 'garantat cu echipamente/imobile/etc' or self.drop_down_2.selected_value == 'garantat cu mix (fond si alte garantii)':
       self.drop_down_3.items = []
       for art in ['Linie de Credit - acordare/suplimentare', 
                'Linie de Credit - acordare/suplimentare',
                'Linie de Credit - prelungire',
                'Linie de Credit - suplimentare 10%',
                'Credit pentru finantarea activitatii curente',
                'Credit pentru achitarea datoriilor la buget',
                'Credit ipotecar pentru investitii acordat PJ',
                'Credit de investitii',
                'Credit de investitii pentru achizia de teren pentru productia agricola']:
          self.drop_down_3.items.append(art)
       self.drop_down_3.items = self.drop_down_3.items
    if self.drop_down_2.selected_value == 'negarantat':
      self.drop_down_3.items = []
      for art in ['Descoperit de Cont pe Card Business - Client Nou, cu expunere sub 6 luni', 
                'Descoperit de Cont pe Card Business - Client Existent, cu expunere de peste 6 luni',
                'Visa Business'] :
         self.drop_down_3.items.append(art)
      self.drop_down_3.items = self.drop_down_3.items
      
    if self.drop_down_2.selected_value == 'valoare mica cu FGCR':
      self.drop_down_3.items = []
      for art in ['Activitate curenta agricultura 500 mii-FGCR', 
                'Investitii in agricultura 500 mii-FGCR',
                'Activitate curenta si investitii in agricultura 500 mii-FGCR'] :
          self.drop_down_3.items.append(art)
      self.drop_down_3.items = self.drop_down_3.items  
    if self.drop_down_2.selected_value == 'OUG 43':
      self.drop_down_3.items = []
      for art in ['Credit pentru finantarea activitatii curente OUG 43/2013', 
                'Credit pentru finantarea investitiilor in domeniul agricol OUG 43/2013',
                'Credit pentru achizitia terenurilor cu destinatie agricola OUG 43/2013'] :
          self.drop_down_3.items.append(art)
      self.drop_down_3.items = self.drop_down_3.items     
      
    if self.drop_down_2.selected_value:
        anvil.server.call("sp1", self.ups(), p1)                         
    pass

  def drop_down_3_change(self, **event_args):
    if self.drop_down_3.selected_value:
        anvil.server.call("sp1", self.ups(), p1) 
    pass

  def drop_down_5_change(self, **event_args):
    if self.drop_down_5.selected_value:
        anvil.server.call("sp1", self.ups(), p1) 
    pass

  def text_box_9_lost_focus(self, **event_args):
    anvil.server.call("sp1", self.ups(), p1) 
    pass

  def text_box_10_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def text_box_10_lost_focus(self, **event_args):
    anvil.server.call("sp1", self.ups(), p1)
    pass

  def text_area_1_lost_focus(self, **event_args):
    anvil.server.call("sp1", self.ups(), p1)
    pass

  def text_area_2_lost_focus(self, **event_args):
    anvil.server.call("sp1", self.ups(), p1)
    pass
  def con_drop3(self):
    self.drop_down_3.items = []
    for art in [' ', 'Linie de Credit - acordare/suplimentare', 
                'Linie de Credit - acordare/suplimentare',
                'Linie de Credit - prelungire',
                'Linie de Credit - suplimentare 10%',
                'Credit pentru finantarea activitatii curente',
                'Credit pentru achitarea datoriilor la buget',
                'Credit ipotecar pentru investitii acordat PJ',
                'Credit de investitii',
                'Credit de investitii pentru achizia de teren pentru productia agricola',
                'Descoperit de Cont pe Card Business - Client Nou, cu expunere sub 6 luni', 
                'Descoperit de Cont pe Card Business - Client Existent, cu expunere de peste 6 luni',
                'Visa Business',
                'Activitate curenta agricultura 500 mii-FGCR', 
                'Investitii in agricultura 500 mii-FGCR',
                'Activitate curenta si investitii in agricultura 500 mii-FGCR' ,
                'Credit pentru finantarea activitatii curente OUG 43/2013', 
                'Credit pentru finantarea investitiilor in domeniul agricol OUG 43/2013',
                'Credit pentru achizitia terenurilor cu destinatie agricola OUG 43/2013']:
  
          self.drop_down_3.items.append(art)
    self.drop_down_3.items = self.drop_down_3.items

  def text_box_2_lost_focus(self, **event_args):
    anvil.server.call("sp1", self.ups(), p1)
    pass

  def text_box_3_lost_focus(self, **event_args):
    anvil.server.call("sp1", self.ups(), p1)
    pass

  def text_box_5_lost_focus(self, **event_args):
    anvil.server.call("sp1", self.ups(), p1)
    pass

  def text_box_6_lost_focus(self, **event_args):
    anvil.server.call("sp1", self.ups(), p1)
    pass

  def text_box_7_lost_focus(self, **event_args):
    anvil.server.call("sp1", self.ups(), p1)
    pass

  def text_box_8_lost_focus(self, **event_args):
    anvil.server.call("sp1", self.ups(), p1)
    pass

  def text_box_11_lost_focus(self, **event_args):
    anvil.server.call("sp1", self.ups(), p1)
    pass

  def drop_down_7_change(self, **event_args):
    if self.drop_down_7.selected_value:
        anvil.server.call("sp1", self.ups(), p1)
    pass

  def text_box_4_lost_focus(self, **event_args):
    anvil.server.call("sp1", self.ups(), p1)
    pass

  def drop_down_6_change(self, **event_args):
    if self.drop_down_6.selected_value:
        anvil.server.call("sp1", self.ups(), p1)
    pass

  def drop_down_9_change(self, **event_args):
    if self.drop_down_9.selected_value:
        anvil.server.call("sp1", self.ups(), p1)
    pass

  def drop_down_10_change(self, **event_args):
    if self.drop_down_10.selected_value:
        anvil.server.call("sp1", self.ups(), p1)
    pass

  def drop_down_11_change(self, **event_args):
    if self.drop_down_11.selected_value:
        anvil.server.call("sp1", self.ups(), p1)
    pass

  def drop_down_12_change(self, **event_args):
    if self.drop_down_12.selected_value:
        anvil.server.call("sp1", self.ups(), p1)
    pass

  def drop_down_13_change(self, **event_args):
    if self.drop_down_13.selected_value:
        anvil.server.call("sp1", self.ups(), p1)
    pass

  def drop_down_14_change(self, **event_args):
    if self.drop_down_14.selected_value:
        anvil.server.call("sp1", self.ups(), p1)
    pass

  def drop_down_15_change(self, **event_args):
    if self.drop_down_15.selected_value:
        anvil.server.call("sp1", self.ups(), p1)
    pass

  def drop_down_4_change(self, **event_args):
    if self.drop_down_4.selected_value:
        anvil.server.call("sp1", self.ups(), p1)
    pass

  
  def text_box_8_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  

  def text_area_3_lost_focus(self, **event_args):
    anvil.server.call("sp1", self.ups(), p1)
    pass

  def button_8_click(self, **event_args):
    open_form('init')
    pass

  def button_9_click(self, **event_args):
    open_form('init.verific')
    pass

  def button_1_click(self, **event_args):
    
    # Take a payment of £9.99
    c= stripe.checkout.charge(amount=100,
                           currency="EUR",
                           title="Raport",
                           description="verificari")
    print (c["result"])
    pass

  def text_area_2_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass
                               
  def gar(self, rows, ex):
    self.grid_panel_4.clear()    
    #tb = self.tb = {}   
    i = 1
    j = 0    
    k=300                          
    for j in range (2,rows+2): # rows
      for i in range (1,5):
        if i == 1:                      
          k=300+j*10+i          
          self.txb[k] = TextArea(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=280,
                              align = "left",    
                              foreground="#000",background="#fff"")
          self.txb[k].role = "scroll"
                                 
          self.txb[k].tag.name = k                           
          self.grid_panel_4.add_component(self.txb[k], row=j, col_xs=0, width_xs=6)
          #self.txb[k].set_event_handler('lost_focus', self.ll_focus)
        if i == 2:
          k=300+j*10+i        
          self.txb[k] = TextArea(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=80,
                              align = "left",   
                              foreground="#000",background="#fff"")
          self.txb[k].role = "scroll"
          self.txb[k].tag.name = k                           
          self.grid_panel_4.add_component(self.txb[k], row=j, col_xs=6, width_xs=2)
          #self.txb[k].set_event_handler('lost_focus', self.ll_focus)                        
        if i == 3:
          k=300+j*10+i        
          self.txb[k] = TextArea(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=90,
                              align = "left",   
                              foreground="#000",background="#fff"")
          self.txb[k].role = "scroll"
          self.txb[k].tag.name = k                           
          self.grid_panel_4.add_component(self.txb[k], row=j, col_xs=8, width_xs=2)
          #self.txb[k].set_event_handler('lost_focus', self.ll_focus) 
        if i == 4:
          k=300+j*10+i        
          self.txb[k] = Button(font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "small",
                              width=10,                              
                              align = "centre",  
                              foreground="#000",background="#fff"")
          self.txb[k].tag.name = k
          self.txb[k].text = "X"
          self.txb[k].role = "raised"                     
          self.grid_panel_4.add_component(self.txb[k], row=j, col_xs=10, width_xs=1)
          self.txb[k].set_event_handler('click', self.lll_focus)                        
                                 
    i=1
    k=300+21    
    for i in range(0,rows):
      try:                              
          self.txb[k].text = ex[i]["tip"]         
          self.txb[k+1].text = ex[i]["prop"]
          self.txb[k+2].text = ex[i]["data_a"]                       
          k=k+10
      except:
          pass       
    pass                            
  def lll_focus(self, sender,**event_args):
    tg = int(sender.tag.name)
    self.txb[tg-1].text = ""
    self.txb[tg-2].text = ""
    self.txb[tg-3].text = ""                     
    
    pass                             

  def button_10_click(self, **event_args):
    """This method is called when the button is clicked"""
    g =  {"tip": " ", "prop": " ", "data_a": " "}
    p1['garantii'].append(g)                               
    row = len( p1['garantii'])                                 
    self.gar(row,  p1['garantii'])                           
    pass

  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    c =0
    li =[]                           
    for it in self.grid_panel_4.get_components():       
       if type(it) == TextArea:
          c = c+1                     
          if it.text !="":
              if c ==1:                 
                tip = it.text
              if c ==2:
                 prop = it.text
              if c == 3:
                 data_a = it.text                               
                 li.append({"tip": tip, "tara": prop, "data_a": data_a})
                 tip = ""
                 prop = "" 
                 data_a = ""
                 c = 0              
    p1['garantii'] = li                             
    anvil.server.call("sp1", self.ups(), p1)   
    row = len(p1['garantii'])
    self.gar(row, p1['garantii'])                             
    pass














































