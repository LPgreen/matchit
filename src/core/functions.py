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