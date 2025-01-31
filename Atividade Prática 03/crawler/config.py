config = {
  # Configuração da região da coleta -> Formato: ISO 3166-1 alpha-2
  "region_code": "BR",         

  # Configuração da linguagem da coleta -> Formato: ISO 639-1   
  "relevance_language": "pt",     

  # A coleta ocorre da data final para a data inicial -> [ano, mês, dia]
  "start_date": [2024, 1, 1], 
  "end_date": [2024, 12, 31],

  # API que receberá uma requisição PATCH com payload de um JSON contendo informações acerca da coleta
  # Mantenha uma string vazia "" Caso não tenha configurado
  "api_endpoint": "",
  # Intervalo, em segundos, entre cada envio de dados para a API
  "api_cooldown": 60,                                                   

  # Intervalo, em segundos, entre cada tentativa de requisição para a API apos falha
  "try_again_timeout": 60,                                              

  # Palavras que serão utilizadas para filtrar os títulos dos vídeos
  "key_words": [
    "calvoesfera", "luan", "renan",
  ], 
#  "key_words": [
#    "vacina", "covid", "coronavirus", "pfizer"
#  ], 


# como obter a chave https://developers.google.com/youtube/v3/getting-started?hl=pt-br
  # KEYs da API v3 do YouTube
  "youtube_keys": [
    # "key 1",
    # "key 2",
    # "key 3",
    
  ],

  # Queries que serão utilizadas na pesquisa
  "queries": [
    "calvoesfera luan", "calvoesfera renan",
  ]
#  "queries": [
#    "vacina covid19", "vacina coronavirus", "vacina pfizer"
#  ]
}
