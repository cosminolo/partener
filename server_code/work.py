import anvil.server
import json
import requests
import xmltodict
from requests.structures import CaseInsensitiveDict
from pandas import json_normalize
@anvil.server.callable
def js_ini():
 j = {}
 j = {
    "tip":"SRL", "credit":" ", "facilit":" ", "suma":0, "valut":"Lei", "cui":" ", "den":" ", "sediu": "", "onrc":" ", "caen":" ",
    "ramura":" ", "cereale":"NU", "descriere":" ", "asociati":" ", "admin":" ", "nrsal":"0", "telef":" ", "soc_grup":" ",
    "piata":" ", "concurenta":" ", "strategia":" ", "conducere":" ", "ev_manag":" ", "cal_act":" ", "con_cli":" ", "exp_imp":" "
    }
 return j

def sp(x):
  parti = " "
  try:
   for i in range (0, len(x)):
        parti = parti + str (x[i]['nume']) + "-" + str(x[i]['calitateParte']) + " "
  except:
      pass
  return parti
@anvil.server.callable 
def lit(den):
 url = "http://portalquery.just.ro/Query.asmx"
 headers = CaseInsensitiveDict()
 headers["Content-Type"] = "application/soap+xml; charset=utf-8"
 headers["Content-Length"] = "length"
 data = """
  <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
   <soap12:Body>
     <CautareDosare xmlns="portalquery.just.ro">      
       <numeParte>""" + den + """</numeParte>          
     </CautareDosare>
   </soap12:Body>
  </soap12:Envelope>
 """
 litigii = []
 try:
  resp = requests.post(url, headers=headers, data=data)
  nr_l=0
  try:
    dict_data = xmltodict.parse(resp.content)
  except:
      nr_l = len(resp.content)
  json_data = json.dumps(dict_data, sort_keys=False, indent=2, ensure_ascii=False)
  js = json.loads(json_data)
  dat = json.loads(json.dumps(js['soap:Envelope']['soap:Body']['CautareDosareResponse']['CautareDosareResult']['Dosar'], sort_keys=False, indent=2, ensure_ascii=False))
  for i in range(0, len(dat)):
    x = dat[i]['parti']['DosarParte']
    parti = sp(x)
    for j in range(0, len(x)):
     calit = ""
     nuu = ""
     cazz={}
     try:
      if x[j]['nume'].find(den.upper()) != -1 or x[j]['nume'].find(den.lower()) != -1:
       calit = x[j]['calitateParte']
       nuu = x[j]['nume']
       s = " "
       s = str(dat[i]['sedinte']['DosarSedinta'][len(dat[i]['sedinte']['DosarSedinta'])-1]).replace("'", " ")
       cazz = {"denumire": nuu, "calitate": calit, "obiect": dat[i]['obiect'],  "categ_caz": dat[i]['categorieCaz'], "parti": parti, "nr_dosar": dat[i]['numar'], "instanta": dat[i]['institutie'], "data_d": dat[i]['data'][:10], "data_mod": dat[i]['dataModificare'][:10], "stadiu": dat[i]['stadiuProcesual'], "solutie":s}
       litigii.append(cazz)
     except:
        a = 1
 except:
     if nr_l > 1000000:
        litigii = {"rez": " foarte multe, verifica la https://portal.just.ro"}
     else:
         litigii = {"rez": "nu inregistreaza"}
 litig = json.dumps(litigii, sort_keys=False, indent=2, ensure_ascii=False) 
 return litig
