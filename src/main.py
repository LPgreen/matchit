import os.path

from core.engine import MatchIt

KV_DIRS = [os.path.join(os.getcwd(), 'src')]
if __name__ == '__main__':
    MatchIt().run()

# перенес из engine установку размера окна в set window size