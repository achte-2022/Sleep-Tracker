# IMPORTING LIBRARIES
import requests
import datetime as dt


def post_pixel(username, token):
    graph_id = input("Enter Graph ID: ")
    api_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}"

    header = {"X-USER-TOKEN": token}
    try:
        sleep_input = int(input("How many hours did you sleep last night?: "))
    except:
        print("Your input is in incorrect format.")
        return

    date = dt.datetime.today()
    params = {"date": date.strftime("%Y%m%d"), "quantity": str(sleep_input)}

    response = requests.post(
        url=api_endpoint,
        json=params,
        headers=header,
    )
    print(response.text)
    return
