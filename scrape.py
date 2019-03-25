import requests



searchterm = input("Search term to scrape: ")
searchterm = searchterm.replace(" ", "+")
writtenlinks = []
counter = 1

while True:
    form = 1
    for x in range(4):
        if form == 1:
            src = requests.get('https://www.bing.com/search?q="'+searchterm+'"+site%3Apastebin.com&first='+str(counter)+'&FORM=PERE', timeout=10).text
            links = src.split('<h2><a href="')[1:]
            for link in links:
                link = link.split('"')[0]
                if link in writtenlinks:
                    continue
                else:
                    handle = open('links.txt', 'a')
                    handle.write(link+'\n')
                    print(link)
                    writtenlinks.append(link)
        else:
            src = requests.get('https://www.bing.com/search?q="'+searchterm+'"+site%3Apastebin.com&first='+str(counter)+'&FORM=PERE'+str(form), timeout=10).text
            links = src.split('<h2><a href="')[1:]
            for link in links:
                link = link.split('"')[0]
                if link in writtenlinks:
                    continue
                else:
                    handle = open('links.txt', 'a')
                    handle.write(link+'\n')
                    print(link)
                    writtenlinks.append(link)
        form += 1
    counter += 10
