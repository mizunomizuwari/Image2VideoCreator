import cv2


def create_video(image_frame_pairs, output_video_path, fps=20, loop_count=1):
    fitst_image_path = image_frame_pairs[0][0]
    fitst_image = cv2.imread(fitst_image_path)
    height, width, _ = fitst_image.shape
    
    # 全ての画像のサイズが同じ大きさかチェックする
    for image_path, _ in image_frame_pairs[1:]:
        image = cv2.imread(image_path)
        height_temp, width_temp, _ = image.shape
        if height != height_temp or width != width_temp:
            print("画像のサイズが一致しません:", fitst_image_path, "と", image_path)
            return 

    # 動画フォーマット設定
    fourcc = cv2.VideoWriter.fourcc("m", "p", "4", "v")
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for _ in range(loop_count):
        for image_path, frames in image_frame_pairs:
            img = cv2.imread(image_path)
            for _ in range(frames):
                out.write(img)

    out.release()
    print("動画を作成しました:", output_video_path)


# ~~~~~~~~~~~設定部分ここから~~~~~~~~~~~~

# 画像のパスとコマ数のタプルのリスト。
# コマ数は、指定した分だけ連続して書き込みを行います。
# FPSが20の時に20を指定すると、同じ画像が1秒間続くっていう感じですな
# 画像のサイズはすべて同じに揃えてください！！
image_frame_pairs = [
    ('image_src/image1.jpg', 10), 
    ('image_src/image2.jpg', 10), 
    ('image_src/image3.jpg', 10),
    ('image_src/image4.jpg', 10), 
    ('image_src/image5.jpg', 10), 
    ('image_src/image6.jpg', 10),
    ('image_src/image7.jpg', 10),
    ('image_src/image8.jpg', 10),
]
# 出力先ファイルパス
file_name = "output_video.mp4"
# 出力ファイルのフレームレート
fps = 20
# image_frame_pairsの書き込みを繰り返す回数
loop_count=3

# ~~~~~~~~~~~設定部分ここまで~~~~~~~~~~~~

# 動画作成
create_video(image_frame_pairs, file_name, fps=fps, loop_count=loop_count)
