import os

# 입력
# file_name = input("파일 이름을 입력하세요 : ")
file_name = '502018850_KO_cnt_1.vtt'

# 입력 파일 읽기
file_data = open(file_name, 'r')

# 파일 저장
file_storage = file_data.read()

# 문자열 바꾸기
file_storage = file_storage.replace("line:90%,end position:50%,center align:center","")

# 입력 파일 출력
print(file_storage)

# 파일 정리
file_data.close()
