# IMPORTING LIBRARIES
import requests


def delete_pixel(username, token):
    graph_id = input("Enter Graph ID: ")

    try:
        month = int(input("Enter Month: "))
        year = int(input("Enter Year: "))
        day = int(input("Enter Day: "))

        if day < 10:
            day = f"0{day}"

        if month < 10:
            month = f"0{month}"

    except:
        print("Your input is in incorrect format.")
        return

    date = f"{year}{month}{day}"
    api_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}"

    header = {"X-USER-TOKEN": token}

    response = requests.delete(
        url=api_endpoint,
        headers=header,
    )
    print(response.text)
    return
