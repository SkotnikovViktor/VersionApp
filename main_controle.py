
def add_site():
    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    website_list = open('site_block.txt','r')
    website_list = str(website_list.read().replace('https://',''))
    print(website_list)

    if website_list[-1]=='/':
        website_list = website_list[:-1]
        print(website_list)

        pass
    website_list=[website_list]
    redirect = '127.0.0.1'
    file = open(host_path,'r+')
    content = file.read()
    print(content)
    for website in website_list:
        if website in content:
            pass
        else:
            file.write(redirect + " " + website + "\n")


add_site()




