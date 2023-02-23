import os
import shutil
from os.path import join
import pandas as pd
from datetime import datetime, timedelta
from key import key

# Intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

# Formatando as datas
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

city = 'Boston'
            
URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
            f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')

dados = pd.read_csv(URL)
print(dados.head())

# Registrando os .csv
file_path = f'datapipeline/semana={data_inicio}/'
if os.path.exists(file_path):
    shutil.rmtree(file_path)
os.mkdir(file_path)

dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')