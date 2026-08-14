import requests as rq

url4099 = "https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201-202601/variaveis/4099?localidades=N3[26]&classificacao=2[all]"
url4096 = "https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201-202601/variaveis/4096?localidades=N3[26]&classificacao=2[all]"
url12466 = "https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201-202601/variaveis/12466?localidades=N3[26]&classificacao=2[all]"

data4099 = rq.get(url4099).json()
data4096 = rq.get(url4096).json()
data12466 = rq.get(url12466).json()

valores4099 = data4099[0]['resultados'][0]['series'][0]['serie']
valores4099H = data4099[0]["resultados"][1]["series"][0]["serie"]
valores4099M = data4099[0]["resultados"][2]["series"][0]["serie"]

valores4096 = data4096[0]['resultados'][0]['series'][0]['serie']
valores4096H = data4096[0]['resultados'][1]['series'][0]['serie']
valores4096M = data4096[0]['resultados'][2]['series'][0]['serie']

valores12466 = data12466[0]['resultados'][0]['series'][0]['serie']
valores12466H = data12466[0]['resultados'][1]['series'][0]['serie']
valores12466M = data12466[0]['resultados'][2]['series'][0]['serie']


with open("total4099.json", "w") as f:
    f.write(str(valores4099))

with open("Homens4099.json", "w") as f:
    f.write(str(valores4099H))

with open("Mulheres4099.json", "w") as f:
    f.write(str(valores4099M))


with open("total4096.json", "w") as f:
    f.write(str(valores4096))

with open("Homens4096.json", "w") as f:
    f.write(str(valores4096H))

with open("Mulheres4096.json", "w") as f:
    f.write(str(valores4096M))


with open("total12466.json", "w") as f:
    f.write(str(valores12466))

with open("Homens12466.json", "w") as f:
    f.write(str(valores12466H))

with open("Mulheres12466.json", "w") as f:
    f.write(str(valores12466M))





