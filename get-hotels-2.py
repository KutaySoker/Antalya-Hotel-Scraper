import requests

cookies = {
    'entryChannel': '22',
    'entryUrl': 'https%3A%2F%2Fwww.trivago.com.tr%2F',
    'userLanguage': 'en-US',
    'edge_tid_s': 'd36bcdfb7abed25ff5d23da202',
    'edge_tid': 'd36bcdfb7abed25ff5d23da202',
    'trv_wbs': '1240',
    'trv_wb': '1240',
    'ak_bmsc': 'DEBB0D84453DF78C6A5FE1FF23B2E5A1~000000000000000000000000000000~YAAQVIYUArL3OfyXAQAAqRoLHRxsv5Nmu4HgEqMslcCSpz0RVJ34k7JyShZ9rJ5/C7L0SOl+WbJw9/tr49Hc12kATPetYSgBgPKOb+IbFV0AFM+HFCiWLg76cKv5db6Ulklji/32dJ+574skXNquSDvGE4gZOVUsip4jSQk8e09gDXDN4BxhFtvEbV33q3YjkxzOALVBHNba3Cpf00qqMNj9ctBNSqPV5PpcbLaEPJk0PgksC6JYo08tAe8EQ2kY4YhMkz0gcQGJwW77DATt+NDs+3CsftJs6zoZcRv3dt49Wf1MT6nLh87Ist4zfBxJ8IJmCFhvbjSJ0fk9emlU44JUsVUYLaxjQGxCMx7w1FPN4h6ubza/wFlKQac2352qkiPZ6bhreaeaI65PZE6cUNlKmzgTfgkPlkh7HSS5z+Kggf1Yyy0=',
    'DT_SEL': '%7B%22source%22%3A0%2C%22detail%22%3A0%7D',
    'RC_AC': '1',
    'trv_user_selection': 'rc-1-2',
}

headers = {
    'accept': 'application/graphql-response+json, application/graphql+json, application/json, text/event-stream, multipart/mixed',
    'accept-language': 'en-US,en;q=0.9,tr;q=0.8',
    'apollographql-client-name': 'hs-web-app',
    'apollographql-client-version': 'ae37537e',
    'content-type': 'application/json',
    'ect': '4g',
    'origin': 'https://www.trivago.com.tr',
    'priority': 'u=1, i',
    'referer': 'https://www.trivago.com.tr/en-US/srl/hotels-antalya-t%C3%BCrkiye?search=200-15247;dr-20250730-20250731;pa-2;rc-1-2',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'x-trv-app-id': 'HS_WEB_APP_WARP',
    'x-trv-connection-id': 'IG8UZc4aX2UNoub5UUQ1qYtHOPr',
    'x-trv-cst': '55622,46164,48405,51886,52345,56034,70018-2,70089,70246,70290,70332,70407,70579,70620-2,70623,70773-2,70785,70766,70826,70830,70928-1,70886,70806,70739-2,70511,70916,71028-1,70798,71023,71142,70841,71057-2,70819,71118-1,71230,71254,71263,71285,71292,70839,71194,71393-1,71172,71475,71469,71476,71289,71447,71460,71431,71428,71549,71550,71553-1,71554-1,71512,71498,71511,71523,71173,71569,71598,71599,71597,71633,71591,71619,71586,71402,71615,71572-1,71410,71561,71479-1,71315,71590,71734,71594,71576,71583,71560-3,71621,71654,71725-2,71700,71646,71704-2,71707,71759-1,71728,71691,71770,71581,71605-2,71029,71693-2,71726-2,71663,71680-2,71613,71716,71721,71650-1,71805,71773,71750,71699-2,71748,71743,71712,71744,71610,71715-1,71796-3,71060-1,71788,71683',
    'x-trv-currency': 'TRY',
    'x-trv-language': 'en-US',
    'x-trv-platform': 'tr',
    'x-trv-sequence-id': '49',
    'x-trv-tid': 'd36bcdfb7abed25ff5d23da202',
    # 'cookie': 'entryChannel=22; entryUrl=https%3A%2F%2Fwww.trivago.com.tr%2F; userLanguage=en-US; edge_tid_s=d36bcdfb7abed25ff5d23da202; edge_tid=d36bcdfb7abed25ff5d23da202; trv_wbs=1240; trv_wb=1240; ak_bmsc=DEBB0D84453DF78C6A5FE1FF23B2E5A1~000000000000000000000000000000~YAAQVIYUArL3OfyXAQAAqRoLHRxsv5Nmu4HgEqMslcCSpz0RVJ34k7JyShZ9rJ5/C7L0SOl+WbJw9/tr49Hc12kATPetYSgBgPKOb+IbFV0AFM+HFCiWLg76cKv5db6Ulklji/32dJ+574skXNquSDvGE4gZOVUsip4jSQk8e09gDXDN4BxhFtvEbV33q3YjkxzOALVBHNba3Cpf00qqMNj9ctBNSqPV5PpcbLaEPJk0PgksC6JYo08tAe8EQ2kY4YhMkz0gcQGJwW77DATt+NDs+3CsftJs6zoZcRv3dt49Wf1MT6nLh87Ist4zfBxJ8IJmCFhvbjSJ0fk9emlU44JUsVUYLaxjQGxCMx7w1FPN4h6ubza/wFlKQac2352qkiPZ6bhreaeaI65PZE6cUNlKmzgTfgkPlkh7HSS5z+Kggf1Yyy0=; DT_SEL=%7B%22source%22%3A0%2C%22detail%22%3A0%7D; RC_AC=1; trv_user_selection=rc-1-2',
}

json_data = {
    'extensions': {
        'persistedQuery': {
            'sha256Hash': '96baeca82d4eabf3f37fa1f7eb9e09b5e0b8bd90ba414a6c19eaac7bf1e309a2',
            'version': 1,
        },
    },
    'operationName': 'accommodationSearchQuery',
    'variables': {
        'aiGeneratedInput': {
            'filter': {
                'sentiment': 'POSITIVE',
            },
            'pagination': {
                'limit': 2,
            },
            'sorting': {
                'searchConcepts': [],
            },
        },
        'cheapestDayPerMonthInput': {
            'yearMonths': [],
        },
        'distanceLabelInput': None,
        'mainImageConcepts': [],
        'monthlyForecastedPricesInput': {
            'currencyCode': 'TRY',
            'filter': [
                {
                    'priceType': 'CHEAPEST',
                    'yearMonth': '2025-08',
                },
                {
                    'priceType': 'CHEAPEST',
                    'yearMonth': '2025-09',
                },
                {
                    'priceType': 'CHEAPEST',
                    'yearMonth': '2025-10',
                },
                {
                    'priceType': 'CHEAPEST',
                    'yearMonth': '2025-11',
                },
                {
                    'priceType': 'CHEAPEST',
                    'yearMonth': '2025-12',
                },
                {
                    'priceType': 'CHEAPEST',
                    'yearMonth': '2026-01',
                },
            ],
        },
        'params': {
            'allInRateModelOverride': False,
            'applicationGroup': 'MAIN_WARP',
            'budgetRestriction': {
                'budgetType': 'PRICE_PER_NIGHT',
                'maxPrice': 2147483647,
                'minPrice': 0,
            },
            'channel': {
                'branded': {
                    'isStandardDate': True,
                    'stayPeriodSource': {
                        'value': 0,
                    },
                },
            },
            'currency': 'TRY',
            'dealsLimit': 3,
            'deviceType': 'DESKTOP_MSEDGE',
            'includePriceHistogram': True,
            'limit': 35,
            'offset': 35,
            'rooms': [
                {
                    'adults': 2,
                    'children': [],
                },
            ],
            'searchExecutionContext': {
                'searchType': 'SINGLE_POLL_NO_DEALS',
            },
            'searchResultViewType': 'LIST_VIEW',
            'sorting': [
                {
                    'type': 0,
                },
            ],
            'stayPeriod': {
                'arrival': '2025-07-30',
                'departure': '2025-07-31',
            },
            'trafficChannel': 'SEO',
            'uiv': [
                {
                    'nsid': {
                        'id': 15247,
                        'ns': 200,
                    },
                },
            ],
        },
        'pollData': None,
        'priceSliderParams': {
            'currency': 'TRY',
            'priceHistogramAlgorithmType': 'LINEAR',
        },
        'shouldIncludeCanonicalURL': False,
        'shouldIncludeChainPlusSubscription': True,
        'shouldIncludeCheapestDayPerMonth': False,
        'shouldIncludeEligiblePartners': True,
        'shouldIncludeForecastedPriceAmount': False,
        'shouldIncludeFreeSearchDetails': False,
        'shouldIncludeFreeWiFiStatus': False,
        'shouldIncludeMainImageBasedOnConcepts': False,
        'shouldIncludeMonthlyForecastedMedianPrice': False,
        'shouldIncludeMonthlyForecastedPrices': True,
        'shouldIncludePersonalisation': True,
        'shouldIncludePriceRestrictions': False,
        'shouldIncludeRestrictedDeals': True,
        'shouldIncludeReviewsSummary': True,
        'shouldIncludeRoomTypeInfo': True,
        'shouldIncludeSEOIndexation': False,
        'shouldIncludeSlug': False,
    },
}

response = requests.post(
    'https://www.trivago.com.tr/graphql?accommodationSearchQuery',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"extensions":{"persistedQuery":{"sha256Hash":"96baeca82d4eabf3f37fa1f7eb9e09b5e0b8bd90ba414a6c19eaac7bf1e309a2","version":1}},"operationName":"accommodationSearchQuery","variables":{"aiGeneratedInput":{"filter":{"sentiment":"POSITIVE"},"pagination":{"limit":2},"sorting":{"searchConcepts":[]}},"cheapestDayPerMonthInput":{"yearMonths":[]},"distanceLabelInput":null,"mainImageConcepts":[],"monthlyForecastedPricesInput":{"currencyCode":"TRY","filter":[{"priceType":"CHEAPEST","yearMonth":"2025-08"},{"priceType":"CHEAPEST","yearMonth":"2025-09"},{"priceType":"CHEAPEST","yearMonth":"2025-10"},{"priceType":"CHEAPEST","yearMonth":"2025-11"},{"priceType":"CHEAPEST","yearMonth":"2025-12"},{"priceType":"CHEAPEST","yearMonth":"2026-01"}]},"params":{"allInRateModelOverride":false,"applicationGroup":"MAIN_WARP","budgetRestriction":{"budgetType":"PRICE_PER_NIGHT","maxPrice":2147483647,"minPrice":0},"channel":{"branded":{"isStandardDate":true,"stayPeriodSource":{"value":0}}},"currency":"TRY","dealsLimit":3,"deviceType":"DESKTOP_MSEDGE","includePriceHistogram":true,"limit":35,"offset":35,"rooms":[{"adults":2,"children":[]}],"searchExecutionContext":{"searchType":"SINGLE_POLL_NO_DEALS"},"searchResultViewType":"LIST_VIEW","sorting":[{"type":0}],"stayPeriod":{"arrival":"2025-07-30","departure":"2025-07-31"},"trafficChannel":"SEO","uiv":[{"nsid":{"id":15247,"ns":200}}]},"pollData":null,"priceSliderParams":{"currency":"TRY","priceHistogramAlgorithmType":"LINEAR"},"shouldIncludeCanonicalURL":false,"shouldIncludeChainPlusSubscription":true,"shouldIncludeCheapestDayPerMonth":false,"shouldIncludeEligiblePartners":true,"shouldIncludeForecastedPriceAmount":false,"shouldIncludeFreeSearchDetails":false,"shouldIncludeFreeWiFiStatus":false,"shouldIncludeMainImageBasedOnConcepts":false,"shouldIncludeMonthlyForecastedMedianPrice":false,"shouldIncludeMonthlyForecastedPrices":true,"shouldIncludePersonalisation":true,"shouldIncludePriceRestrictions":false,"shouldIncludeRestrictedDeals":true,"shouldIncludeReviewsSummary":true,"shouldIncludeRoomTypeInfo":true,"shouldIncludeSEOIndexation":false,"shouldIncludeSlug":false}}'
#response = requests.post(
#    'https://www.trivago.com.tr/graphql?accommodationSearchQuery',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)