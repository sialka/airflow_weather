# Apache Airflow: Orquestrando Pipeline de Dados

**Ideia do Projeto**

Consumir dados climáticos de uma semana e armazenar em csv

*Fonte: Alura*

### API 

https://weather.visualcrossing.com


### Ambiente

* Linux Ubuntu 20.04.5 LTS
* Python3
* Python3-pip
* Python3.9-venv
* Airflow 2.3.2

### Bibliotecas


### Fase 1

A key para uso da API está armazenada em key.py
```python
key = '...'
```

Execução
```bash
$ cd py
$ python3 getinfoClima.py
```

### Fase 2

**Instalando o Airflow**

(1) $ pip install 'apache-airflow==2.3.2' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.9.txt"
(2) $ export AIRFLOW_HOME=/home/alura/Documents/PrevisaoTempo/airflow
(3) $ airflow standalone

Observações 
    1. Em ambiente virtual venv
    2. Neste projeto desejamos que as configurações do Airflow fique em /Documents/PrevisaoTempo/airflow
    3. Executando o Airflow
    4. Por padrão o usuártio é admin e a senha fica armazenada em airflow/standalone_admin_password.txt
    5. No navegador: localhost:8080


### Fase 3

Exemplos simples de Dags:

 * helloWold.py
 * tarefas.py
