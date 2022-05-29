'''
데이터 부풀리기
1. 사진 크기 균일화: (가로)2339 x (세로)3309
2. 기존 데이터로 밝기 변화
3. (기존 데이터 + 밝기 변화)로 회전, 기울기 변화
4. 모든 데이터로 노이즈 변화
5. 생섣된 파일 수: ((Orig X 2) X 3) X 2
'''
from PIL import Image
import cv2, os, random, glob
import numpy as np


print('# 데이터 불러오기.....', end='')
img_list = glob.glob(os.path.join('Data_processed' ,'*.jpg'))
print('완료!\n')


print('<<<사이즈별 이미지의 종류>>>')
arr = []
for i in range(len(img_list)):
    img = cv2.imread(img_list[i])
    arr.append(img.shape)
    print('# 데이터 탐색 중....: ({}/{})'.format(i, len(img_list)), end='\r')
print('# 데이터 탐색 중....: Done' + ' '*10)
arr = set(arr)
print(arr)
print('\n')

if (len(arr)>2):
    print('<<<크기 균일화 시작>>>')
    for i in range(len(img_list)):
        img = cv2.imread(img_list[i])

        size = cv2.resize(img, (2339,3309))
        size = Image.fromarray(size, 'RGB')
        size.save(img_list[i])
        print('# 크기 균일화: ({}/{})'.format(i, len(img_list)), end='\r')
    print('# 크기 균일화: Done' + ' '*10)
    print('<<<변환 완료>>>\n')


print('# 데이터 불러오기.....', end='')
img_list = glob.glob(os.path.join('Data_processed', '*.jpg'))
print('완료!\n')


print('<<<밝기 변환 시작>>>')
for i in range(len(img_list)):
    paths = img_list[i].split('\\')
    img = cv2.imread(img_list[i])
    val = random.randrange(10, 100)
    arr = np.full(img.shape, (val, val, val), dtype=np.uint8)

    sub_dst = cv2.subtract(img, arr)

    brightness = Image.fromarray(sub_dst, 'RGB')
    brightness.save(paths[0] + '/B_' + paths[1])
    print('# 밝기 변환: ({}/{})\r'.format(i, len(img_list)), end='\r')
print('# 밝기 변환: Done' + ' '*10)
print('<<<변환 완료>>>\n')


print('# 데이터 불러오기.....', end='')
img_list = glob.glob(os.path.join('Data_processed', '*.jpg'))
print('완료!\n')


print('<<<회전 변환 시작>>>')
for i in range(len(img_list)):
    paths = img_list[i].split('\\')
    img = Image.open(img_list[i])

    rotated = img.rotate(random.randrange(-15, 15))
    rotated.save(paths[0] + '/R_' + paths[1])
    print('# 회전 변환: ({}/{})\r'.format(i, len(img_list)), end='\r')
print('# 회전 변환: Done' + ' '*10)
print('<<<변환 완료>>>\n')


print('<<<기울기 변환 시작>>>')
W = 2339 # 사진 가로
H = 3309 # 사진 세로
for i in range(len(img_list)):
    paths = img_list[i].split('\\')
    img = cv2.imread(img_list[i])
    height, width = img.shape[:2]

    pts1 = np.array(
        [[0,0], [W,0], [W,H], [0,H]],
        dtype=np.float32
    )
    inclined = random.randrange(50, 300)
    pts2 = np.array(
        [[inclined,0], [W-inclined,0], [W,H], [0,H]],
        dtype=np.float32
    )
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, matrix, (W,H))

    incl = Image.fromarray(result, 'RGB')
    incl.save(paths[0] + '/I_' + paths[1])
    print('# 기울기 변환: ({}/{})\r'.format(i, len(img_list)), end='\r')
print('# 기울기 변환: Done' + ' '*10)
print('<<<변환 완료>>>\n')


print('# 데이터 불러오기.....', end='')
img_list = glob.glob(os.path.join('Data_processed', '*.jpg'))
print('완료!\n')


print('<<<노이즈 변환 시작>>>')
for i in range(len(img_list)):
    paths = img_list[i].split('\\')
    img = cv2.imread(img_list[i])

    noized = cv2.GaussianBlur(img, (0,0), random.randint(1,3))

    noized = Image.fromarray(noized, 'RGB')
    noized.save(paths[0] + '/N_' + paths[1])
    print('# 노이즈 변환: ({}/{})\r'.format(i, len(img_list)), end='\r')
print('# 노이즈 변환: Done' + ' '*10)
print('<<<변환 완료>>>')