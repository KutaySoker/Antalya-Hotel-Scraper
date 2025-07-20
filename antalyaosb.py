import requests

cookies = {
    'ci_session': '4f563ae583d0f58277fc2cc2eb3bfb9a02c54c54',
    'aosb-popup': 'true',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,tr;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.antalyaosb.org.tr',
    'priority': 'u=1, i',
    'referer': 'https://www.antalyaosb.org.tr/tr/firmalar',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'ci_session=4f563ae583d0f58277fc2cc2eb3bfb9a02c54c54; aosb-popup=true',
}

data = {
    'limit': '12',
    'offset': '0',
    'search-query': '',
    'sectors': '',
    'export_country': '',
}

offset_step = 12


responses = []

while True:
        
    response = requests.post(
        'https://www.antalyaosb.org.tr/tr/firmalar/getCompaniesPagination/',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    if response.text == '':
        print("No more data to fetch.")
        break
    responses.append(response)

    #increment offset
    data['offset'] = str(int(data['offset']) + offset_step)


with open('antalyaosb_data.txt', 'w', encoding='utf-8') as f:
    for response in responses:
        f.write(response.text + '\n')
        f.write('-' * 80 + '\n')