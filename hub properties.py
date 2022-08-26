import hubspot
from pprint import pprint
from hubspot.crm.properties import ApiException

client = hubspot.Client.create(access_token="pat-na1-6f7c3193-8e83-4bae-a6ea-257a74e09b78")

try:
    api_response = client.crm.properties.core_api.get_all(object_type="deals", archived=False)
    # pprint(api_response)
except ApiException as e:
    print("Exception when calling core_api->get_all: %s\n" % e)

api = vars(api_response)
# pprint(len(api['_results']))
lista = []
pprint(api)
# for i in range(len(api['_results'])):
#     api_var = vars(api['_results'][i])
#     # pprint(api_var['_name'])
#     lista.append(api_var['_name'])
# print(lista)


