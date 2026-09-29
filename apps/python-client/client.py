import requests


AUTH_SERVICE_URL = "http://localhost:8001"


def login(username, password):
    response = requests.post(
        f"{AUTH_SERVICE_URL}/login",
        json={
            "username": username,
            "password": password
        }
    )

    return response


def main():

    username = input("Username: ")
    password = input("Password: ")

    try:
        response = login(username, password)

        # Convert response body to JSON
        result = response.json()

        print("\nHTTP Status:", response.status_code)

        # 200 OK
        if response.status_code == 200:

            print("\nLogin successful")
            print("User ID:", result["user_id"])
            print("Username:", result["username"])

        # 401 Unauthorized
        elif response.status_code == 401:

            print("\nLogin failed")
            print(result["message"])

        # Any other HTTP error
        else:

            print("\nUnexpected server response")
            print("Status:", response.status_code)
            print(result)

    except requests.exceptions.ConnectionError:

        print("\nUnable to connect to authentication server")
        print(f"Make sure Auth Service is running at {AUTH_SERVICE_URL}")

    except requests.exceptions.RequestException as error:

        print("\nRequest failed")
        print(error)


if __name__ == "__main__":
    main()