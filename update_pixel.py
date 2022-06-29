# IMPORTING LIBRARIES
import requests


def update_pixel(username, token):
    graph_id = input("Enter Graph ID: ")

    header = {"X-USER-TOKEN": token}

    try:
        month = int(input("Enter Month: "))
        year = int(input("Enter Year: "))
        day = int(input("Enter Day: "))

        if day < 10:
            day = f"0{day}"

        if month < 10:
            month = f"0{month}"

        sleep_input = int(
            input(f"How many hours did you sleep on {month}/{day}/{year}?: ")
        )
    except:
        print("Your input is in incorrect format.")
        return

    date = f"{year}{month}{day}"
    api_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}"
    params = {"quantity": str(sleep_input)}

    response = requests.put(
        url=api_endpoint,
        json=params,
        headers=header,
    )
    print(response.text)
    return
