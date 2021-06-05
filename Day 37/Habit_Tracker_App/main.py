import requests
import os
import datetime as dt

# user_params = {
#     'token': os.environ.get('PIX_USR_TKN'),
#     'username': os.environ.get('PIX_USR_NAM'),
#     'agreeTermsOfService': "yes",
#     'notMinor': "yes",
#     }

# response = requests.post(url='https://pixe.la/v1/users', json=user_params)
# print(response.text)

USERNAME = os.environ.get('PIX_USR_NAM')
TOKEN = os.environ.get('PIX_USR_TKN')

graph_config = {
    'id': "books",
    'name': "bookreading",
    'unit': "pages",
    'type': "int",
    'color': "sora",
    }

authentication = {
    'X-USER-TOKEN': TOKEN,
    }

# response = requests.post(url=f'https://pixe.la/v1/users/{USERNAME}/graphs', json=graph_config, headers=authentication)
# print(response.text)

response = requests.post(url=f'https://pixe.la/v1/users/{USERNAME}/graphs/{graph_config["id"]}', json={"date": dt.datetime.today().strftime('%Y%m%d'), "quantity": "10"}, headers=authentication)
print(response.text)

# response = requests.put(url=f'https://pixe.la/v1/users/{USERNAME}/graphs/{graph_config["id"]}/{dt.datetime.today().strftime("%Y%m%d")}', json={"quantity": "2"}, headers=authentication)
# print(response.text)

# response = requests.delete(url=f'https://pixe.la/v1/users/{USERNAME}/graphs/{graph_config["id"]}/{dt.datetime.today().strftime("%Y%m%d")}', headers=authentication)
# print(response.text)
