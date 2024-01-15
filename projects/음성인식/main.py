import speech_recognition as sr

if __name__ == '__main__':
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('지금 말해주세요:')
        # 총 7초 동안 음성을 인식 합니다.
        speech = recognizer.listen(source, phrase_time_limit=7)

    try:
        audio = recognizer.recognize_google(speech, language='ko')
        print(f'인식 되어진 결과: {audio}')
    except sr.UnknownValueError:
        print('인식을 하지 못했습니다.')
    except sr.RequestError as e:
        print(f'Request error: {e}')
