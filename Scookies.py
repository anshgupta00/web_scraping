import requests 

# Making a get request 
response = requests.get('https://api.github.com') 

# printing request cookies 
print(response.cookies) 
