# -*- coding: utf-8 -*-
import json

def salvar_json(dicionario, arquivo):
    """
    Salva o dicionário fornecido no formato JSON.
    """
    with open(arquivo, 'w', encoding='utf-8') as json_file:
        json.dump(dicionario, json_file, ensure_ascii=False, indent=4)

def salvar_tsv(dicionario, arquivo):
    """
    Salva o dicionário fornecido no formato TSV.
    """
    with open(arquivo, 'w', encoding='utf-8') as tsv_file:
        tsv_file.write("id \ttitulo \tano \tgenero \tdiretor \tnota_imdb \n")
        for filme_id, filme_info in dicionario.items():
            generos = ', '.join(filme_info['genero'])
            tsv_file.write(
                f"{filme_id}\t{filme_info['titulo']}\t{filme_info['ano']}\t{generos}\t"
                f"{filme_info['diretor']}\t{filme_info['nota_imdb']}\n"
            )

def ler_tsv_para_dicionario(arquivo):
    """
    Lê um arquivo TSV e retorna um dicionário com os dados.
    """
    dicionario = {}
    with open(arquivo, 'r', encoding='utf-8') as tsv_file:
        linhas = tsv_file.readlines()
        for linha in linhas[1:]: # Ignorar o cabeçalho
            campos = linha.strip().split('\t')
            dicionario[campos[0]] = {
                'titulo': campos[1],
                'ano': int(campos[2]),
                'genero': campos[3].split(', '),
                'diretor': campos[4],
                'nota_imdb': float(campos[5])
            }
    return dicionario    

def main():
    # Criando dicionário de filmes
    dict_filmes = {
        'f1': {
            'titulo': 'A Origem', 'ano': 2010, 
            'genero': ['Ficção Científica', 'Ação'], 
            'diretor': 'Christopher Nolan', 'nota_imdb': 8.8
        },
        'f2': {
            'titulo': 'Clube da Luta', 'ano': 1999, 
            'genero': ['Drama'], 
            'diretor': 'David Fincher', 'nota_imdb': 8.8
        },
        'f3': {
            'titulo': 'O Senhor dos Anéis: O Retorno do Rei', 'ano': 2003, 
            'genero': ['Aventura', 'Fantasia'], 
            'diretor': 'Peter Jackson', 'nota_imdb': 9.0
        },
        'f4': {
            'titulo': 'Pulp Fiction', 'ano': 1994, 
            'genero': ['Crime', 'Drama'], 
            'diretor': 'Quentin Tarantino', 'nota_imdb': 8.9
        },
        'f5': {
            'titulo': 'Matrix', 'ano': 1999, 
            'genero': ['Ficção Científica', 'Ação'], 
            'diretor': 'Lana Wachowski, Lilly Wachowski', 'nota_imdb': 8.7
        }
    }

    # Salvar os dados em JSON e TSV
    salvar_json(dict_filmes, 'filmes.json')
    salvar_tsv(dict_filmes, 'filmes.tsv')

    # Ler o TSV e carregar novamente em um dicionário
    dict_carregado = ler_tsv_para_dicionario('filmes.tsv')
    print("\nDicionário carregado do TSV:")
    print(dict_carregado)

if __name__ == "__main__":
    main()