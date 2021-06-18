import m3u8
import subprocess


final_hls = r"C:\Users\admin\PycharmProjects\test2\playlist.m3u8"
final_mp4 = r"C:\xampp\htdocs\hls\final_output.mp4"


# =========================================================== Loading a playlist


playlist = m3u8.load('http://localhost/hls/index.m3u8')
print(playlist.segments)
print(playlist.target_duration)

# if you already have the content as string, use
#
# playlist = m3u8.loads('#EXTM3U8')
# playlist = m3u8.loads('#EXT-X-VERSION:3')

loader_list = [
    '#EXTM3U',
    '#EXT-X-VERSION:3',
    '#EXT-X-STREAM-INF:BANDWIDTH=550320,RESOLUTION=1280x720,NAME="720" hls_720p.m3u8',
    '#EXT-X-TARGETDURATION:4',
    '#EXT-X-INDEPENDENT-SEGMENTS',
    '#EXT-X-PROGRAM-DATE-TIME:2020-01-07T17:44:47Z',
    '#EXTINF:6.400000,no-desc',
    'Fragments(video=1583486742000000,format=m3u8-aapl-v8)',
    '#EXTINF:6.400000,no-desc',
    'Fragments(video=1583486806000000,format=m3u8-aapl-v8)',
    '#EXTINF:6.166667,no-desc',
    'Fragments(video=1583487638000000,format=m3u8-aapl-v8)',
    '#EXT-X-CUE:ID=95766,TYPE="SpliceOut",DURATION=30.000000,TIME=158348769.966667',
    '#EXTINF:0.233333,no-descs',
    'Fragments(video=1583487699666666,format=m3u8-aapl-v8)',
    '#EXT-X-CUE:ID=95766,TYPE="SpliceOut",DURATION=30.000000,TIME=158348769.966667,ELAPSED=0.233333',
    '#EXTINF:6.400000,no-desc',
    ]

for i in loader_list:
    playlist = m3u8.loads(i)

# =========================================================== Dumping a playlist


print(playlist.dumps())

# if you want to write a file from its content
# playlist.dump('playlist.m3u8')


def convert_mp4():
    command = 'ffmpeg -i ' + final_hls + ' ' + '-' \
                                               '' + ' ' + 'codec copy' + ' ' + '-' + ' ' + 'vcodec code ' + final_mp4
    print(command)
    # subprocess.run(command)

    # ffmpeg - i in.m3u8 - acodec copy - vcodec copy out.mp4

# =========================================================== Encryption keys

