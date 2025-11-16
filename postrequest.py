import requests

r = requests.get('https://api.github.com/events')
print(r.text)

requests.post("https://httpbin.org/post", data=[("key", "value")])

url = 'https://www.w3schools.com/python/demopage.php'
myfiles = {'file': open('myfirstreact.png' ,'r')}
x = requests.post(url, files = myfiles)


url = 'https://w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}
x = requests.post(url, data = myobj, auth = ('user', 'pass'))


url = 'https://w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}
x = requests.post(url, data = myobj, stream=True)


url = 'https://w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}
x = requests.post(url, data = myobj, timeout=0.1)

token = "<YOUR_GITHUB_PA_TOKEN>"
response = requests.post(
    "https://api.github.com/user",
    auth=("", token)
)
response.status_code

url = "https://httpbin.org/post"
user_data = {
    "username": "new_user123",
    "password": "securepassword123",
    "email": "newuser@example.com"
}
response = requests.post(url, data=user_data)

if response.status_code == 200: 
    print("User registered successfully!")
    print("Response:", response.json())
else:
    print(f"Failed to register user. Status code: {response.status_code}")
    print("Response:", response.text)

requests.post("https://httpbin.org/post", data={"key": "value"})

requests.put("https://httpbin.org/put", data={"key": "value"})

requests.delete("https://httpbin.org/delete")

requests.head("https://httpbin.org/get")

requests.patch("https://httpbin.org/patch", data={"key": "value"})

requests.options("https://httpbin.org/get")