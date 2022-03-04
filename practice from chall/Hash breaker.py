import requests
import hashlib
import re

if(__name__=="__main__"):

    grab_message = '----- BEGIN HASH -----<br />\r\n\t\t(\w+)'
    flag_search = 'FLAG-\w+'
    url = 'https://www.ringzer0team.com/challenges/56'
    cookie = {'PHPSESSID': '9to621vstcdm5h26mk2c7i58c0'}
    r = requests.get(url=url, cookies=cookie)
    # Extracting text from the reponse
    text = re.search(grab_message, r.text)
    hash_text = text.group(1)
    print(r.text)
    print(hash_text)

    calculated_hash = ''
    x=0
    while calculated_hash != hash_text:
        calculated_hash = hashlib.sha1(str(x).encode('utf-8')).hexdigest()
        print("%s = %s" % (calculated_hash, x))
        x += 1

    final_url = 'https://www.ringzer0team.com/challenges/56/' + str(x-1)
    data = requests.get(final_url, cookies=cookie).content
    data = data.decode().split('<div class="alert alert-info">')

    flag = re.findall(r"FLAG-\w+", data[1])
    print(flag)