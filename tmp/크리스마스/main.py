import webbrowser
from datetime import datetime


def christmas_open_song():
    video_url = 'https://www.youtube.com/watch?v=aAkMkVFwAoo'
    webbrowser.open(video_url)


if __name__ == '__main__':

    expected_time = '2023-12-25 12:00:00'

    while True:
        current_time_info = datetime.now()
        actual_time = current_time_info.strftime('%Y-%m-%d %H:%M:%S')

        if actual_time == expected_time:
            print('Merry Christmas')
            christmas_open_song()
            break
