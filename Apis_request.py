# 1 making a get requests
import requests

url="https://jsonplaceholder.typicode.com/posts/1"

response= requests.get(url)

print(f"status code:{response.status_code}")
print("response content:", response.json())
# 2 making a post requests

url="https://jsonplaceholder.typicode.com/posts"

data={
    "title": "new post",
    "body": "this is the body of the new post",
    "userId":1
}

# send the post requests

response=requests.post(url,json=data)

print(f"status code:{response.status_code}")
print("response content:", response.json())

# Importance of Error Handling in APIs
url="https://jsonplaceholder.typicode.com/posts"

response=requests.get(url)

if response.status_code==200:
        print("request successful")
        # print("response content:", response.json())
else:
    print(f"error {response.status_code}: Unable to fetch data")
    print("request failed")