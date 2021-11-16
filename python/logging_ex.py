import logging
import mylib


def main():
  # 로그 생성
  logger = logging.getLogger()

  # 로그의 출력 기준 설정
  logger.setLevel(logging.INFO)

  # 로그 출력 형식
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

  # 로그 출력
  stream_handler = logging.StreamHandler()
  stream_handler.setFormatter(formatter)
  logger.addHandler(stream_handler)

  # 로그를 파일에 출력
  file_handler = logging.FileHandler('my.log')
  file_handler.setFormatter(formatter)
  logger.addHandler(file_handler)
  
  logger.info('테스트 로거입니다.')

if __name__ == '__main__':
  main()
  mylib.do_something()
  for i in range(10):
    logging.info(f'{i}번째 방문자입니다.')
  