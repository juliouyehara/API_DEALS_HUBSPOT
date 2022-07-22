import hubspot
from pprint import pprint
from hubspot.crm.owners import ApiException
import pandas as pd

lista = []


def api_owner(client):
    try:
        api_response = client.crm.owners.owners_api.get_page(limit=200, archived=False)
        api_response = vars(api_response)
        api_response = api_response['_results']
        # pprint(api_response[1])
        for i in range(167):
            dict = {}
            api_response_results = vars(api_response[i])
            owner_id = api_response_results['_id']
            owner_name = api_response_results['_first_name']
            owner_last_name = api_response_results['_last_name']
            dict.update({'owner id': owner_id, 'owner name': owner_name, 'owner last name': owner_last_name})
            lista.append(dict)

    except ApiException as e:
        print("Exception when calling owners_api->get_page: %s\n" % e)

    df = pd.DataFrame(lista)
    return df