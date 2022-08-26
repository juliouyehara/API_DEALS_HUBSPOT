from api import api_deals
from owner import api_owner
from datetime import date
import hubspot
from postgres import insert_postgre, delete_postgres
from config import *
import time

config = CatalogConfig()
config.read()


def modelagem_deals(df, df_owner):

    df = df[df['deal stage'].isin(['6341606', '10918553', '10730156'])]
    df = df.reset_index(drop=True)
    # df = df.drop(columns='Unnamed: 0')
    lista = []
    for i in range(len(df)):
        data_string = df['close date'][i].split('T')[0]
        data_nova = date(*map(int, data_string.split('-')))
        lista.append(data_nova)
    df['close date'] = lista
    lista = []
    for i in range(len(df)):
        data_string = df['create date'][i].split('T')[0]
        data_nova = date(*map(int, data_string.split('-')))
        lista.append(data_nova)
    df['create date'] = lista
    lista = []
    for i in range(len(df)):
        data_string = df['last date modified'][i].split('T')[0]
        data_nova = date(*map(int, data_string.split('-')))
        lista.append(data_nova)
    df['last date modified'] = lista
    lista = []
    for i in range(len(df)):
        deal_name = df['deal name'][i].split('|')[0]
        lista.append(deal_name)
    df['deal name'] = lista
    lista = []
    for i in range(len(df)):
        owner = df['owner id'][i]
        lista.append(int(owner))
    df['owner id'] = lista
    lista = []
    for i in range(len(df)):
        deal = df['deal stage'][i]
        lista.append(int(deal))
    df['deal stage'] = lista
    lista = []
    for i in range(len(df)):
        deal = df['pipeline'][i]
        lista.append(int(deal))
    df['pipeline'] = lista
    lista = []
    for i in df['owner id']:
        primeiro_nome = str(df_owner['owner name'][df_owner['owner id'] == f'{i}'])
        primeiro_nome = primeiro_nome.split()[1]
        sobrenome = str(df_owner['owner last name'][df_owner['owner id'] == f'{i}'])
        sobrenome = sobrenome.split()[1]
        nome = str(primeiro_nome) + ' ' + str(sobrenome)
        if nome == 'Name: Name:':
            nome = 'Não encontrado'
        lista.append(nome)
    df['owner'] = lista
    lista = []
    lista = []
    for i in df['deal name']:
        i = str(i).upper()
        i = i.strip()
        lista.append(i)
    df['deal name'] = lista
    return df


key = config['POSTGRES']['URL']
# while True:

# delete_postgres(key_postgre=key)
client = hubspot.Client.create(access_token=config['HUB']['URL'])
df_deals = api_deals(client=client)
df_owner = api_owner(client=client)
df = modelagem_deals(df=df_deals, df_owner=df_owner)
print(df)
df.to_csv('api_hub.csv')
# df_dict = df.to_dict('records')
# insert_postgre(key_postgre=key, response=df_dict)
# time.sleep(7200)


