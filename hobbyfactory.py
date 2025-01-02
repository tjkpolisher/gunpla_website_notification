import requests
from bs4 import BeautifulSoup
import time

"""
hobbyfactory
=======================
리테일 업체 하비팩토리의 재고 알림을 받을 수 있는 모듈입니다.
"""

# url = "http://www.hobbyfactory.kr/shop/shopdetail.html?branduid=2180109"
url = "PLACE_YOUR_URL_HERE"
# slack_webhook_url = "YOUR_OWN_SLACK_WEBHOOK_URL"

# 보안 문제로 슬랙 웹훅 url을 별도의 txt 파일로 저장한 경우
# 아래 구문을 주석 해제한 뒤 파일 이름을 변경하시고 사용하시면 됩니다.
with open("webhook_url.txt", "r") as f:
    slack_webhook_url = f.read()


def check_stock():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while getting the page: {e}")
        return False

    soup = BeautifulSoup(response.content, 'html.parser')

    # Check if the product is sold out
    if "상품이 품절되었습니다." not in soup.text:
        # if "주문하기" in soup.text:
        print("Product restocked!\n상품이 재입고되었습니다!")
        return True
        # else:
        #     print("Product is sold out.\n상품이 아직 품절 상태입니다.")
        #     return False
    else:
        print("Product is sold out.\n상품이 아직 품절 상태입니다.")
        return False


def send_slack_message(url):
    message = f"상품이 재입고되었습니다: {url}"
    payload = {"text": message}

    try:
        response = requests.post(slack_webhook_url, json=payload)
        if response.status_code == 200:
            print("Slack message sent successfully!")
        else:
            print(f"Failed to send Slack message. Status code: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error occurred while sending Slack message: {e}")


def main():
    while True:
        if check_stock():
            send_slack_message(url)
            break
        time.sleep(3600)  # Check every hour


if __name__ == "__main__":
    main()
