import ffmpeg_streaming
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
import urllib3, hashlib, time, json, base64
import subprocess
import atexit
import ffmpeg
import os
import sys
import scte

#-------------------------------------------------global values

#change the location of file root

root = r"C:\Users\admin\PycharmProjects\test2"

#change the name of video files here
input_file = r"\source\main.mp4"
ad1_file = r"\source\1.mp4"
ad2_file = r"\source\2.mp4"

# output_main = r"\transform\output_main.webm"
# output_ad1 = r"\transform\output_ad1.webm"
# output_ad2 = r"\transform\output_ad2.webm"

out_main = r"\transform\output_main_file"
out_ad1 = r"\transform\output_ad1_file"
out_ad2 = r"\transform\output_ad2_file"

video_main = ffmpeg_streaming.input(root+input_file)
video_ad1 = ffmpeg_streaming.input(root+ad1_file)
video_ad2 = ffmpeg_streaming.input(root+ad2_file)

print(root+out_main)
print(root+out_ad1)
print(root+out_ad2)

def video_to_hls():
    _480p = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))

    #main video to HLS Conversion
    hls_main = video_main.hls(Formats.h264())
    hls_main.representations(_480p)
    hls_main.output(root+out_main+'.m3u8')
    atexit.register(print, "Main video conversion successful!")

    # ad1 video to HLS Conversion
    hls_ad1 = video_ad1.hls(Formats.h264())
    hls_ad1.representations(_480p)
    hls_ad1.output(root+out_ad1+'.m3u8')
    atexit.register(print, "AD1 video conversion successful!")

    #ad2 video to HLS Conversion
    hls_ad2 = video_ad2.hls(Formats.h264())
    hls_ad2.representations(_480p)
    hls_ad2.output(root+out_ad2+'.m3u8')
    atexit.register(print, "AD2 video conversion successful!")


def hls_enc():
    #A path you want to save a random key to your local machine
    save_to = root+'/key'

    #A URL (or a path) to access the key on your website
    url = 'http://www.localhost.com/test2/key'
    # or url = '/"PATH TO THE KEY DIRECTORY"/key';

    #creating hls encrypted file for main video
    main_hls = video_main.hls(Formats.h264())
    main_hls.encryption(save_to, url)
    main_hls.auto_generate_representations()
    main_hls.output(root+'/hls_main.m3u8')

    # creating hls encrypted file for ad1 video
    ad1_hls = video_main.hls(Formats.h264())
    ad1_hls.encryption(save_to, url)
    ad1_hls.auto_generate_representations()
    ad1_hls.output(root + '/hls_ad1.m3u8')

    # creating hls encrypted file for ad2 video
    ad2_hls = video_main.hls(Formats.h264())
    ad2_hls.encryption(save_to, url)
    ad2_hls.auto_generate_representations()
    ad2_hls.output(root + '/hls_ad2.m3u8')



# --------------------------------------------------input parameters from user #DRIVER CODE#

print('''THIS IS A POC CODE FOR AD-INSERTION
Please enter you preference for video conversion
Select:
1 - for HLS conversion
''')

# def playlist_driver():
#     user_input_sub = input("Do you want to create a playlist for HLS live streaming (y/n): ")
#     if user_input_sub == 'y':
#         create_hls_playlist()
#     if user_input_sub == 'n':
#         sys.exit(0)


user_input = int(input("Please enter your preference: "))

if user_input == 1:
    print('You selected video conversion to HLS format. Please wait while the file is being converted...')
    video_to_hls()
    # hls_enc()
    # playlist_driver()

