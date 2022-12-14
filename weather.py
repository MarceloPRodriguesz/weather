import requests
 
# API que tem como buscar em tempo real a previsão do tempo de uma cidade digitada pelo usário
# Foram utilizados nesse projeto a integração do python juntamente do Open Weather.

def pesquisa_clima(city):
    # pego chave da API
    API_key = "0e77ea7de532fd9b6703a7be59a2c865"

    # Faço a solicitação (request)
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&lang=pt_br"

    # requisição recebe os resultados do request
    requisicao = requests.get(link)

    # usando vairavel para receber resultados do dicionario
    dic_requisicao = requisicao.json()

    # filtrando itens especificos do dicionario
    descricao = dic_requisicao['weather'][0]['description']
    temperatura = dic_requisicao['main']['temp'] - 273.15
    
    return descricao

    # exibindo resultados do filtro
    #print(descricao)
    
def pesquisa_temperatura(city):
    API_key = "0e77ea7de532fd9b6703a7be59a2c865"
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&lang=pt_br"
    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()
    temperatura = dic_requisicao['main']['temp'] - 273.15
    #print(f"{int(temperatura)}°C")
    
    return (f"{int(temperatura)}°C")
