# IMPORTING LIBRARIES
import requests


def create_user(username, token):
    api_endpoint = "https://pixe.la/v1/users"

    agree_TOS_input = input("Do you agree to Terms of Service(y/n)? : ").lower()
    if agree_TOS_input[0] == "y":
        agree_TOS = "yes"
    else:
        agree_TOS = "no"

    not_minor_input = input("Are you a minor(below 18 years of age)? : ").lower()
    if not_minor_input[0] == "y":
        not_minor = "no"
    else:
        not_minor = "yes"

    params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": agree_TOS,
        "notMinor": not_minor,
    }

    response = requests.post(url=api_endpoint, json=params)
    print(response.text)
    return
