#coding: utf-8

import json, gzip, os, sys


def main():
    files_path = ''    
    candidates = ['haddad']  # candidatos
    file_name = 'all_posts'  # nome do arquivo com todas as postagens
    
    for candidate in candidates:
        files_path = os.path.join(sys.path[0])
        # cria um arquivo para salvar alguns detalhes das postagens do comentário
        output_file = open('%s/posts_details_%s.tsv' % (files_path, candidate), 'w', encoding='utf-8')
        # cabeçalho do arquivo
        output_file.write('post_id\tdate\tnum_likes\tnum_angry\tnum_shares\n')
        print('********************************************************************************************************')
        print('\t\t\tREADING POSTS FROM %s ' % candidate)
        # caminho para o arquivo de post do candidato
        posts_file_path = '%s/%s/%s.json.gz' % (files_path, candidate, file_name)
        # caminho dos comentários
        comments_path = '%s/%s/comments/' % (files_path, candidate)
        print('\t\t\t%s' % posts_file_path)
        print('\t\t\t%s' % comments_path)   
        print('********************************************************************************************************')        
		
        # carregando o arquivo compactado
        with gzip.open(posts_file_path, 'rt', encoding='utf-8') as posts_file:  # Abre o arquivo compactado
            for line in posts_file: 
                json_line = json.loads(line.strip())
                print(json_line)
                post_id = json_line['id']
                date = json_line['created_time']
                
                # Converte reações para inteiros ou usa 0 como padrão
                num_likes = int(json_line['reactions_like']['summary']['total_count']) if 'reactions_like' in json_line else 0
                num_angry = int(json_line['reactions_angry']['summary']['total_count']) if 'reactions_angry' in json_line else 0
                
                # Trata o campo shares (se não existir, usa 0 como padrão)
                num_shares = int(json_line['shares']['count']) if ('shares' in json_line and 'count' in json_line['shares']) else 0

                # Escreve os dados no arquivo
                output_file.write('%s\t%s\t%d\t%d\t%d\n' % (
                    post_id, 
                    date, 
                    num_likes, 
                    num_angry, 
                    num_shares
                ))

        output_file.close()
                

if __name__ == "__main__":
    main()
