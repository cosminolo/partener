from ._anvil_designer import verTemplate
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
import string

from datetime import date
import stripe.checkout
class ver(verTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)    
    self.clear_tva()    
    self.clear_bilant()
    self.ch_pan()
    global p1    
    p1 = anvil.server.call("get_p1", self.ups())
    global cui
    cui = p1['gen']['cui']
    global den 
    den = p1['gen']['name']
    self.text_box_1.text = den
    self.ref_buget("a")
    
    
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('init.crit')    
    pass
  def button_1_click(self, **event_args):
     open_form('init')
     pass
  def button_3_click(self, **event_args):
     open_form('init.st')
     pass

  def tva(self, tva):   
    try:      
      self.label_12.text = tva['cui']      
      self.label_13.text = tva['scpTVA']
      self.label_14.text = tva['data_inceput_ScpTVA']
      self.label_15.text = tva['statusRO_e_Factura']
      self.label_16.text = tva['statusInactivi']
      self.label_17.text = tva['statusTvaIncasare']
      self.label_18.text = tva['dataInceputTvaInc']
      self.label_19.text = tva['statusSplitTVA']
      self.label_20.text = tva['dataInceputSplitTVA']
      self.label_21.text = tva['mesaj_ScpTVA']
      self.label_23.text = tva['data']
    except:
      pass
    pass
  def clear_tva(self):      
      self.label_12.text = ""
      self.label_13.text = ""
      self.label_14.text = ""
      self.label_15.text = ""
      self.label_16.text = ""
      self.label_17.text = ""
      self.label_18.text = ""
      self.label_19.text = ""
      self.label_20.text = ""
      self.label_21.text = ""
      self.label_23.text = ""
      pass
  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          return us
      pass

  def bilant(self, a, b):        
      #time.sleep(1)
      try:
        bil = a      
        self.label_41.text = bil['an']
        self.label_42.text = "{:,}".format(bil['ACTIVEIMOBILIZATE-TOTAL'])
        self.label_43.text = "{:,}".format(bil['ACTIVECIRCULANTE-TOTAL,dincare:'])
        self.label_44.text = "{:,}".format(bil['Stocuri'])
        self.label_45.text = "{:,}".format(bil['Creante'])
        self.label_46.text = "{:,}".format(bil['Casaşiconturilabănci'])
        self.label_47.text = "{:,}".format(bil['CHELTUIELIINAVANS'])
        self.label_48.text = "{:,}".format(bil['DATORII'])
        self.label_49.text = "{:,}".format(bil['VENITURIINAVANS'])
        self.label_50.text = "{:,}".format(bil['PROVIZIOANE'])
        self.label_51.text = "{:,}".format(bil['CAPITALURI-TOTAL,dincare:'])
        self.label_52.text = "{:,}".format(bil['Capitalsubscrisvarsat'])
        self.label_53.text = "{:,}".format(bil['Patrimoniulregiei'])
        self.label_54.text = "{:,}".format(bil['Cifradeafacerineta'])
        self.label_55.text = "{:,}".format(bil['VENITURITOTALE'])
        self.label_56.text = "{:,}".format(bil['CHELTUIELITOTALE'])
        self.label_57.text = "{:,}".format(int(bil['Profitnet']) - int(bil['Pierdereneta']))
        self.label_59.text = "{:,}".format(bil['Numarmediudesalariati'])
      except:
        pass
      try:
        bil = b
        self.label_61.text = bil['an']
        self.label_62.text = "{:,}".format(bil['ACTIVEIMOBILIZATE-TOTAL'])
        self.label_63.text = "{:,}".format(bil['ACTIVECIRCULANTE-TOTAL,dincare:'])
        self.label_64.text = "{:,}".format(bil['Stocuri'])
        self.label_65.text = "{:,}".format(bil['Creante'])
        self.label_66.text = "{:,}".format(bil['Casaşiconturilabănci'])
        self.label_67.text = "{:,}".format(bil['CHELTUIELIINAVANS'])
        self.label_68.text = "{:,}".format(bil['DATORII'])
        self.label_69.text = "{:,}".format(bil['VENITURIINAVANS'])
        self.label_70.text = "{:,}".format(bil['PROVIZIOANE'])
        self.label_71.text = "{:,}".format(bil['CAPITALURI-TOTAL,dincare:'])
        self.label_72.text = "{:,}".format(bil['Capitalsubscrisvarsat'])
        self.label_73.text = "{:,}".format(bil['Patrimoniulregiei'])
        self.label_74.text = "{:,}".format(bil['Cifradeafacerineta'])
        self.label_75.text = "{:,}".format(bil['VENITURITOTALE'])
        self.label_76.text = "{:,}".format(bil['CHELTUIELITOTALE'])
        self.label_77.text = "{:,}".format(int(bil['Profitnet']) - int(bil['Pierdereneta']))
        self.label_78.text = "{:,}".format(bil['Numarmediudesalariati'])
      except:
        pass
      pass
   
  def clear_bilant(self):    
        self.label_41.text = ""
        self.label_42.text = ""
        self.label_43.text = ""
        self.label_44.text = ""
        self.label_45.text = ""
        self.label_46.text = ""
        self.label_47.text = ""
        self.label_48.text = ""
        self.label_49.text = ""
        self.label_50.text = ""
        self.label_51.text = ""
        self.label_52.text = ""
        self.label_53.text = ""
        self.label_54.text = ""
        self.label_55.text = ""
        self.label_56.text = ""
        self.label_57.text = ""
        self.label_59.text = ""        
        self.label_61.text = ""
        self.label_62.text = ""
        self.label_63.text = ""
        self.label_64.text = ""
        self.label_65.text = ""
        self.label_66.text = ""
        self.label_67.text = ""
        self.label_68.text = ""
        self.label_69.text = ""
        self.label_70.text = ""
        self.label_71.text = ""
        self.label_72.text = ""
        self.label_73.text = ""
        self.label_74.text = ""
        self.label_75.text = ""
        self.label_76.text = ""
        self.label_77.text = ""
        self.label_78.text = ""
        pass

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    re = anvil.server.call("prel_js_gol", self.ups(),2)
    print(re['buget'])
    pass

  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.text_box_1.text = self.item[ 'denumire' ]
    pass
  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
   

    # Take a payment of £9.99
    c= stripe.checkout.charge(amount=1000,
                           currency="RON",
                           title="verificare",
                           description="info tva")
    print (c["result"])
    pass

  def button_4_click(self, **event_args):      
      get_tva = json.loads(anvil.server.call("is_1", cui))
     
      #anvil.server.call("tva_js", self.ups(), get_tva)
      self.clear_tva()      
      self.tva(get_tva)
      pass

  def button_7_click(self, **event_args):
    self.clear_bilant()
    an = str(int(date.today().year))   
    c = json.loads(anvil.server.call("is_2", an, cui))
    #anvil.server.call("bil_js", self.ups(), c, 1 ) 
    print (c)
    ann = str(int(c['an'])-1)      
    d = json.loads(anvil.server.call("is_2", ann, cui))
    #anvil.server.call("bil_js", self.ups(), d, 2 )        
    self.bilant(d, c)
    pass

  def button_8_click(self, **event_args):
    self.ref_buget("b")
    pass
  def ref_buget(self, tip):
    self.label_79.text = ""
    self.label_80.text = ""
    self.label_81.text = ""
    self.label_83.text = ""
    self.label_87.text = ""
    self.label_89.text = ""
    self.label_90.text = ""
    self.label_96.text = ""
    us = str(self.ups()).strip()
    if tip == "b":
      rbb = json.loads(anvil.server.call("rest_buget", us, den, cui))    
      if len(rbb)>0:
        p1['buget'].update(rbb)
        p1['buget']['datav'] = str(date.today().isoformat())
      else:      
        p1['buget']['nume'] = den
        p1['buget']['cui'] = cui
        p1['buget']['obs'] = "Nu are restante la finele ultimului trimestru"
        p1['buget']['datav'] = str(date.today().isoformat())
      anvil.server.call("sp1", self.ups(), p1)
      self.label_79.text = p1['buget']['bs']
      self.label_80.text = p1['buget']['bss']
      self.label_81.text = p1['buget']['bas']
      self.label_83.text = p1['buget']['bass']
      self.label_87.text = p1['buget']['cui']
      self.label_89.text = p1['buget']['total']
      self.label_90.text = p1['buget']['obs']
      self.label_96.text = p1['buget']['datav']
    if tip == "a":
      self.label_79.text = p1['buget']['bs']
      self.label_80.text = p1['buget']['bss']
      self.label_81.text = p1['buget']['bas']
      self.label_83.text = p1['buget']['bass']
      self.label_87.text = p1['buget']['cui']
      self.label_89.text = p1['buget']['total']
      self.label_90.text = p1['buget']['obs']
      self.label_96.text = p1['buget']['datav']
    pass
  
  def ps(self, sst):
    s=""
    st=str(sst)
    for i in st:
       if i.isnumeric() or i=="," or i.isalpha():
        s = s + i
    return s

  def button_9_click(self, **event_args): 
    self.drop_down_1.selected_value = ""
    self.drop_down_2.selected_value = ""
    den = self.text_box_1.text.strip()
    li = anvil.server.call("litigii", den)
    anvil.server.call("s_lit", self.ups(), li)    
    lit = json.loads(li)
    cal = []
    calitate =[""]
    ob = []
    obiect=[""]
    if len(lit) > 1:
     for i in range(0, len(lit)):
      cal.append(lit[i]['calitate'])
      [calitate.append(x) for x in cal if x not in calitate]
      ob.append(lit[i]['obiect'])
      [obiect.append(x) for x in ob if x not in obiect]
     self.drop_down_1.items = calitate
     self.drop_down_2.items = obiect    
     self.repeating_panel_1.items = lit
    else:
        self.repeating_panel_1.items = []
        if lit[0]["denumire"] == "nu inregistreaza":
          n = Notification("",
             title=lit[0]["denumire"]).show()
          time.sleep(1)
          n.hide()
        else:
          n = Notification("",
             title=lit[0]["denumire"]).show()
          time.sleep(1)
          n.hide()
    pass

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_1.selected_value != "":
      filt = []
      s1 = self.repeating_panel_1.items
      for i in range(0, len(s1)):
        if s1[i]['calitate'] == self.drop_down_1.selected_value.strip():
          f = s1[i]
          filt.append(f)
      self.repeating_panel_1.items = filt    
    pass

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_2.selected_value != "":
      filt = []
      s1 = self.repeating_panel_1.items
      for i in range(0, len(s1)):
        if s1[i]['obiect'] == self.drop_down_2.selected_value.strip():
          f = s1[i]
          filt.append(f)
      self.repeating_panel_1.items = filt   
    pass
  def ch_pan(self):
    li= anvil.server.call('get_lit', self.ups())    
    try:
      lit = json.loads(li)
      if len(lit)>0:
         self.repeating_panel_1.items = lit
    except:
        pass
    pass













