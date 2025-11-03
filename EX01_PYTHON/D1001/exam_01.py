## [1] homework.txt, message.txt 파일 읽어서 출력
with open('./homework.txt', mode = 'r') as text1:
    print(text1.read())

with open('./message.txt', mode = 'r', encoding = 'utf-8') as text2:
    print(text2.read())


## [2] data.txt 복사해서 data_copy.txt 생성

FILE_NAME = './data_copy.txt'
with open (FILE_NAME, mode='w') as textF:
    with open('./data.txt', mode = 'r') as text1:
        cnt = textF.write(text1.read())