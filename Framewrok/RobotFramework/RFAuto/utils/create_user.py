import requests

HEADERS = {
    "user-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36"
}

Default_User = {
        "name": "test1",
		"salary": "1000",
		"age": "25"
}

re = requests.post(url="http://dummy.restapiexample.com/api/v1/create", headers=HEADERS, json=Default_User)
print(re.json())
print(re.cookies.get_dict())