import requests
import hashlib
import re

if(__name__=="__main__"):

    grab_message = '----- BEGIN SHELLCODE -----<br />\r\n\t\t(\w+)'
    flag_search = 'FLAG-\w+'
    url = 'https://www.ringzer0team.com/challenges/121'
    cookie = {'PHPSESSID': '9to621vstcdm5h26mk2c7i58c0'}
    r = requests.get(url=url, cookies=cookie)
    # Extracting text from the reponse
    chuli = ''
    list1 = r.text.split('\n')
    for i in range(len(list1)):
        if ('BEGIN SHELLCODE' in list1[i]):
            chuli = list1[i + 1]
            break

    chuli = chuli.strip('\t')
    print(chuli.decode('gbk'))

    final_hash = bytes(chuli, 'ascii')
    print(final_hash)
    print(b(final_hash).decode('gbk'))

    final_url = 'https://www.ringzer0team.com/challenges/14/' + final_hash
    data = requests.get(final_url, cookies=cookie).content
    data = data.decode().split('<div class="alert alert-info">')

    flag = re.findall(r"FLAG-\w+", data[1])
    print(flag)