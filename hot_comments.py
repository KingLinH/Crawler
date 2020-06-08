import requests
import json

def get_hot_comments(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open('hot_comments.txt','w',encoding='utf-8') as file:
        for each in hot_comments:
            file.write(each['user']['nickname'] + ':\n\n')
            file.write(each['content'] + '\n')
            file.write("------------------------------------\n")

def get_comments(url):
    name_id = url.split('=')[1]
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'referer':'https://music.163.com/song?id=4466775'}
    params ="e8v4oFAkBNJ3+JV8/PeHZOiOWSmPaPgXVJlxvdXekztyeSZRep3i/HhKYQT8/Ob3lmKj6v9Q9bgGVdh7H2yHTymIFVZOdM5UYvXnbTIMkvy5K5//x2jVkjHXJCTRLTX/GnmzfzaTWs3YvzQ16d/fEX1UmmbIMf9DuuyWHVXszxJOAFbU73Yclhr/rA1ALQ3F"
    encSecKey = "46782fb6f2e412228f93567f638a44917f38740bb2105cc4a0d539b10b4b58c0657732d2225902b02e16620d16571993b785263213fa8b9670eabe9129ee33253cdc1c909f7ebb41159da0ede50398ab6bbc88367348b7a2d5575b09831119a3bee625e9c72c90f1e69600f87af79bfd420d9ec8988b685e1ea664ad77966130"
    data = {
        'params':params,
        'encSecKey':encSecKey
        }

    target_url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(name_id)
    

    res = requests.post(target_url,headers=headers,data=data)

    return res

def main():
    url = input("请输入链接地址：")
    res = get_comments(url)
    get_hot_comments(res)


if __name__ == "__main__":
    main()
