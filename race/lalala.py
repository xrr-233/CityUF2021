import requests
import hashlib
import re

if(__name__=="__main__"):

    grab_message = 'CITYUF'
    url = 'http://cityf01.cs.cityu.edu.hk:30002/main.html'
    # cookie = {'PHPSESSID': '9to621vstcdm5h26mk2c7i58c0'}
    r = requests.get(url=url)
    # Extracting text from the reponse
    print(r.text)

    chuli = ''
    list1 = r.text.split('\n')
    for i in range(len(list1)):
        print("!")
        if ('{' in list1[i] or '}' in list1[i]): # 直接筛{}号
            print(list1[i])

    text = re.search(grab_message, r.text)
    hash_text = text.group(1)
    # print(hash_text)
    final_hash = hashlib.sha512(hash_text.encode('utf-8')).hexdigest()
    # print(final_hash)

    final_url = 'https://www.ringzer0team.com/challenges/13/' + final_hash
    data = requests.get(final_url, cookies=cookie).content
    data = data.decode().split('<div class="alert alert-info">')

    flag = re.findall(r"FLAG-\w+", data[1])
    print(flag)