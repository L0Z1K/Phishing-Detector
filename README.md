# Phishing-Detector
Detect whether the context is related to phishing with LLMs. 

## Quick Demo

### Example 1 - Voice Phishing

https://user-images.githubusercontent.com/64528476/235434243-b2d29370-f43c-4b84-994a-b02e90f9043b.mov

```bash
[+] Context: 그럼 관련해서 몇 가지 드렸고요 예 예 서울중앙지검 서울중앙지검 이요
[+] 보이스피싱 점수: 8점
[+] 그렇게 판단한 이유
[+] 1. 피싱범이 "서울중앙지검"이라는 단어를 반복해서 사용하여 신뢰성을 유도하려 한다.
[+] 2. 피싱범이 "드렸고요 예 예"와 같이 중얼거리는 식으로 말을 하여 다른 사람인 척 하고 있다.
[+] 3. 피싱범이 구체적인 사유 없이 "관련해서 몇 가지 드렸고요"와 같이 모호한 언어를 사용하고 있다.
```

### Example 2 - Voice Phishing

https://user-images.githubusercontent.com/64528476/235436189-7ba318cd-3c29-41af-b8f6-bff0a77a7874.mov

```bash
[+] Context: 제가 지금 임태용 관련해서 보니까 요즘 언니는요 검찰에서 임태현 주범으로 있는 금융범죄 자기주식을 했는데요 현장에 명의로 된 우리은행 건 통장에 같이 관련 연락 드렸습니다 제 통장에
[+] 보이스피싱 점수: 9
[+] 그렇게 판단한 이유
[+] 1. 세부적인 금융 관련 정보를 언급하여 피해자의 경계심을 낮춤.
[+] 2. 긴급성을 강조하여 판단을 서두르게 함.
[+] 3. 불필요한 상황 설명과 부연설명이 포함되어 이해하기 어려움.
```

### Example 3 - Just a normal conversation

This is just a normal conversation but the model still gives a high score.

https://user-images.githubusercontent.com/64528476/235436198-9c7ed161-2797-4b55-ab0c-551eaad028ff.mov

```bash
[+] Context: 네 이번에 그 휴복학 관련해서 서류 준비하는 것 때문에 전화 드렸는데요 오실 때 서류 좀 챙겨 오셔야 할게 있어서 그거 알려 드리려고 전화 드렸고요 아예
[+] 보이스피싱 점수: 7
[+] 판단 근거
[+] 1. 전화 번호를 알리지 않은 상태에서 파견 대상 서류를 준비하라는 메시지를 전달하는 것은 이상합니다.
[+] 2. "서류 좀 챙겨 오셔야 할게 있어서 그거 알려 드리려고 전화 드렸고요 아예"라는 문장에서 특정한 이름이나 회사명, 부서명 등의 정보가 전혀 없습니다. 이러한 상황에서는 보이스피싱 혹은 문자피싱일 가능성이 높습니다.
[+] 3. 또한 발신자의 음성이 신뢰성이 없거나 익숙하지 않은 발음, 억양, 어감 등의 특징이 있다면 의심이 더욱 커집니다. 하지만, 정확한 판단을 위해서는 추가적인 정보가 필요할 수 있습니다.
```

## Requirements

- OpenAI API key
- Google Cloud Speech Credentials