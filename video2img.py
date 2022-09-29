from lib2to3.pytree import Base
import os
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
global_video_path = BASE_DIR + "/video"
global_output_path = BASE_DIR + "/img"
global_step = 35   # 隔几帧抽
resize_img_size = (640, 360)        # 尽量等比例缩小

def video2img(video_path, video_name, output_path, step):
    cap = cv2.VideoCapture(video_path + "/" + video_name)
    prename = video_name.split(".")[0]
    frame_count, check_flag = 0, 0
    flag = cap.isOpened()
    while flag:
        frame_count += 1
        flag, frame = cap.read()
        #print(frame.shape)
        if frame_count % step == 0:
            if not check_flag and os.path.isfile(output_path + "/" + prename + "_" + str(frame_count / step) + ".png"):
                return
            else:
                check_flag = 1
            #frame = cv2.resize(frame, resize_img_size)
            cv2.imencode('.png', frame)[1].tofile(output_path + "/" + prename + "_" + str(frame_count / step) + ".png")

    cap.release()

if __name__ == "__main__":
    if not os.path.exists(global_output_path):
        os.makedirs(global_output_path)
    if not os.path.exists(global_video_path):
        os.makedirs(global_video_path)


    for video_name in os.listdir(global_video_path):
        video2img(global_video_path, video_name, global_output_path, global_step)

