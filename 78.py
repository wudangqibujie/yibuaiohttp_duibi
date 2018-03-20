url = "https://www.che168.com/china/dazhong/a0_0msdgscncgpi1ltocsp{}exb1x0/"
import requests
from lxml import etree
import asyncio
import aiohttp
import time

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
def get_html(url):
    r = requests.get(url,headers=headers)
    if r.status_code == 200:
        html = etree.HTML(r.text)
        return html

def parser(html):
    items = html.xpath('//*[@id="viewlist_ul"]/li')
    data = []
    # print(len(items))
    for i in items:
        j=i.xpath('a/div/h3/text()')
        data.extend(j)
    return data

async def get_post_url(url):
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as response:
            body = await response.text()
            body = etree.HTML(body)
            post_list = parser(body)
            print(post_list)
if __name__ == '__main__':
    # st = time .time()
    # loop = asyncio.get_event_loop()
    # urls = [url.format(i) for i in range(1, 50)]
    # tasks = [get_post_url(url) for url in urls]
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()
    # en = time.time()
    # print("开启异步之后的用时",(en-st))

    st1 = time .time()
    urls = [url.format(i) for i in range(1,23)]
    for i in urls:
        html = get_html(i)
        data = parser(html)
        print(data)
    en1 = time.time()
    print("普通方法用时",(en1-st1))



