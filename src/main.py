import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'core'))
from core.engine import MatchIt

if __name__ == '__main__':
    MatchIt().run()

# перенес из engine установку размера окна в set window size