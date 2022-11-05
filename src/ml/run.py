from detect import *

if __name__ == "__main__":
    if os.path.exists('/akai-code/source.h264'):
        os.system("ffmpeg -i /akai-code/source.h264 -c:v copy /akai-code/src/ml/data/images/source.mp4 -y")
    os.system(
        "python3 src/ml/detect.py --weights /akai-code/src/ml/yolov5l.pt --source /akai-code/src/ml/data/images/source.mp4 --vid-stride 5")
    os.system("python3 ./src/ml/vectorize.py")
