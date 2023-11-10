import requests
from datetime import datetime

USERNAME = "chojdacka"
TOKEN = "weraskeid33jacospajna2"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

users_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=users_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Read Master",
    "unit": "Page",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

""" CHANGE DATE TO FORMAT PIXELA USE STRFTIME """
today=datetime.now()


pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today?"),
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

"""UPDATE PIXEL/DATA IN GRAPH """
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data={
    "quantity": "3"
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

"""DELETE DATA FROM PIXELA"""
delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_pixel, headers=headers)
print(response.text)
