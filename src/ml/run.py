from detect import *

if __name__ == "__main__":
    if os.path.exists('./source.h264'):
        os.system("ffmpeg -i ./source.h264 -c:v copy src/ml/data/images/source.mp4 -y")
    os.system(
        "python3 src/ml/detect.py --weights src/ml/yolov5l.pt --source src/ml/data/images/source.mp4 --vid-stride 5")
    os.system("python3 src/ml/vectorize.py")
