# -*- coding: utf-8 -*-
__author__ = "israel Amaral"

import gzip
import json
from collections import Counter
from datetime import datetime
import os

# Definir o diretório de trabalho
os.chdir("C:\\Users\\israe\\OneDrive\\Documentos\\vscode\\Análise de Mídias Sociais\\Atividade Prática 02")

# Função para processar os arquivos
def processar_arquivo(file_path):
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        posts = [json.loads(line) for line in f]
    return posts

# Função para obter o total de curtidas
def obter_curtidas(post):
    return post.get('reactions_like', {}).get('summary', {}).get('total_count', 0)

# Função para obter o total de compartilhamentos
def obter_shares(post):
    return post.get('shares', {}).get('count', 0)

# Função para analisar as postagens
def analisar_postagens(posts, nome_candidato):
    print(f"\nAnalisando postagens de {nome_candidato}...\n")

    # Total de postagens
    total_posts = len(posts)
    print(f"Total de postagens: {total_posts}")

    # Palavra mais utilizada
    stopwords = {'que', 'e', 'a', 'o', 'da', 'de', 'do', 'em', 'um', 'uma', 'os', 'as', 'para'}
    todas_palavras = Counter()
    for post in posts:
        if 'message' in post:
            palavras = post['message'].lower().split()
            palavras_filtradas = [palavra for palavra in palavras if palavra not in stopwords]
            todas_palavras.update(palavras_filtradas)
    palavra_mais_comum = todas_palavras.most_common(1)[0] if todas_palavras else ('Nenhuma', 0)
    print(f"Palavra mais utilizada: {palavra_mais_comum[0]} (usada {palavra_mais_comum[1]} vezes)")

    # Dia com maior quantidade de postagens
    dias = Counter()
    for post in posts:
        if 'created_time' in post:
            data = datetime.strptime(post['created_time'], "%Y-%m-%dT%H:%M:%S%z")
            dias[data.date()] += 1
    dia_mais_posts = dias.most_common(1)[0] if dias else ('Nenhum', 0)
    print(f"Dia com mais postagens: {dia_mais_posts[0]} ({dia_mais_posts[1]} postagens)")

    # Postagem mais curtida e menos curtida
    mais_curtida = max(posts, key=lambda x: obter_curtidas(x))
    menos_curtida = min(posts, key=lambda x: obter_curtidas(x))
    print(f"Postagem mais curtida: {mais_curtida.get('message', 'Mensagem ausente')} ({obter_curtidas(mais_curtida)} curtidas)")
    print(f"Postagem menos curtida: {menos_curtida.get('message', 'Mensagem ausente')} ({obter_curtidas(menos_curtida)} curtidas)")

    # Tipo de postagem mais utilizada
    tipos = Counter(post.get('status_type', 'desconhecido') for post in posts)
    tipo_mais_comum = tipos.most_common(1)[0] if tipos else ('Nenhum', 0)
    print(f"Tipo de postagem mais utilizado: {tipo_mais_comum[0]} ({tipo_mais_comum[1]} vezes)")

    # Análises adicionais
    # Média de curtidas por postagem
    total_curtidas = sum(obter_curtidas(post) for post in posts)
    media_curtidas = total_curtidas / total_posts if total_posts > 0 else 0
    print(f"Média de curtidas por postagem: {media_curtidas:.2f}")

    # Postagens por mês
    meses = Counter()
    for post in posts:
        if 'created_time' in post:
            data = datetime.strptime(post['created_time'], "%Y-%m-%dT%H:%M:%S%z")
            meses[(data.year, data.month)] += 1
    print("Postagens por mês:")
    for mes, qtd in sorted(meses.items()):
        print(f"  {mes[0]}-{mes[1]:02d}: {qtd} postagens")

    # Tipo de postagem com maior engajamento
    engajamento_por_tipo = Counter()
    for post in posts:
        engajamento = (
            obter_curtidas(post) +
            obter_shares(post) +
            post.get('comments', 0) if isinstance(post.get('comments', 0), int) else 0
        )
        tipo = post.get('status_type', 'desconhecido')
        engajamento_por_tipo[tipo] += engajamento
    tipo_mais_engajamento = engajamento_por_tipo.most_common(1)[0] if engajamento_por_tipo else ('Nenhum', 0)
    print(f"Tipo de postagem com maior engajamento: {tipo_mais_engajamento[0]} ({tipo_mais_engajamento[1]} interações)")

# Executar as análises para Lula e Bolsonaro
if __name__ == "__main__":
    arquivos = {
        "Lula": "lula.gz",
        "Bolsonaro": "bolsonaro.gz"
    }

    for nome, caminho in arquivos.items():
        posts = processar_arquivo(caminho)
        analisar_postagens(posts, nome)
