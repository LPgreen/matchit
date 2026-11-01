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