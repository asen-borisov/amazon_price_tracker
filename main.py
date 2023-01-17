import requests
import bs4
import lxml
import smtplib

BUY_PRICE = 301
YOUR_EMAIL = "enter your email"
YOUR_PASSWORD = "enter your pass"

url = "https://www.amazon.com/Lenovo-Ideapad-Touchscreen-i3-1005G1-Processor/dp/B08B6F1NNR/ref=lp_16225007011_1_12?th=1"
header = {
    "User-Agent": "get this from: http://myhttpheader.com/",
    "Accept-Language": "get this from : http://myhttpheader.com/"
}
response = requests.get(url=url,headers=header)

soup = bs4.BeautifulSoup(response.content, "lxml")
pri = soup.find(class_="a-offscreen").getText()
new = pri.split("$")
price = float(new[1])


title = soup.find(id="productTitle").get_text().strip()

if price < BUY_PRICE:
    message = f"{title} is now ${price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )



