'''
PDF 파일로 저장된 시험지를 페이지마다 PDF로 저장
1. 2018~2020년
2. 3,6,9,수능  # 수능은 홀수
3. 국어, 수학, 영어  # 수학은 가형
# 저장 시, 파일에 한글 X
'''
import os, glob
from pdf2image import convert_from_path

YEAR = ['2018', '2019', '2020']
TAG = ['en', 'ko', 'ma']
NAME = ['A', 'B', 'C', 'D']

INPUT_PATH = 'Data_raw'
OUTPUT_PATH = 'Data_processed'

print('<<<변환 시작>>>')
for y in YEAR:
    for subj in TAG:
        data_paths = glob.glob(os.path.join(INPUT_PATH, y, subj, '*.pdf'))
        cnt = 0
      
        for path in data_paths:
            pdf = convert_from_path(path)
          
            print('# {} - {} - {} 변환:'.format(y, subj, NAME[cnt]), end='\r')
            for n, page in enumerate(pdf):
                page.save(OUTPUT_PATH + '/' + y + '_' + subj + '_' + NAME[cnt] + '_' + str(n) + '.jpg', 'JPEG')
                print('# {} - {} - {} 변환: ({}/{})\r'.format(y, subj, NAME[cnt], n, len(pdf)), end='\r')
            print('# {} - {} - {} 변환: Done    '.format(y, subj, NAME[cnt]))
            cnt += 1
