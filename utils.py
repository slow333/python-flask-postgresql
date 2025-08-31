import os
import sys

# 현재 파일의 상위 3개 디렉토리(프로젝트 루트) 경로를 sys.path에 추가
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)