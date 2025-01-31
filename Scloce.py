# import requests module
import requests

# Making a put request
response = requests.get('https://api.github.com')

# print response
print(response)

# closing the connection
response.close()

# Check if this gets executed
print("Connection Closed")
