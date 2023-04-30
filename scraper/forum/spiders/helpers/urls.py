"""
This tool generates list of urls to scrape, with all thread pages
Base link:

https://4programmers.net/Forum/Kariera/233131-ile_zarabiacie?page=1

"""

base_link='https://4programmers.net/Forum/Kariera/233131-ile_zarabiacie?page='

def get_urls(last_page_number):
    urls = []

    for page in range(1, last_page_number+1):
        urls.append(base_link+str(page))

    return urls

# for link in get_urls(378):
#     print(link)