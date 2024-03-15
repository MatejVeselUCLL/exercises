import requests
import re

def extract_urls(url):
    response = requests.get(url) # Get the html page.
    html_content = response.text
    print(html_content)

    urls_images_links = re.findall(, html_content);

def main():
    url = "https://www.bol.com"
    urls = extract_urls(url)

if __name__ == "__main__":
    main()
