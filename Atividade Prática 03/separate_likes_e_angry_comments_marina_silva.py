#coding: utf-8
import json
import gzip
import os
import sys
from glob import glob


def main():
    files_path = os.path.join(sys.path[0])  
    candidates = ['marina_silva']  # Nome do candidato (diretório)
    
    for candidate in candidates:
        # Cria um arquivo para salvar alguns detalhes das postagens do candidato
        output_file_path = os.path.join(files_path, f'posts_details_{candidate}.tsv')
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Cabeçalho do arquivo
            output_file.write('post_id\tdate\tmessage\tnum_likes\tnum_angry\tnum_shares\n')
            
            print('********************************************************************************************************')
            print(f'\t\t\tPROCESSANDO POSTS DE {candidate}')
            
            # Caminho para o diretório do candidato
            candidate_path = os.path.join(files_path, candidate)
            # Busca todos os arquivos JSON compactados do candidato
            post_files = glob(os.path.join(candidate_path, 'posts_marina_silva_*.json.gz'))
            
            print(f'\t\t\tArquivos encontrados: {len(post_files)}')
            print('********************************************************************************************************')

            # Processa cada arquivo encontrado
            for posts_file_path in post_files:
                print(f'Lendo arquivo: {posts_file_path}')
                with gzip.open(posts_file_path, 'rt', encoding='utf-8') as posts_file:
                    for line in posts_file:
                        json_line = json.loads(line.strip())
                        post_id = json_line['id']
                        date = json_line['created_time']
                        # Verifica se o campo message existe no dicionário
                        msg = json_line['message'] if 'message' in json_line else ''
                        num_likes = json_line['reactions_like']['summary']['total_count']
                        num_angry = json_line['reactions_angry']['summary']['total_count']
                        num_shares = json_line['shares']['count'] if 'shares' in json_line else 0
                        output_file.write(f'{post_id}\t{date}\t{json.dumps(msg)}\t{num_likes}\t{num_angry}\t{num_shares}\n')
        
            print(f'Dados salvos em: {output_file_path}')


if __name__ == "__main__":
    main()
