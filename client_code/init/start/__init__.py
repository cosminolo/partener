from ._anvil_designer import startTemplate
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
import time
from datetime import date
class start(startTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.con_drop1()
    self.con_drop2() 
    self.con_drop3()
    global js_lucru
    js_lucru = anvil.server.call("prel_js_gol", self.ups(), 2)    
    self.item = js_lucru
    if self.drop_down_2.selected_value != "":
     self.drop_down_2_change()
    
  def con_drop1(self):
    self.drop_down_1.items = []
    for art in [' ', 'S.R.L.', 'S.A', 'PFA', 'II', 'SRL-D']:
      self.drop_down_1.items.append(art)
      self.drop_down_1.items = self.drop_down_1.items
    self.drop_down_4.items = []
    for art in [' ','Lei', 'Eur', 'Usd']:
      self.drop_down_4.items.append(art)
    self.drop_down_4.items = self.drop_down_4.items
    self.drop_down_5.items = []
    for art in [' ', 'Agricultura', 'Comert', 'Constructii', 'Industrie',
                'Servicii', 'Transporturi', 'Turism','Alte ramuri']:
      self.drop_down_5.items.append(art)
    self.drop_down_5.items = self.drop_down_5.items  
    self.drop_down_6.items = []
    for art in [' ','DA', 'NU']:
      self.drop_down_6.items.append(art)
    self.drop_down_6.items = self.drop_down_6.items  
    self.drop_down_7.items = []
    for art in [' ', '0', 'Intre 1 si sub 10 salariati',
                'Intre 10 si sub 50 salariati', 'Peste 50 de salariati']:
      self.drop_down_7.items.append(art)
    self.drop_down_7.items = self.drop_down_7.items 
    self.drop_down_8.items = []
    for art in [' ','Clientul este  vizibil intr-o piata cu acoperire nationala/internationala',
                'Clientul este  vizibil intr-o piata regionala',
                'Clientul este  vizibil intr-o piata limitata la 2 judete',
                'Clientul are o vizibilitate redusa in piata de profil']:
      self.drop_down_8.items.append(art)
    self.drop_down_8.items = self.drop_down_8.items   
    self.drop_down_9.items = []
    for art in [' ','Competitie ridicata cu intrare grea pe piata',
                'Competitie redusa cu intrare grea pe piata',
                'Competitie redusa cu intrare usoara pe piata',
                'Competitie inexistenta (nisa de piata)']:
      self.drop_down_9.items.append(art)
    self.drop_down_9.items = self.drop_down_9.items    
    self.drop_down_10.items = []
    for art in [' ','Neagresiva, merge cu produse de inalta calitate',
                'Neagresiva, mizeaza pe volumul produselor comercializate',
                'Agresiva, merge cu produse exclusiviste',
                'Nu are strategie, se acomodeaza pietei']:
      self.drop_down_10.items.append(art)
    self.drop_down_10.items = self.drop_down_10.items    
    self.drop_down_11.items = []
    for art in [' ','Management experimentat cu functiile executive separate',
                'Management experimentat fara functii executive separate',
                'Management fara experienta si fara functii executive separate',
                'Activitatea depinde de o persoana cheie']:
      self.drop_down_11.items.append(art)
    self.drop_down_11.items = self.drop_down_11.items    
    
    pass
  def con_drop2(self):
    self.drop_down_2.items = []
    for art in [' ','negarantat', 'valoare mica cu FGCR', 'OUG 43',  'garantat cu echipamente/imobile/etc', 'garantat cu mix (fond si alte garantii)']:
      self.drop_down_2.items.append(art)
    self.drop_down_2.items = self.drop_down_2.items
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
    pass
  def drop_down_2_change(self, **event_args):
    if self.drop_down_2.selected_value == 'garantat cu echipamente/imobile/etc' or self.drop_down_2.selected_value == 'garantat cu mix (fond si alte garantii)':
       self.drop_down_3.items = []
       for art in [' ', 'Linie de Credit - acordare/suplimentare', 
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
      for art in [' ', 'Descoperit de Cont pe Card Business - Client Nou, cu expunere sub 6 luni', 
                'Descoperit de Cont pe Card Business - Client Existent, cu expunere de peste 6 luni',
                'Visa Business'] :
         self.drop_down_3.items.append(art)
      self.drop_down_3.items = self.drop_down_3.items
      
    if self.drop_down_2.selected_value == 'valoare mica cu FGCR':
      self.drop_down_3.items = []
      for art in [' ', 'Activitate curenta agricultura 500 mii-FGCR', 
                'Investitii in agricultura 500 mii-FGCR',
                'Activitate curenta si investitii in agricultura 500 mii-FGCR'] :
          self.drop_down_3.items.append(art)
      self.drop_down_3.items = self.drop_down_3.items  
    if self.drop_down_2.selected_value == 'OUG 43':
      self.drop_down_3.items = []
      for art in [' ', 'Credit pentru finantarea activitatii curente OUG 43/2013', 
                'Credit pentru finantarea investitiilor in domeniul agricol OUG 43/2013',
                'Credit pentru achizitia terenurilor cu destinatie agricola OUG 43/2013'] :
          self.drop_down_3.items.append(art)
      self.drop_down_3.items = self.drop_down_3.items     
      
    if self.drop_down_2.selected_value:
        self.up_json()  
    pass

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    open_form('init')
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    # btn = Button(text="Click me!")
    #self.xy_panel_2.add_component(btn, x=0, y=1, width=50)
    
    ret_js = json.loads(anvil.server.call("is_1", "14446543"))
    
    print(ret_js['nume'])
    pass

  

  
  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          return us
      pass
  def button_3_click(self, **event_args):
    
   if self.drop_down_1.selected_value.strip() in ("S.R.L.", "S.A", "SRL-D"):
      open_form('init.verific')
   pass

  
  
  def up_json(self):      
      #x = json.dumps(self.item, indent=4)
      anvil.server.call("upp_js", self.ups(), js_lucru) 
      self.item = js_lucru
      pass

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_1.selected_value:
        self.up_json() 
    pass

  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    if self.text_box_1.text.strip():
      self.up_json()  
    pass

  def drop_down_3_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_3.selected_value:
       self.up_json() 
    pass

  def drop_down_4_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_4.selected_value:
        self.up_json() 
    pass

  def drop_down_5_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_5.selected_value:
        self.up_json() 
    pass

  def drop_down_6_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_6.selected_value:
        self.up_json() 
    pass

  def drop_down_7_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_7.selected_value:
        self.up_json() 
    pass

  def drop_down_8_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_8.selected_value:
        self.up_json() 
    pass

  def drop_down_9_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_9.selected_value:
        self.up_json() 
    pass

  def drop_down_10_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_10.selected_value:
        self.up_json() 
    pass

  def drop_down_11_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_11.selected_value:
        self.up_json() 
    pass

 


  def text_area_1_lost_focus(self, **event_args):
    """This method is called when the text area loses focus"""
    if self.text_area_1.text.strip():
      self.up_json()  
    pass

  def text_area_2_lost_focus(self, **event_args):
    """This method is called when the text area loses focus"""
    if self.text_area_2.text.strip():
      self.up_json()  
    pass

  def text_area_4_lost_focus(self, **event_args):
    """This method is called when the text area loses focus"""
    if self.text_area_4.text.strip():
      self.up_json()  
    pass

  def text_box_6_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    if self.text_box_6.text.strip():
      self.up_json()  
    pass

  def text_area_3_lost_focus(self, **event_args):
    """This method is called when the text area loses focus"""
    if self.text_area_3.text.strip():
      self.up_json()  
    pass

  
 


  def text_box_8_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    if 1 == 1:
      js_tva = anvil.server.call("is_1", self.text_box_2.text)
      anvil.server.call("tva_js", self.ups(), js_tva )
      ret_js = json.loads(js_tva)
      self.text_box_3.text = ret_js["denumire"]
      js_lucru['den'] = ret_js["denumire"]      
      self.text_box_4.text = ret_js["adresa"]
      js_lucru['sediu'] = ret_js["adresa"] 
      self.text_box_7.text = ret_js["nrRegCom"]
      js_lucru['onrc'] = ret_js["nrRegCom"] 
      self.text_box_6.text = ret_js["telefon"]    
      js_lucru['telef'] = ret_js["telefon"] 
    #except:
      self.text_box_3.text = ""
      self.text_box_4.text = ""
      self.text_box_7.text = ""
      self.text_box_6.text = "" 
     
    try:
      an = int(date.today().year)      
      ret_js2 = json.loads(anvil.server.call("is_2", an, self.text_box_2.text))
      self.text_box_5.text = ret_js2["caen"]
      js_lucru['caen'] = ret_js["caen"] 
      anvil.server.call("bil_js", self.ups(), ret_js2, 1 )
      
    except:
      self.text_box_5.text = ""
      
      try:    
       an = str(int(date.today().year) - 1)       
       js_bil= anvil.server.call("is_2", an, self.text_box_2.text)
       ret_js2 = json.loads(js_bil)
       self.text_box_5.text = ret_js2["caen"] 
       js_lucru['caen'] = ret_js["caen"]  
       anvil.server.call("bil_js", self.ups(), js_bil, 1)
       
      except:
           self.text_box_5.text = ""
           try:    
              an = str(int(date.today().year) - 2)             
              ret_js2 = json.loads(anvil.server.call("is_2", an, self.text_box_2.text))
              self.text_box_5.text = ret_js2["caen"] 
              js_lucru['caen'] = ret_js["caen"] 
              anvil.server.call("bil_js", self.ups(), ret_js2, 1)
              
           except:
              self.text_box_5.text = ""
              pass
      
      self.up_json()      
      ann = str(int(date.today().year) - 2) 
      #time.sleep(2.5)
      b = anvil.server.call("is_2", ann, self.text_box_2.text)
      anvil.server.call("bil_js", self.ups(), b, 2)
    pass

  def text_box_3_lost_focus(self, **event_args):
    if self.text_box_3.text.strip():      
       js_lucru['den'] = self.text_box_3.text
       self.up_json()     
    pass

  def text_box_7_lost_focus(self, **event_args):
    if self.text_box_7.text.strip():
       self.up_json()    
    pass

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    
    pass

  def text_box_4_lost_focus(self, **event_args):
    if self.text_box_4.text.strip():
       self.up_json() 
    pass

  def text_box_5_lost_focus(self, **event_args):
    if self.text_box_5.text.strip():
       self.up_json() 
    pass








  










 





























