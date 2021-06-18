import subprocess
import ffmpeg
import os


class FFMConverter:

    def convert_mp4_sp(self, input_file, out_file):
        command = 'ffmpeg -i ' + input_file + ' ' + out_file
        subprocess.run(command)


input_file = r'E:\Ad project\1'
out_file = r'E:\Ad project\out'
ffm = FFMConverter()
ffm.convert_mp4_sp(input_file, out_file)