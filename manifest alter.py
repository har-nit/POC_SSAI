import m3u8
import subprocess


final_hls = r"C:\Users\admin\PycharmProjects\test2\playlist.m3u8"
final_mp4 = r"C:\xampp\htdocs\hls\final_output.mp4"


# =========================================================== Loading a playlist

playlist = m3u8.load('http://localhost/hls/index.m3u8')
print(playlist.segments)
print(playlist.target_duration)
#
# final Pattern pattern = Pattern.compile("^#EXT-X-STREAM-INF:.*BANDWIDTH=(\\d+).*RESOLUTION=([\\dx]+).*");
#
# Matcher matcher = pattern.matcher("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=476416,RESOLUTION=416x234");
# String bandwidth = "";
# String resolution = "";
#
# if (matcher.find()) {
#     bandwidth = matcher.group(1);
#     resolution = matcher.group(2);
# }















def convert_mp4():
    command = 'ffmpeg -i ' + final_hls + ' ' + '-' \
                                               '' + ' ' + 'codec copy' + ' ' + '-' + ' ' + 'vcodec code ' + final_mp4
    print(command)
    # subprocess.run(command)

    # ffmpeg - i in.m3u8 - acodec copy - vcodec copy out.mp4

# =========================================================== Encryption keys

