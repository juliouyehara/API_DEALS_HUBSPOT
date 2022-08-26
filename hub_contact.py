import hubspot
from pprint import pprint
from hubspot.crm.contacts import ApiException
import pandas as pd

client = hubspot.Client.create(access_token="pat-na1-6f7c3193-8e83-4bae-a6ea-257a74e09b78")

try:
    api_response = client.crm.contacts.basic_api.get_page(limit=100, archived=False)
    api_response = vars(api_response)
    pprint(len(api_response['_results']))
except ApiException as e:
    print("Exception when calling basic_api->get_page: %s\n" % e)

lista_hubspot = []


def api_contact(client):
    try:
        api_response = client.crm.contacts.basic_api.get_page(limit=100, properties=["hs_lead_status", "sql_tagging_system__wf_", "mql_tagging_system__wf_", "bofu_at__wf_", "tofu_at__wf_","canal","hubspot_owner_id","recent_conversion_date","recent_conversion_event_name","canal_em", "firstname", "lastname"], archived=False)
        api_var = vars(api_response)
        qtd = len(api_var['_results'])
        api_paging = api_var['_paging']
        api_paging = vars(api_paging)
        api_paging = vars(api_paging['_next'])
        paging = api_paging['_after']
        api_var = api_var['_results']
        for i in range(qtd):
            dict = {}
            api_properties = vars(api_var[i])
            api_properties = api_properties['_properties']
            try:
                api_id = api_properties['hs_object_id']
            except:
                api_id = ''
            try:
                api_create_date = api_properties['createdate']
            except:
                api_create_date = ''
            try:
                api_last_modified_date = api_properties['lastmodifieddate']
            except:
                api_last_modified_date = ''
            try:
                api_first_name = api_properties['firstname']
            except:
                api_first_name = ''
            try:
                api_last_name = api_properties['lastname']
            except:
                api_last_name = ''
            try:
                api_email = api_properties['email']
            except:
                api_email = ''
            try:
                api_owner = api_properties['hubspot_owner_id']
            except:
                api_owner = ''
            try:
                api_recent_conversion = api_properties['recent_conversion_date']
            except:
                api_recent_conversion = ''
            try:
                api_canal = api_properties['canal_em']
            except:
                api_canal = ''
            try:
                api_canal_canal = api_properties['canal']
            except:
                api_canal_canal = ''
            try:
                api_tofu = api_properties["tofu_at__wf_"]
            except:
                api_tofu = ''
            try:
                api_bofu = api_properties["bofu_at__wf_"]
            except:
                api_bofu = ''
            try:
                api_mql = api_properties["mql_tagging_system__wf_"]
            except:
                api_mql = ''
            try:
                api_sql = api_properties["sql_tagging_system__wf_"]
            except:
                api_sql = ''
            try:
                api_status = api_properties["hs_lead_status"]
            except:
                api_status = ''
            dict.update({'id':api_id,
                         'create date':api_create_date,
                         'last date modified':api_last_modified_date,
                         'first name':api_first_name,
                         'last name':api_last_name,
                         'email':api_email,
                         'owner':api_owner,
                         'recent conversion':api_recent_conversion,
                         'canal': api_canal,
                         'canal_canal':api_canal_canal,
                         'tofu':api_tofu,
                         'bofu':api_bofu,
                         'mql': api_mql,
                         'sql': api_sql,
                         'status': api_status
                         })
            lista_hubspot.append(dict)

    except ApiException as e:
        print("Exception when calling basic_api->get_page: %s\n" % e)

    while paging is not None:
        try:
            api_response = client.crm.contacts.basic_api.get_page(limit=100, after=paging,  properties=["hs_lead_status", "sql_tagging_system__wf_", "mql_tagging_system__wf_", "bofu_at__wf_", "tofu_at__wf_", "canal", "hubspot_owner_id","recent_conversion_date","recent_conversion_event_name","canal_em", "firstname", "lastname"], archived=False)
            api_var = vars(api_response)
            qtd = len(api_var['_results'])
            api_paging = api_var['_paging']
            try:
                api_paging = vars(api_paging)
            except:
                paging = None
                continue
            api_paging = vars(api_paging['_next'])
            paging = api_paging['_after']
            api_var = api_var['_results']
            for i in range(qtd):
                dict = {}
                api_properties = vars(api_var[i])
                api_properties = api_properties['_properties']
                try:
                    api_id = api_properties['hs_object_id']
                except:
                    api_id = ''
                try:
                    api_create_date = api_properties['createdate']
                except:
                    api_create_date = ''
                try:
                    api_last_modified_date = api_properties['lastmodifieddate']
                except:
                    api_last_modified_date = ''
                try:
                    api_first_name = api_properties['firstname']
                except:
                    api_first_name = ''
                try:
                    api_last_name = api_properties['lastname']
                except:
                    api_last_name = ''
                try:
                    api_email = api_properties['email']
                except:
                    api_email = ''
                try:
                    api_owner = api_properties['hubspot_owner_id']
                except:
                    api_owner = ''
                try:
                    api_recent_conversion = api_properties['recent_conversion_date']
                except:
                    api_recent_conversion = ''
                try:
                    api_canal = api_properties['canal_em']
                except:
                    api_canal = ''
                try:
                    api_canal_canal = api_properties['canal']
                except:
                    api_canal_canal = ''
                try:
                    api_tofu = api_properties["tofu_at__wf_"]
                except:
                    api_tofu = ''
                try:
                    api_bofu = api_properties["bofu_at__wf_"]
                except:
                    api_bofu = ''
                try:
                    api_mql = api_properties["mql_tagging_system__wf_"]
                except:
                    api_mql = ''
                try:
                    api_sql = api_properties["sql_tagging_system__wf_"]
                except:
                    api_sql = ''
                try:
                    api_status = api_properties["hs_lead_status"]
                except:
                    api_status = ''
                dict.update({'id': api_id,
                             'create date': api_create_date,
                             'last date modified': api_last_modified_date,
                             'first name': api_first_name,
                             'last name': api_last_name,
                             'email': api_email,
                             'owner': api_owner,
                             'recent conversion': api_recent_conversion,
                             'canal': api_canal,
                             'canal_canal': api_canal_canal,
                             'tofu': api_tofu,
                             'bofu': api_bofu,
                             'mql':api_mql,
                             'sql':api_sql,
                             'status':api_status
                             })
                lista_hubspot.append(dict)
        except ApiException as e:
            print("Exception when calling basic_api->get_page: %s\n" % e)
    df = pd.DataFrame(lista_hubspot)
    return df

df = api_contact(client)
df.to_csv('contato.csv')
