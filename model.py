import os
import io

import openai
from google.cloud import speech
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def convert_audio_to_text(file_path: str) -> str:
    client = speech.SpeechClient()

    # Loads the audio into memory
    with io.open(file_path, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        # sample_rate_hertz=16000,  # 44100,
        language_code="ko-KR",
        audio_channel_count=2,
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript


def detect_phishing(context: str) -> str:
    """Detects phishing based on the context."""

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "당신은 사기 전담 팀에 속해있는 경찰관입니다. 보이스피싱 혹은 문자피싱을 잡아내야 합니다.",
            },
            {
                "role": "user",
                "content": f"""0점에 가까울수록 보이스피싱이 아니고, 10점에 가까울수록 보이스피싱에 해당합니다. 다음 대화가 보이스피싱일 확률을 계산해주세요.
                
                {context}

                당신의 답변은 다음과 같이 구성되면 좋겠습니다. 점수가 높다면, 왜 보이스피싱이라고 생각했는지, 그리고 점수가 낮다면 왜 보이스피싱이 아니라고 생각했는지를 설명해주세요.

                [+] 보이스피싱 점수: (숫자)
                [+] 판단 근거
                [+] 1. (이유 1)
                [+] 2. (이유 2)
                [+] 3. (이유 3)
                """,
            },
        ],
    )

    return completion.choices[0].message.content
