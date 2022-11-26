from ._anvil_designer import verificTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json
import time
import string

from datetime import date
import stripe.checkout
class verific(verificTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties) 
    
    global p1    
    p1 = anvil.server.call("get_p1", self.ups())
    global cui
    cui = str(p1['gen']['cui'])
    global den 
    den = p1['gen']['name']
    self.text_box_1.text = den
    self.ref_buget("a") 
    self.tva("a")
    try:
        self.ref_lit("a")
    except:
      pass
    self.get_bil("a")
    
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('init.crit')    
    pass
  def button_1_click(self, **event_args):
     open_form('init')
     pass
  def button_3_click(self, **event_args):
     open_form('init.fin')
     pass
  def tva(self, tip):
    if tip == "b":
      gt = json.loads(anvil.server.call("is_1", cui))
      p1['tva']['cui'] = gt['cui']      
      p1['tva']['scpTVA'] = gt['scpTVA']
      p1['tva']['data_inceput_ScpTVA'] = gt['data_inceput_ScpTVA']
      p1['tva']['statusRO_e_Factura'] = gt['statusRO_e_Factura']
      p1['tva']['statusInactivi'] = gt['statusInactivi']
      p1['tva']['statusTvaIncasare'] = gt['statusTvaIncasare']
      p1['tva']['dataInceputTvaInc'] = gt['dataInceputTvaInc']
      p1['tva']['statusSplitTVA'] = gt['statusSplitTVA']
      p1['tva']['dataInceputSplitTVA'] = gt['dataInceputSplitTVA']
      p1['tva']['mesaj_ScpTVA'] = gt['mesaj_ScpTVA']
      p1['tva']['data'] = gt['data']        
      anvil.server.call("sp1", self.ups(), p1)
    self.clear_tva()        
    self.label_12.text = p1['tva']['cui']      
    self.label_13.text = p1['tva']['scpTVA']
    self.label_14.text = p1['tva']['data_inceput_ScpTVA']
    self.label_15.text = p1['tva']['statusRO_e_Factura']
    self.label_16.text = p1['tva']['statusInactivi']
    self.label_17.text = p1['tva']['statusTvaIncasare']
    self.label_18.text = p1['tva']['dataInceputTvaInc']
    self.label_19.text = p1['tva']['statusSplitTVA']
    self.label_20.text = p1['tva']['dataInceputSplitTVA']
    self.label_21.text = p1['tva']['mesaj_ScpTVA']
    self.label_23.text = p1['tva']['data']  
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

 
  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.text_box_1.text = self.item[ 'denumire' ]
    pass
  def button_6_click(self, **event_args):
    nr = int(self.label_97.text)
    li = []
    if nr > 0:
      nr = int(self.label_97.text)-1
      li.append(p1['litigii'][nr])
      self.repeating_panel_1.items = li
    self.label_97.text = str(nr)
    pass

  def button_4_click(self, **event_args):
    if cui == "":
      alert ("CUI necompletat")
    else:
       self.tva("b")      
    pass

  def button_7_click(self, **event_args):
    if cui == "":
      alert ("CUI necompletat")
    else:
      self.get_bil("b")
    pass
  def get_bil(self, tip):
    if tip == "b":
      self.clear_bilant()
      an = str(int(date.today().year))  
      p1['bil'][str(0)] = json.loads(anvil.server.call("is_2", an, cui))
      ann = str(int(p1['bil']['0']['an'])-1)      
      p1['bil'][str(1)] = json.loads(anvil.server.call("is_2", ann, cui))
      anvil.server.call("sp1", self.ups(), p1)
    try:  
      self.bilant(p1['bil'][str(1)], p1['bil'][str(0)])
    except:
      pass
    pass

  def button_8_click(self, **event_args):
    if cui == "" or p1['gen']['name'] == "":
      alert ("CUI/Denumire necompletat")
    else:  
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
  def ps(self, sst):
    s=""
    st=str(sst)
    for i in st:
       if i.isnumeric() or i=="," or i.isalpha():
        s = s + i
    return s
  def button_9_click(self, **event_args): 
    if p1['gen']['name'] == "":
      alert ("Denumire necompletat")
    else:
      self.ref_lit("b")
    pass
  def ch_pan(self, js, mx):
    self.repeating_panel_1.items = js
    self.label_97.text = "0"
    self.label_99.text = mx
    
  def ref_lit(self, tip):    
      self.drop_down_1.selected_value = ""
      self.drop_down_2.selected_value = ""
      den = self.text_box_1.text
      lit=[]
      if tip == "b":
        li = json.loads(anvil.server.call("litigii", den))
        p1['litigii'] = li
        anvil.server.call("sp1", self.ups(), p1)
      lit.append(p1['litigii'][0])
      mx  = str(len(p1['litigii'])-1)
      self.ch_pan(lit, mx)      
      cal = []
      calitate =[""]
      ob = []
      obiect=[""]
      if len(p1['litigii']) > 0:
        for i in range(0, len(p1['litigii'])):
          cal.append(p1['litigii'][i]['calitate'])
          [calitate.append(x) for x in cal if x not in calitate]
          ob.append(p1['litigii'][i]['obiect'])
          [obiect.append(x) for x in ob if x not in obiect]
        self.drop_down_1.items = calitate
        self.drop_down_2.items = obiect    
        #self.repeating_panel_1.items = lit     
      pass
  def drop_down_1_change(self, **event_args):
    filt = []
    if self.drop_down_1.selected_value != "" and self.drop_down_2.selected_value == "":
      s1 = p1['litigii']
      for i in range(0, len(p1['litigii'])):
        if s1[i]['calitate'] == self.drop_down_1.selected_value.strip():
          f = s1[i]
          filt.append(f)
      mx = "0"
      self.ch_pan(filt, mx)    
    if self.drop_down_1.selected_value.strip() == "" and self.drop_down_2.selected_value.strip() == "":  
      filt.append(p1['litigii'][0])
      mx = str(len(p1['litigii'])-1) 
      self.ch_pan(filt, mx) 
    if self.drop_down_1.selected_value != "" and self.drop_down_2.selected_value != "":  
      s1 = p1['litigii']
      for i in range(0, len(p1['litigii'])):
        if s1[i]['calitate'] == self.drop_down_1.selected_value.strip() and s1[i]['obiect'] == self.drop_down_2.selected_value.strip():
          f = s1[i]
          filt.append(f)
      mx = "0"
      self.ch_pan(filt, mx)
    if self.drop_down_2.selected_value != "" and self.drop_down_1.selected_value == "":
      s1 = p1['litigii']
      for i in range(0, len(p1['litigii'])):
        if s1[i]['obiect'] == self.drop_down_2.selected_value.strip():
          f = s1[i]
          filt.append(f)
      #mx  = str(len(filt)-1)   
      mx = "0"
      self.ch_pan(filt, mx) 
      
      
    pass
  def drop_down_2_change(self, **event_args):
    filt = []    
    if self.drop_down_2.selected_value != "" and self.drop_down_1.selected_value == "":
      s1 = p1['litigii']
      for i in range(0, len(p1['litigii'])):
        if s1[i]['obiect'] == self.drop_down_2.selected_value.strip():
          f = s1[i]
          filt.append(f)
      #mx  = str(len(filt)-1)   
      mx = "0"
      self.ch_pan(filt, mx)
    if self.drop_down_2.selected_value.strip() == "" and self.drop_down_1.selected_value.strip() == "":  
      filt.append(p1['litigii'][0])
      mx = str(len(p1['litigii'])-1) 
      self.ch_pan(filt, mx)
    if self.drop_down_1.selected_value != "" and self.drop_down_2.selected_value != "":  
      s1 = p1['litigii']
      for i in range(0, len(p1['litigii'])):
        if s1[i]['calitate'] == self.drop_down_1.selected_value.strip() and s1[i]['obiect'] == self.drop_down_2.selected_value.strip():
          f = s1[i]
          filt.append(f)
      mx = "0"
      self.ch_pan(filt, mx)  
    if self.drop_down_1.selected_value != "" and self.drop_down_2.selected_value == "":
      s1 = p1['litigii']
      for i in range(0, len(p1['litigii'])):
        if s1[i]['calitate'] == self.drop_down_1.selected_value.strip():
          f = s1[i]
          filt.append(f)
      mx = "0"
      self.ch_pan(filt, mx)   
    pass

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    mx = int(self.label_99.text)
    li = []
    nr = int(self.label_97.text)
    nr = nr +1 
    if nr < mx or nr == mx:
      li.append(p1['litigii'][nr])
      self.repeating_panel_1.items = li
      self.label_97.text = str(nr)
    pass

  