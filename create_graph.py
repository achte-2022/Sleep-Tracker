# IMPORTING LIBRARIES
import requests


def create_graph(username, token):
    api_endpoint = f"https://pixe.la/v1/users/{username}/graphs"

    header = {"X-USER-TOKEN": token}

    graph_id = input("Enter Graph ID: ")
    graph_name = input("Enter Graph Name: ")

    params = {
        "id": graph_id,
        "name": graph_name,
        "unit": "commit",
        "type": "int",
        "color": "kuro",
    }

    response = requests.post(
        url=api_endpoint,
        headers=header,
        json=params,
    )
    print(response.text)
    return
