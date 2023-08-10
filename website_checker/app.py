import requests
import csv
from fake_useragent import UserAgent
from http import HTTPStatus

def getwebsite(csv_path):
    websites = []
    with open(csv_path,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1]:
                websites.append(f'https://{row[1]}')

            else:
                websites.append(row[1])

        return websites
    
def getuseragent():
    ua = UserAgent()
    return ua.chrome

def get_status_desc(status):
    for value in HTTPStatus:
        if value == status:
            description = f'({value} {value.name}) {value.description}'
            return description
        
    return '(???) UNKNOWN STATUS CODE...'

def check_website(website,user_agent):
    try:
        code = requests.get(website, headers={'User-Agent': user_agent}).status_code
        print(website, get_status_desc(code))
    except Exception:
        print(f'could not getinformation for website: "{website}"')

def main():
    sites = getwebsite('website.csv')
    user_agent = getuseragent()

    for site in sites:
        check_website(site, user_agent)

if __name__ == '__main__':
    main()