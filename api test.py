from __future__ import print_function

from config import *
from hubspot.crm.deals import ApiException
import pandas as pd
import hubspot
from pprint import pprint
from hubspot.crm.properties import ApiException
from owner import api_owner
import os.path
import xlsxwriter
import pandas as pd
import numpy as np

config = CatalogConfig()
config.read()

client = hubspot.Client.create(access_token=config['HUB']['AUTH'])



try:
    api_response = client.crm.properties.core_api.get_all(object_type="deals", archived=False)
except ApiException as e:
    print("Exception when calling core_api->get_all: %s\n" % e)

api = vars(api_response)
lista_properties = []
for i in range(len(api['_results'])):
    api_var = vars(api['_results'][i])
    lista_properties.append(api_var['_name'])
print(len(lista_properties[:350]))

lista_hubspot = []
lista_hubspot1 = []



try:
    api_response = client.crm.deals.basic_api.get_page(limit=100,properties=lista_properties[:350], archived=False)
    # print(vars(api_response))
except ApiException as e:
    print("Exception when calling basic_api->get_page: %s\n" % e)
api_var = vars(api_response)
api_paging = api_var['_paging']
api_paging = vars(api_paging)
api_paging = vars(api_paging['_next'])
paging = api_paging['_after']
print(paging)
api_var = api_var['_results']
lista = []
for i in range(100):
    dic = {}
    api_properties = vars(api_var[i])
    api_properties = api_properties['_properties']
    lista_hubspot.append(api_properties)
df2 = pd.DataFrame(lista_hubspot)
print(df2)


while paging is not None:
    try:
        api_response = client.crm.deals.basic_api.get_page(limit=100, after=paging, properties=lista_properties[:350], archived=False)
        api_var = vars(api_response)
        api_paging = api_var['_paging']
        try:
            api_paging = vars(api_paging)
        except:
            paging = None
            continue
        api_paging = vars(api_paging['_next'])
        paging = api_paging['_after']
        api_var = api_var['_results']
        for i in range(100):
            dic = {}
            api_properties = vars(api_var[i])
            api_properties = api_properties['_properties']
            lista_hubspot.append(api_properties)



    except ApiException as e:
        print("Exception when calling basic_api->get_page: %s\n" % e)

df3 = pd.DataFrame(lista_hubspot)
df3 = df3.replace({',':''}, regex=True)
df3 = df3.replace({'"':''}, regex=True)


#
try:
    api_response = client.crm.deals.basic_api.get_page(limit=100,properties=lista_properties[350:], archived=False)
except ApiException as e:
    print("Exception when calling basic_api->get_page: %s\n" % e)
api_var = vars(api_response)
api_paging = api_var['_paging']
api_paging = vars(api_paging)
api_paging = vars(api_paging['_next'])
paging = api_paging['_after']
print(paging)
api_var = api_var['_results']
lista = []
for i in range(100):
    dic = {}
    api_properties = vars(api_var[i])
    api_properties = api_properties['_properties']
    lista_hubspot1.append(api_properties)


while paging is not None:
    try:
        api_response = client.crm.deals.basic_api.get_page(limit=100, after=paging, properties=lista_properties[350:], archived=False)
        api_var = vars(api_response)
        api_paging = api_var['_paging']
        try:
            api_paging = vars(api_paging)
        except:
            paging = None
            continue
        api_paging = vars(api_paging['_next'])
        paging = api_paging['_after']
        api_var = api_var['_results']
        for i in range(100):
            dic = {}
            api_properties = vars(api_var[i])
            api_properties = api_properties['_properties']
            lista_hubspot1.append(api_properties)
    except ApiException as e:
        print("Exception when calling basic_api->get_page: %s\n" % e)
df = pd.DataFrame(lista_hubspot1)
df = df.replace({',':''}, regex=True)
df = df.replace({'"':''}, regex=True)
df_final = df3.join(df, lsuffix="DROP").filter(regex="^(?!.*DROP)")
df_final = df_final[df_final['pipeline'].isin(['49962', '6336898', '49963', '10918547', '56475', '10730150'])]
df_final['pipeline'] = df_final['pipeline'].fillna(0)
df_final = df_final[df_final['pipeline'] != '0']
df_final = df_final.reset_index(drop=True)

df_owner = api_owner(client=client)

lista = []
for i in range(len(df_final)):
    owner = df_final['hubspot_owner_id'][i]
    try:
        lista.append(int(owner))
    except:
        lista.append(0)
df_final['hubspot_owner_id'] = lista

lista = []
for i in df_final['hubspot_owner_id']:
    primeiro_nome = str(df_owner['owner name'][df_owner['owner id'] == f'{i}'])
    primeiro_nome = primeiro_nome.split()[1]
    sobrenome = str(df_owner['owner last name'][df_owner['owner id'] == f'{i}'])
    sobrenome = sobrenome.split()[1]
    nome = str(primeiro_nome) + ' ' + str(sobrenome)
    if nome == 'Name: Name:':
        nome = 'Não encontrado'
    lista.append(nome)
df_final['owner'] = lista
df_pipe = pd.read_csv('propriedade_pipe.csv')
df_final['pipeline'] = df_pipe['pipeline']

path = config['PATH']['URL']
writer = pd.ExcelWriter(path , engine='xlsxwriter')
df_final.to_excel(writer)
writer.save()




