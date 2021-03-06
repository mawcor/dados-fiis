from bs4 import BeautifulSoup
import requests

data_list = ["Valor Patrimonial", "Último Rendimento", "Dividend Yield"]
tickers = ["HCTR11", "VGIP11","CPTS11","MXRF11","SARE11","SDIL11","GGRC11","BRCR11","BCFF11","RBRP11","XPLG11","HGRU11","XPML11","HGRE11","KNCR11","RECT11","RECR11","VRTA11","IRDM11","MCCI11","BTLG11","HGLG11","PVBI11","MALL11","VILG11","VISC11","ALZR11","DEVA11","KNSC11","RBRY11","RVBI11","RBRF11","VGIR11","HSML11","JSRE11","HSLG11","HGPO11","RBRR11","MGFF11","RBRL11","XPIN11","TEPP11","HGBS11","VINO11","KNRI11","TRXF11","CXCO11"]

url = "https://www.fundsexplorer.com.br/funds/"

informations = {}

print("Iniciando...")

for ticker in tickers:
    print("Executando ticker {}".format(ticker))

    result = requests.get("{}{}".format(url, ticker))
    doc = BeautifulSoup(result.text, "html.parser")

    for data in data_list:
        vp_text = doc.find_all(text=data)
        span = vp_text[0].parent
        vp = span.next_sibling.next_sibling.text.strip()
        # print("{} = {}".format(ticker, vp))

        if data in informations.keys():
            informations[data].append("{} = {}".format(ticker, vp))
        else:
            informations[data] = ["{} = {}".format(ticker, vp)]

for info in informations:
    print(info)
    print(*informations[info], sep="\n")
    print("")
