# Website Crawler for Gunpla Modelers
파이썬 기반 평범한 웹사이트 크롤러입니다.  
하지만 건프라를 기다리는 모든 모델러 여러분을 위한 서비스를 만들어보려고 노력했습니다.  
  
국내 리테일 샵의 재입고 여부를 위주로 우선 구현했습니다.  
현재 리테일 샵 별로 알림 기능을 순차적으로 구현 중이며, 하나의 메인 모듈에서 각 기능을 불러오는 기능도 단계적으로 구현할 예정입니다.

## Virtual Environment
가상환경을 별도로 설치하실 때 아래와 같이 가상환경을 생성한 후 `requirements.txt`를 이용해 패키지를 설치해주세요.  
```Bash
python -m venv {venv_name}
pip install requirements.txt
```  
스크립트 실행 전, 가상환경을 먼저 활성화시켜주세요.  
```Bash
source {venv_name}/Scripts/activate
```  
## Slack Configuration
이 애플리케이션은 슬랙(Slack)의 게시판에 알림을 적용하는 방식으로 개발되었습니다.  
슬랙에 개인용 워크스페이스를 개설하신 뒤, 웹훅 API를 이용해 파이썬 스크립트에서 전송한 메시지를 출력하는 형태입니다.  
워크스페이스를 개설한 뒤, Incoming Webhooks 앱을 추가하고 웹훅 URL을 우선 발급받아야 합니다.  
자세한 발급 방법은 [Slack API 문서의 webhook 페이지](https://api.slack.com/automation/triggers/webhook)를 참고해주세요.
## Run Scripts
워크스페이스에 Incoming Webhooks 앱이 연동되었다면 해당 웹 페이지에서 웹훅 URL을 확인할 수 있을 겁니다. 이 URL을 별도로 기록해두었다가 본 애플리케이션의 `slack_webhook_url`에 복사해 붙여넣으세요.  
이후 가상환경을 활성화한 상태에서 스크립트를 실행하면 Slack과의 연동을 테스트할 수 있습니다.