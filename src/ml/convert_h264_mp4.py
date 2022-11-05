from subprocess import call 

def convert(file_h264, file_mp4):
    command = "MP4Box -add " + file_h264 + " " + file_mp4
    call([command], shell=True)
    print("\r\nRasp_Pi => Video Converted! \r\n")
    
if __name__ == "__main__":
    convert('h264.h264', 'h264.mp4')