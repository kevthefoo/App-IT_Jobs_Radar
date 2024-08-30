import requests, random, bs4
from bs4 import BeautifulSoup

url = "https://www.linkedin.com/jobs/search?keywords=software%20engineer&location=Australia&geoId=101452733&trk=public_jobs_jobs-search-bar_search-submit&position=1&start=50"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Cookie': 'bcookie="v=2&b46fd869-3fff-44fb-85d2-79220ddd918b"; bscookie="v=1&202408161335382b7718f1-d11c-479f-813a-0873925ece16AQGE-mRPPpJv20PT3Ae3xPw038P8kGzn"; li_rm=AQEylhh4APx7awAAAZFbc1rK3ncm5H0IRuCpEkaKV6xWdH8VS9FeeJQcu4xf1a3gGLoHQrUWYohQlUiKDly_Alj7f6O_BRyhYuq30cAot36dagx30vd2Nm1u; aam_uuid=24249839521505795093623189758378218091; _gcl_au=1.1.1349138731.1723816175; g_state={"i_l":0}; liap=true; timezone=Australia/Brisbane; li_theme=light; li_theme_set=app; li_sugr=52694aa3-9e72-417a-920e-383bf2ed5e71; _guid=d3cb8005-5399-4b5b-84e6-b3d7fc9d82f9; dfpfpt=0f18c4489cac40b0b9829f4bdaf2e8bf; li_at=AQEDAVHJ02EFhXIOAAABkVt0EdcAAAGRpjOAqFYApAGp8oMsIVnpQvKnEierHCbQC9KvtRE4SHBSp0RCufTrvoFoVWYLsuBQ6QzABeQpClG609IqtGI7VLGXt4GAh04sU_GAZrXkMFnEGC-Ql9DedLNy; JSESSIONID="ajax:1957680388491486747"; AnalyticsSyncHistory=AQJU7saQp_yx-QAAAZGHgEMCtnsb2XO4QY3GQzcwg6Cj9kvTT6PLLl5XNWou6NoTrbXfp8Nrofx6sSYS14YiCQ; lms_ads=AQHezy7GOlhBRQAAAZGHgEPkIEvbVRWdcEmwG4r-RKK8ijRJ2doCkqE8-v6aFVQWaWn5BC7ybYXkalDrnlcpYJ3P8OlxdL3e; lms_analytics=AQHezy7GOlhBRQAAAZGHgEPkIEvbVRWdcEmwG4r-RKK8ijRJ2doCkqE8-v6aFVQWaWn5BC7ybYXkalDrnlcpYJ3P8OlxdL3e; lang=v=2&lang=en-us; UserMatchHistory=AQLd_QDJC3BdqQAAAZGSP6dN8vClM_vg0xoL4tMHlddum7j5uTFxhirSN_ZWjIAp4Fi0IcYF3mbFIVW91aUhmNU0jDhlzyBmZU_wyJhhwVD1o7HgGOGzSahvlsFwK5urkbokVDo197k8eupi1yO6i42t2pqM-KRKlJV1rt5dvbijnI6uQSKYBd4jjtPX0Z42I1D8EZO0xqgRnY8NGuyTAhlfpmDyPSnlr0eqUvBjikLZ1rND_zXMDsGp7gnBgQQUXP_jNDg9VEtXxA4xR0qR1NFdKRkTZGZ67pA4Hy6hbCBiDwQYKlxynS9iRJzGCf1Ok3jWnA5DvNl1lz1dfLB9py4NP3RZVP-nRAEP-nZ72NpoK91nLw; lidc="b=OB45:s=O:r=O:a=O:p=O:g=5431:u=2:x=1:i=1724735531:t=1724821927:v=2:sig=AQG62IUajFAJNS8E2oVZs2aZpjCFvaC_"; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19963%7CMCMID%7C24072896678057561583640888578579718560%7CMCAAMLH-1725340332%7C8%7CMCAAMB-1725340332%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1724742732s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C1494580728; fptctx2=taBcrIH61PuCVH7eNCyH0J9Fjk1kZEyRnBbpUW3FKs9wsYQjfm251dUKXsx0mefLn%252bT9SoAsDGLh3NSeNkZz%252fpcvD5OVpBkYjpuNU%252fdWGPTqm7hM0YuPzHySVZFmUPzeK%252f1iUJPu9KsldwfWcwmjoXarETsNYdhWdP6SkiEI0aHVy6cI9bMwuy0KLeWaJ39Lco890r88O6V%252b%252fjeLCYjVKKtm8kuyY60sDYuzJRVhEtTqyM%252bwYLb5rQOxvlNZbgp6S8rHLg44aMgnlIi7vOtATjrUjY9KGf8KcNCJQ1VKSg%252bvdo%252bn1%252fo5v0ouuCdSp2pV4s78WauqUg%252fHaEdnqHcBMOy6tDsudiVibThZnZS7c4g%253d'
}

r = requests.get(url, headers=headers)
print(r.status_code)


soup = BeautifulSoup(r.text, 'lxml')
with open('zzzz.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())


x = soup.find_all('a', class_='job-card-list__title')

print(len(x))
for i in x:
    print(i.text.strip())
