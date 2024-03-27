import pandas as pd
import os #Manipulador diretorio no SO
import glob #Manipular diretorio em massa

# Caminho para ler os arquivos (\\ = para entender que é um caminho)
folder_path = 'src\\data\\raw'

# Lista todos arquivos 
execel_files = glob.glob(os.path.join(folder_path,'*.xlsx'))

# Analisa se o caminho foi  lido
if not execel_files:
    print("Não tem nenhum caminho associado!")
else:
    # Armazena toda as tabelas
    df = []
    # Percorrer as tabelas
    for execel_file in execel_files:
        # Criar uma excessão para a leitura
        try:
            # Ler o arquivo 
            df_temp = pd.read_excel(execel_file)
            
            # Ler o caminho  
            file_name = os.path.basename(execel_file)

            df_temp['file_name'] = file_name
            
            # A partir do caminho pega apenas a strig do país
            location = file_name.split("_")[2].split(".")[0].upper()
            
            # Cria uma coluna para rascreio dos dados na fonte
            df_temp['location'] = location
            
            # cria uma nova coluna para a campanha
            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')
            
            # Salva tudo em df
            df.append(df_temp)

        except Exception as e:
            print(f"Erro ao ler o arquivo {execel_file}: {e}")
    
    

if df:
    # Cria um unico dataframe concatenando todas as tabelas
    df_data = pd.concat(df, ignore_index=True)
    # Cria um caminho 'scr\\data\\ready'
    output_path = os.path.join('src','data','ready','dataset.xlsx')
    # configura o motor de escrita para xlsxwriter
    write = pd.ExcelWriter(output_path,engine='xlsxwriter')
    # Leva os dados para o motor
    df_data.to_excel(write,index=False)
    # salva o arquido de excel
    write._save()
else:
    print("Nenhum dado para ser salvo")


