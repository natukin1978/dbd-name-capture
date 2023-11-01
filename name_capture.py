import sys
import glob
import os
import subprocess
import pytesseract  # OCRライブラリ
import cv2  # OpenCVライブラリ


os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))


def resize_screenshot(image_path, target_width, target_height):
    screenshot = cv2.imread(image_path)

    # 画像のリサイズ
    resized_screenshot = cv2.resize(screenshot, (target_width, target_height))

    return resized_screenshot


args = len(sys.argv)
if args <= 1:
    print("dbd player name", file=sys.stderr)
    print("Usage:", file=sys.stderr)
    print(f"python {os.path.basename(__file__)} (image files folder)", file=sys.stderr)
    exit(1)

img_folder = sys.argv[1]

TARGET_WIDTH = 1536
TARGET_HEIGHT = 864

list_images = glob.glob(os.path.join(img_folder, "*.png"))
for image in list_images:
    # スクリーンショットの読み込み
    screenshot = resize_screenshot(image, TARGET_WIDTH, TARGET_HEIGHT)

    # プレイヤー名の表示座標
    x = 172
    y = 222
    width = 400
    height = 24

    for num in range(4):
        # プレイヤー名の領域を切り取る
        player_name_region = screenshot[y : y + height, x : x + width]

        y += 94

        # 切り取った領域をグレースケールに変換
        gray = cv2.cvtColor(player_name_region, cv2.COLOR_BGR2GRAY)

        # 画像の二値化
        threshold = cv2.threshold(gray, 78, 255, cv2.THRESH_BINARY_INV)[1]

        # cv2.imwrite(f"tmp{num}.png", threshold)

        # OCRを使用してテキストを認識
        player_name = pytesseract.image_to_string(threshold, lang="jpn")

        print(player_name, end="")  # 勝手に改行が入るので

    print()
