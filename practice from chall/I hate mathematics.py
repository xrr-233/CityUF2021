import requests
import hashlib
import re

if(__name__=="__main__"):

    grab_message = '----- BEGIN MESSAGE -----<br />\r\n\t\t(\w+)'
    flag_search = 'FLAG-\w+'
    url = 'https://ringzer0ctf.com/challenges/32'
    cookie = {'PHPSESSID': '9to621vstcdm5h26mk2c7i58c0'}
    r = requests.get(url=url, cookies=cookie)
    # Extracting text from the reponse
    print(r.text)

    chuli = ''
    list1 = r.text.split('\n')
    for i in range(len(list1)):
        if('BEGIN MESSAGE' in list1[i]):
            chuli = list1[i + 1]
            break

    print(chuli)
    dd = chuli.split(' ')
    dd[0] = dd[0].strip('\t')
    print(dd)

    ans = int(dd[0]) + int(dd[2],16) - int(dd[4],2)
    print(ans)

    final_url = 'https://ringzer0ctf.com/challenges/32/' + str(ans)
    data = requests.get(final_url, cookies=cookie).content
    data = data.decode().split('<div class="alert alert-info">')

    flag = re.findall(r"FLAG-\w+", data[1])
    print(flag)