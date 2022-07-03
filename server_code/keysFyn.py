import requests
from requests.structures import CaseInsensitiveDict
import xmltodict
import json
import re
import anvil.server
@anvil.server.callable
def login_k (us, psw):
    url = "https://testarews.keysfin.com/service.asmx?op=Login"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/soap+xml"
    data = """
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Header>
        <Credentials xmlns="http://tempuri.org/">
            <Username>"""+ us +"""</Username>
            <Password>"""+ psw +"""</Password>
        </Credentials>
      </soap12:Header>
      <soap12:Body>
        <Login xmlns="http://tempuri.org/">
            <Username>"""+ us +"""</Username>
            <Password>"""+ psw +"""</Password>
        </Login>
      </soap12:Body>
    </soap12:Envelope>
    """
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)
    idus = json.loads(json.dumps(xmltodict.parse(resp.content)))['soap:Envelope']['soap:Body']['LoginResponse']['LoginResult']
    return idus
  
def norm_js(jst):
    js = json.loads(json.dumps(jst))
    for key in js:
        if bool(re.match("^[a-zA-Z]+", str(js[key]))) == False:
            try:
                js[key] = str(int(float(js[key])))
            except:
                v = 0
        js['An'] = js['An'][:4]
        if str(js[key]) == "None":
            js[key] = "0"
    return js
@anvil.server.callable
def get_fin(idus, cui):
    url = "https://testarews.keysfin.com/service.asmx?op=CompanyFinancial"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/soap+xml; charset=utf-8"
    headers["Content-Length"] = "lenght"
    data = """
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
        <soap12:Body>
            <CompanyFinancial xmlns="http://tempuri.org/">
                <CUI>"""+ cui +"""</CUI>
                <IdUser>"""+ idus +"""</IdUser>
            </CompanyFinancial>
        </soap12:Body>
    </soap12:Envelope>
    """
    js=[]
    try:
        resp = requests.post(url, headers=headers, data=data)
        ret_pars = xmltodict.parse(resp.content)
        ret_js = json.loads(json.dumps(ret_pars, sort_keys=False, indent=2, ensure_ascii=False))['soap:Envelope']['soap:Body']['CompanyFinancialResponse']['CompanyFinancialResult']['xmlData']
        ret_pars1 = xmltodict.parse(ret_js)['root']['row']
        ret_js1 = json.loads(json.dumps(ret_pars1, sort_keys=False, indent=2, ensure_ascii=False))
        ret_js2 = ret_js1[len(ret_js1)-1]
        ret_js3 = ret_js1[len(ret_js1)-2]
        js.append(norm_js(ret_js3))
        js.append(norm_js(ret_js2))
    except:
        return js
    return js
