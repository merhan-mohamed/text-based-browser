import sys
import os

from bs4 import BeautifulSoup






args = sys.argv
import requests

saved_url_folder = args[0]
print(saved_url_folder)
print(os.getcwd())


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

url_dic = {'nytimes.com': nytimes_com, 'bloomberg.com': bloomberg_com}
offline_url_list = []
offline_url_list2 = []



def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    else:
        pass


def save_to_file(raw_url, url_var):
    global offline_url_list, saved_url_folder
    file_name = f"{os.getcwd()}\\{raw_url.split('.')[0]}.txt"
    with open(file_name, 'w') as file:
        file.write(url_var)
    offline_url_list.append(f"{raw_url.split('.')[0]}")
    offline_url_list2.append(f"{raw_url.split('.')[0]}" + '.com')




def get_offline_page(saved_url):
    with open(f"{os.getcwd()}\\{saved_url}.txt", 'r') as file:
        print(file.read())


# write your code here
create_folder(saved_url_folder)
while True:
    url = input()
    if url in url_dic:
        print(url_dic[url])
        save_to_file(url, url_dic[url])
    elif url in offline_url_list:
        print(get_offline_page(url))
    elif url == 'back':
        i = len(offline_url_list2)
        if i > 0:
            while (i >= 1 ):
                x = offline_url_list2.pop()
                i -= 1
            print(url_dic[x])
        else:
            print('')
    elif url.startswith('http://'):
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        t = soup.findAll('a')
        for links in t :
            title = links.string
            print(title)
    elif url == 'exit':
        break
    else:
        print('Error: Incorrect URL')


