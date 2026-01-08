
import requests

url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/lv.wikipedia/all-access/2025/12/04"

headers = {
    "User-Agent": "Vikipedijas-Pulss-ZPD (karlis.kirsakmens@edu.tukums.lv)"
}

exclude_pages = ["Sākumlapa", "Kontakti", "Palīdzība", "Vikipēdija:Kontakti", "Special:Search"]

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    articles = data["items"][0]["articles"]

    filtered_articles = [a for a in articles if a["article"] not in exclude_pages]

    top_5 = filtered_articles[:5]

    for article in top_5:
        print(article["article"], "-", article["views"], "skatījumi")
else:
    print("Kļūda: API nav pieejams (statusa kods:", response.status_code, ")")

