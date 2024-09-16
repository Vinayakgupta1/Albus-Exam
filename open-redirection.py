#Question: Create an exploit to detect an open redirection vulnerability.

import requests


def test_open_redirect(target_url, redir_param, evil_url):

    full_url = target_url + "?" + redir_param + "=" + evil_url
    
    try:

        response = requests.get(full_url, allow_redirects=False)


        if response.status_code in [301, 302, 303, 307, 308]:
            location_header = response.headers.get('Location', '')
            

            if evil_url in location_header:
                print("Oh no! This might be an open redirection vulnerability!")
                print("It tried to send us to:", location_header)
            else:
                print("There's a redirection, but it doesn't look vulnerable.")
        else:
            print("No redirection was found.")

    except Exception as e:
        print("Oops, something went wrong with the request:", e)


target_url = input("Enter the target URL (e.g., http://example.com): ")
redirect_param = input("Enter the parameter for redirection (e.g., 'next', 'url'): ")


evil_url = "http://bad-site.com"

test_open_redirect(target_url, redirect_param, evil_url)
