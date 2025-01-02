import requests
from bs4 import BeautifulSoup

"""
gundamboom
=======================
리테일 업체의 재고 알림을 받을 수 있는 모듈입니다.
"""

# url = "https://gundamboom.com/product/detail.html?product_no=2525746"
url = "PLACE_YOUR_URL_HERE"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    if "구매하기" in soup.text:
        print("Product restocked!\n상품이 재입고되었습니다!")
    elif "품절" in soup.text:
        print("Product is sold out.\n상품이 아직 품절 상태입니다.")
except requests.exceptions.RequestException as e:
    print(f"Error occurred while getting the page: {e}")

# if __name__ == "__main__":
#     while True:
#         if check_stock():
#             send_slack_message(url)
#             break
#         time.sleep(3600)  # Check every hour
