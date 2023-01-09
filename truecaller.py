#copy this code with credits
import requests
def print_callerid_banner():
print('              .__  .__               .__    .___')
print('  ____ _____  |  | |  |   ___________|__| __| _/')
print('_/ ___\\__  \ |  | |  | _/ __ \_  __ \  |/ __ |') 
print('\  \___ / __ \|  |_|  |_\  ___/|  | \/  / /_/ |') 
print(' \___  >____  /____/____/\___  >__|  |__\____ |') 
print('     \/     \/               \/              \/ ')
print('coded by @cybermasterteam')
print_callerid_banner()
# Get the phone number and API key from the user
phone_number = input('Enter a phone number: ')
api_key = input('Enter your Truecaller API key: ')

# Send the request to the Truecaller API
url = f'https://api.truecaller.com/v2/search?q={phone_number}'
headers = {'Authorization': f'Bearer {api_key}'}
response = requests.get(url, headers=headers)

# Parse the JSON response from the Truecaller API
response_json = response.json()

# Print the response in a user-friendly way
if 'error' in response_json:
    # An error occurred
    print(f'Error: {response_json["error"]}')
else:
    # No error occurred
    phone_info = response_json['phoneInfo']
    print(f'Name: {phone_info["name"]}')
    print(f'Country: {phone_info["country"]}')
    print(f'City: {phone_info["city"]}')
    print(f'Provider: {phone_info["provider"]}')
