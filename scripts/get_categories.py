import sqlite3
from ebaysdk.trading import Connection as Trading

def get_tranding_api(site_id = 0):
    app_id = "MichaBag-ca6b-45b4-aab0-b1044c2fd03e"
    dev_id = "c89fb856-8d3b-4e00-a1e0-8c2ad0306415"
    cer_id = "8dd7a41c-1af8-41ee-aa42-08e3ed9a1cca"

    token = "AgAAAA**AQAAAA**aAAAAA**MEOsWQ**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6ACloWjDpGKpwidj6x9nY+seQ**EN8BAA**AAMAAA**DJwe7KtHFcVp0TMSaV98mij/KT6FFJzxiLE9mzvhsIEeAL2YlDkMAoj6I23JbksbuNCuMLShdJd1Z6XfhYCgRH9/3iitf3zWIgrZnFWkVLsgrW80Ve0tCqbHX1uN2T5TnXmZ7/vYeITgwG9Qt31O/9/On6lod7JYBzWsBurgdWtNzuDsBHlwcPBfi7FI85fhrxsn7bknf2/0krTlS14nkXDfy1+2vjEivM+huf0rlXzOyT16Ow50VzZRNJcB4h0sxEXdai0L9RiHEVtGZdYNVpu41Lj0X61MzYcQck+RGptSy8fqYcGf39YZ6qVn/mYizWFshn6NIGTLF9F/700h8KwVCqWrk543NscxF38dmQDlZEt7mnMkfxrp6dWzniAMY14LzppDp9oZ+AMrWVZt9NfVN//wT7sIn8SSxHq/k2231Y9UqYipFxleTx8XpJts3y6IPYXkmslf6SYfOV/szuY6DkvB0ij7JrmFYSyZie3ItG29vrCmjBm1/T/4MBdcIPZwRD+Saeo0PjdIyNtnVKSP/EtdFJ/lm5IOp8WC6elL/dANaXXzPFRzBc+9MgrV9cJDjVmLTa48coqQDQq80hWxhX0HHA2h0Ky0poxeGEcu0Ytcrrjt3kyeFffh5ZVrtB08JBNfZN0yTJwRIiWsIJ0dZPL3dfzUEjawiX8Dco42gYGkZ9ETgQpR3P/6FHOJTw7O75XEzQPjwDgY5lBuRJXvMo0EiNvoxTZAlLPZFNlGY5FFLx4ySnWUn+Zzz0ZS"

    return Trading(
        appid=app_id,
        devid=dev_id,
        certid=cer_id,
        token=token,

        config_file=None,
        siteid=str(site_id))

def get_all_categories(site_id = "0"):

    api = get_tranding_api();
    callData = {
        'DetailLevel': 'ReturnAll'
    }
    response = api.execute('GetCategories', callData)


    categories = response.dict()["CategoryArray"]["Category"]

    conn = sqlite3.connect('cats/cats_'+site_id+'.db')
    c = conn.cursor()


    for cat in categories:
        query = "INSERT INTO categories VALUES (?,?,?,?,?)"

        c.execute(
            query,
            (
                cat["CategoryID"],
                cat["CategoryName"],
                cat["CategoryParentID"],
                cat["CategoryLevel"],
                int(site_id)
            )
        )

        conn.commit()


sites = ["0","2","3","15","16","23","71","77","100","101","123","146","186","193","201","203","205","207","210","211","212","216"]

for site in sites:
    conn = sqlite3.connect('cats/cats_'+site+'.db')
    c = conn.cursor()
    c.execute('''DROP TABLE if exists categories''')
    c.execute('''CREATE TABLE categories
    (id int, name text, parent int, level int, site_id int)''')
    conn.close()

    get_all_categories(site)
