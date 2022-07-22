from hubspot.crm.deals import ApiException
import pandas as pd

lista_hubspot = []


def api_deals(client):

    try:
        api_response = client.crm.deals.basic_api.get_page(limit=100,properties=["hubspot_owner_id","dealname","createdate","closedate","amount", "valor_de_implantacao__automatico_", "hs_tcv", "implantacao__typeform____manual", "condicoes_comerciais___implantacao",  "dealstage", 'pipeline'], archived=False)
        api_var = vars(api_response)
        api_paging = api_var['_paging']
        api_paging = vars(api_paging)
        api_paging = vars(api_paging['_next'])
        paging = api_paging['_after']
        api_var = api_var['_results']
        for i in range(100):
            dict = {}
            api_properties = vars(api_var[i])
            api_properties = api_properties['_properties']
            api_amount = api_properties['amount']
            try:
                api_id = api_properties['_id']
            except:
                api_id = ''
            try:
                api_amount = api_properties['amount']
            except:
                api_amount = ''
            try:
                api_close_date = api_properties['closedate']
            except:
                api_close_date = ''
            try:
                api_create_date = api_properties['createdate']
            except:
                api_create_date = ''
            try:
                api_deal_name = api_properties['dealname']
            except:
                api_deal_name = ''
            try:
                api_deal_stage = api_properties['dealstage']
            except:
                api_deal_stage = ''
            try:
                api_last_modified_date = api_properties['hs_lastmodifieddate']
            except:
                api_last_modified_date = ''
            try:
                api_object_id = api_properties['hs_object_id']
            except:
                api_object_id = ''
            try:
                api_pipeline = api_properties['pipeline']
            except:
                api_pipeline = ''
            try:
                api_owner_id = api_properties['hubspot_owner_id']
            except:
                api_owner_id = ''
            try:
                api_condicoes = api_properties['condicoes_comerciais___implantacao']
            except:
                api_condicoes = ''
            try:
                api_total_contract = api_properties['hs_tcv']
            except:
                api_total_contract = ''
            try:
                api_implatacao_typeform = api_properties['implantacao__typeform____manual']
            except:
                api_implatacao_typeform = ''
            try:
                api_implatacao_auto = api_properties['valor_de_implantacao__automatico_']
            except:
                api_implatacao_auto = ''
            dict.update({'id': api_id,
                         'amount': api_amount,
                         'close date': api_close_date,
                         'create date': api_create_date,
                         'deal name': api_deal_name,
                         'deal stage': api_deal_stage,
                         'last date modified': api_last_modified_date,
                         'object id': api_object_id,
                         'pipeline': api_pipeline,
                         'owner id': api_owner_id,
                         'condicoes': api_condicoes,
                         'total contrato': api_total_contract,
                         'implatacao typeform': api_implatacao_typeform,
                         'implatacao automatica': api_implatacao_auto})
            lista_hubspot.append(dict)

    except ApiException as e:
        print("Exception when calling basic_api->get_page: %s\n" % e)

    while paging is not None:
        try:
            api_response = client.crm.deals.basic_api.get_page(limit=100, after=paging, properties=["hubspot_owner_id", "dealname", "createdate", "closedate", "amount", 'valor_de_implantacao__automatico_', "hs_tcv", "implantacao__typeform____manual", "condicoes_comerciais___implantacao", "dealstage", 'pipeline'], archived=False)
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
                dict = {}
                api_properties = vars(api_var[i])
                api_properties = api_properties['_properties']
                api_amount = api_properties['amount']
                try:
                    api_id = api_properties['_id']
                except:
                    api_id = ''
                try:
                    api_amount = api_properties['amount']
                except:
                    api_amount = ''
                try:
                    api_close_date = api_properties['closedate']
                except:
                    api_close_date = ''
                try:
                    api_create_date = api_properties['createdate']
                except:
                    api_create_date = ''
                try:
                    api_deal_name = api_properties['dealname']
                except:
                    api_deal_name = ''
                try:
                    api_deal_stage = api_properties['dealstage']
                except:
                    api_deal_stage = ''
                try:
                    api_last_modified_date = api_properties['hs_lastmodifieddate']
                except:
                    api_last_modified_date = ''
                try:
                    api_object_id = api_properties['hs_object_id']
                except:
                    api_object_id = ''
                try:
                    api_pipeline = api_properties['pipeline']
                except:
                    api_pipeline = ''
                try:
                    api_owner_id = api_properties['hubspot_owner_id']
                except:
                    api_owner_id = ''
                try:
                    api_condicoes = api_properties['condicoes_comerciais___implantacao']
                except:
                    api_condicoes = ''
                try:
                    api_total_contract = api_properties['hs_tcv']
                except:
                    api_total_contract = ''
                try:
                    api_implatacao_typeform = api_properties['implantacao__typeform____manual']
                except:
                    api_implatacao_typeform = ''
                try:
                    api_implatacao_auto = api_properties['valor_de_implantacao__automatico_']
                except:
                    api_implatacao_auto = ''
                dict.update({'id': api_id,
                             'amount': api_amount,
                             'close date': api_close_date,
                             'create date': api_create_date,
                             'deal name': api_deal_name,
                             'deal stage': api_deal_stage,
                             'last date modified': api_last_modified_date,
                             'object id': api_object_id,
                             'pipeline': api_pipeline,
                             'owner id': api_owner_id,
                             'condicoes': api_condicoes,
                             'total contrato': api_total_contract,
                             'implatacao typeform': api_implatacao_typeform,
                             'implatacao automatica': api_implatacao_auto})
                lista_hubspot.append(dict)
        except ApiException as e:
            print("Exception when calling basic_api->get_page: %s\n" % e)
    df = pd.DataFrame(lista_hubspot)
    return df

