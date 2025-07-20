import json
# open processed_hotels.json
filtererd_hotels = []
with open('processed_hotels.json', 'r', encoding='utf-8') as f:
    hotels = json.load(f)
    for hotel in hotels:
        if hotel['classification'] == 'N/A':
            continue
        if hotel['classification'] != 4 and hotel['classification'] != 5:
            continue
        if not hotel['email'] or not hotel['phone'] or not hotel['website']:
            continue
        if 'gmail' in hotel['email'] or 'hotmail' in hotel['email'] or 'yahoo' in hotel['email']:
            continue
        filtererd_hotels.append(hotel)

with open('filtered_hotels.json', 'w', encoding='utf-8') as f:
    json.dump(filtererd_hotels, f, ensure_ascii=False, indent=4)
        