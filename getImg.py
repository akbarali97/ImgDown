import requests
import sys

imgsets = ['07','081216']
for i in imgsets:
    count = 1
    while True:
        try:
            url = f'https://1847884116.rsc.cdn77.org/hindi/gallery/actor/aamirkhan/aamir_khan_{i}_00{count}.jpg'
            x = requests.get(url)
            if x.status_code == 404 or x.status_code == 500: break
            img_filename = url.split('/')[7]
            with open(f"./images/{img_filename}", "wb") as f:f.write(x.content)
            count += 1
        except Exception as e:
            break

