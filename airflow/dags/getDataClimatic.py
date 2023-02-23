from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.macros import ds_add
from airflow.models import Variable
from os.path import join
import pendulum
import pandas as pd

with DAG(
    "Dados_Climaticos",
    start_date=pendulum.datetime(2023, 1, 16, tz="UTC"),
    schedule_interval='0 0 * * 1',  # executar toda segunda feira
) as dag:

    tarefa_1 = BashOperator(
        task_id='Cria_Pastas_DataLake',
        bash_command='mkdir -p "/home/alura/Documents/PrevisaoTempo/DataLake/semana={{data_interval_end.strftime("%Y-%m-%d")}}"'
    )

    def extrai_dados(data_interval_end):

        city = 'Boston'
        key = Variable.get("weather_api_key")
        url = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
                   f'{city}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&include=days&key={key}&contentType=csv')

        dados = pd.read_csv(url)

        file_path = f'/home/alura/Documents/PrevisaoTempo/DataLake/semana={data_interval_end}/'

        dados.to_csv(file_path + 'dados_brutos.csv')
        dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(
            file_path + 'temperaturas.csv')
        dados[['datetime', 'description', 'icon']].to_csv(
            file_path + 'condicoes.csv')

    tarefa_2 = PythonOperator(
        task_id='Extrai_Dados_Climaticos',
        python_callable=extrai_dados,
        op_kwargs={
            'data_interval_end': '{{data_interval_end.strftime("%Y-%m-%d")}}'}
    )

    tarefa_1 >> tarefa_2
