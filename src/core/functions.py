import os
import json
from kivy.utils import platform


def vibro(duration: float = 0.1, amplitude: int = 150): # потом при компиляции в buildozer.spec добавить android.permissions = VIBRATE
    if platform == 'android':
        try:
            from jnius import autoclass, cast
            from android import activity  # type: ignore
            Context = autoclass('android.content.Context')
            vibrator_service = activity.getSystemService(Context.VIBRATOR_SERVICE)
            vibrator = cast('android.os.Vibrator', vibrator_service)

            # Для Android 8+ с амплитудой
            VibrationEffect = autoclass('android.os.VibrationEffect')
            effect = VibrationEffect.createOneShot(
                int(duration * 1000),  # переводим в миллисекунды
                amplitude
            )
            vibrator.vibrate(effect)

        except Exception as exc:
            print(f'Ошибка вибрации {exc}')

def get_tasks():
    directory = os.path.dirname(__file__) + r'\..\..\data\tasks'
    file_lst = os.listdir(directory)
    data_games = []
    for name in file_lst:
        with open(f'{directory}\\{name}', 'r', encoding='utf-8') as file:
            data = json.load(file)
            data_games.append(data)
    data_games.sort(key = lambda d:(d['knowledge category'], d['level'], len(d['data'])))
    return data_games


def get_settings(file_name = 'settings.json'):
    file_name = file_name
    directory = os.path.dirname(__file__) + r'\..\..\data'
    with open(fr'{directory}\{file_name}', 'r', encoding='utf-8') as file:
        return json.load(file)

def save_settings(file_name = 'settings.json',
                  number_round=0,
                  current_number_game=0,
                  difficulty=1,
                  all_wrong_answers_count=0,
                  all_right_answers_count=0,
                  font_size=None,
                  sound_volume=0.3,
                  number_rounds_session=3):
    file_name = file_name
    directory = os.path.dirname(__file__) + r'\..\..\data'

    settings = dict(number_round=number_round,
                    current_number_game=current_number_game,
                    difficulty=difficulty,
                    all_wrong_answers_count=all_wrong_answers_count,
                    all_right_answers_count=all_right_answers_count,
                    font_size=font_size
                    # sound_volume = sound_volume,
                    # number_rounds_session = number_rounds_session
                    )

    with open(fr'{directory}\{file_name}', 'w', encoding='utf-8') as file:
        json.dump(settings, file, ensure_ascii=False)
