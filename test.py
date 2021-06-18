import ffmpeg_streaming
from ffmpeg_streaming import Formats, Bitrate, Representation, Size


root = r"C:\Users\admin\PycharmProjects\test2"
input_file = r"\2.mp4"
out_file = r"\out.webm"
out = r"\output_gen_file"
video = ffmpeg_streaming.input(root+input_file)


def hls_enc():
    #A path you want to save a random key to your local machine
    save_to = root+'/key'

    #A URL (or a path) to access the key on your website
    url = 'http://www.localhost.com/test2/key'
    # or url = '/"PATH TO THE KEY DIRECTORY"/key';

    hls = video.hls(Formats.h264())
    hls.encryption(save_to, url)
    hls.auto_generate_representations()
    hls.output(root+'/hls.m3u8')


hls_enc()