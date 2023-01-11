from ._anvil_designer import cfTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import stripe.checkout
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json
class cf(cfTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    items = []
    for row in range(10):
      item = {}
      for col in range(1, 19):
         item.update({'column_{}'.format(col): 'col{}_{}'.format(col, row)})
      items.append(item)
    self.repeating_panel_1.items = items

    self.data_grid_1.role = 'wide'
    # Any code you write here will run when the form opens.
    

  def button_4_click(self, **event_args):
    open_form('init')
    pass

  def button_5_click(self, **event_args):
    open_form('init.analiza')
    pass

  def button_1_click(self, **event_args):
    ccf = []
    cf = {"a":{"den":"a.Nr. luni in perioada (12 luni sau cate au ramas pana la finele anului )", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "b":{"den":"b.Cifra de afaceri (anual/estimat de la luna curenta pana la finele anului pt an curent)", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "c":{"den":"c.Alte venituri de exploatare cu caracter recurent care nu sunt cuprinse in CA (nu include: variatia stocurilor, ven din ajustari/provizioane, ven financiare, ven exceptionale)-anual/estimat de la luna curenta pana la finele anului pt an curent", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "d":{"den":"d.Cheltuieli operationale estimate (fara amortizari si provizioane) - anual/estimat de la luna curenta pana la finele anului pt an curent", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "e":{"den":"e.CashFlow Operational brut", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "f":{"den":"f.La cate zile se incaseaza clientii de la data vanzarii (perioada de la avans la facturare diminueaza per estimata)?", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "g":{"den":"g.Cate zile se stocheaza marfurile/produsele/productia in curs (perioada de la momentul achizitiei pana la vanzarea acestora)?", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "h":{"den":"h.La cate zile se platesc furnizorii de la data achizitiei (perioada de la plata avansului pana la factura finala creste perioada)?", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "i":{"den":"i.Variatie in capitalul de lucru", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "j":{"den":"j.CashFlow Operational Net", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "k":{"den":"k.Disponibilitati din perioada anterioara/estimat disponibil", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "l":{"den":"l.CashFlow Disponibil", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""}, 
         "m":{"den":"m.Plati reprezentand rambursari (rate si dobanzi ) aferente creditului solicitat   (anual/estimat de la luna curenta pana la finele anului pt an curent)", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "n":{"den":"n.Plati reprezentand rambursari (rate si dobanzi )la creditele si leasingurile existente/care se vor contracta - altele decat creditul solicitat  (anual/estimat de la luna curenta pana la finele anului pt an curent)", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "o":{"den":"o.Plati (fara tva) reprezentand investitii in imobilizari (anual/estimat de la luna curenta pana la finele anului pt an curent)", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "p":{"den":"p.Incasari din imprumuri noi contractate/ estimate a se contracta (credite (inclusiv credit solicitat), leasinguri, de la asociati sau majorari de capital social) -anual/estimat de la luna curenta pana la finele anuluipt an curent", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "r":{"den":"r.Plati reprezentand rambursari imprumuturi asociati sau rambursari de dividende (anual/estimat de la luna curenta pana la finele anului pt an curent)", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "s":{"den":"s.Plati reprezentand datorii restante/reesalonate la buget din anii anteriori (anual/estimat de la data curenta pana la finele anului pt an curent)", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "t":{"den":"t.Incasari reprezentand subventii pt investitii", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""}, 
         "x":{"den":"x.Total sarcina financiara ", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""},
         "y":{"den":"y.Sustinerea sarcinii financiare (val>1.2 este eligibila; val <1.2 nu este eligibila)", "an_ant":"", "an_c":"", "an_2":"", "an_3":"", "an_4":"", "an_5":"", "an_6":"", "an_7":"",
              "an_8":"", "an_9":"", "an_10":"", "an_11":"", "an_12":"", "an_13":"", "an_14":"", "an_15":"", "an_16":"", "an_17":"", "an_18":""}, 
         "premise":{"ven":"1", "chelt":"2", "plt":""}}
    key_list=[]
    for key in cf.keys():
      ll={}
      ll=cf[key]   
      ccf.append(ll)
      key_list.append(key)
    self.repeating_panel_1.items=ccf
    self.text_area_1.text=self.repeating_panel_1.items[21]["ven"]
    self.text_area_2.text=self.repeating_panel_1.items[21]["chelt"]
    self.text_area_3.text=self.repeating_panel_1.items[21]["plt"]
    #print(key_list)
    i=2
    j=0
    lis_col=[]
    for col in self.data_grid_1.columns:
      cc={}
      cc = col
      if j<3:
        lis_col.append(cc)
      j=j+1
    print(lis_col)  
    #self.data_grid_1.columns=lis_col
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    js=self.repeating_panel_1.items
    jsf=[]
    for i in range(0,len(js)):
      js1={}
      js1["a"]=js[0]
      js1["b"]=js[1]
      jsf.append(js1)
    print(jsf[0])  
    pass




