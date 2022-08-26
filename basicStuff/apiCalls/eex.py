print("API REQUEST: EEX")
import requests
query = {
        'returnType':'TRADES',
        'productType':'OPTIONS',
        'tradeDate':f'2022-08-{day}',
        'commodity':'POWER'
                }
    response = requests.get(
        "https://api1.datasource.eex-group.com/getDerivatives/json",
        params=query,
        auth=requests.auth.HTTPBasicAuth('EEX_7563', 'dua876v2'),verify=False
        ) (edited) 
print("RESPONSE", response)