import re
import subprocess


#===========================   STEP:1
#### Reading the main file for EXTINF reading ####
#This function will read the main .m3u8 file and split the data into tags basis and it's time for cue point searching

def main_reader():

    main_file = open(r'C:\Users\admin\PycharmProjects\test2\transform\output_main_file_480p.m3u8', "r")
    main = main_file.readlines()

    main_extinf_list = []
    extinf_time_list = []
    for i in main:
        if 'EXTINF' in i:
            main_extinf_list.append(i)

    for i in range(len(main_extinf_list)):
        text = re.sub("[^\d\.]", "", main_extinf_list[i])
        extinf_time_list.append(text)
    # main_file.close()
    return main, main_file, extinf_time_list, main_extinf_list


#===========================   STEP:2
#### Now splitting the EXT tags from EXTINF tags ####
#This function will separate the normal EXT tags with the EXTINF tags so that we can get time data from it

def ext_splitter():
#This will get the EXTINF tags and store it in a list

    main, main_file, extinf_time_list, main_ext_inf = main_reader()
    string1 = '#EXTINF'
    string2 = 'output_main_file'
    # setting flag and index to 0
    flag = 0
    index = 0

    ext_main_list = []

    # Loop through the file line by line
    for line in main:
        index += 1

        # checking string is present in line or not
        if string1 in line:
            ext_main_list.append(main[index - 1])

        if string2 in line:
            ext_main_list.append(main[index - 1])

    # closing text file
    main_file.close()
#This will get the residual hashes apart from the EXTINF tags

    return ext_main_list

#This function will store the cue points in seconds format and create a cue list for it
def cue_inputs():
    cue_1 = 120
        # float(input('Enter the time in seconds where you want to insert the ad: '))
    cue_2_1 = 180
        # float(input('Enter the time in seconds where you want to insert the ad: '))
    cue_2_2 = 240
        # float(input('Enter the time in seconds where you want to insert the ad: '))

    cue_list = [cue_1, cue_2_1, cue_2_2]
    return cue_list


#===========================   STEP:3
#### Fetching EXTINF from AD files ####
#This function will store the EXTINF tags for ad1 and ad2 so that it can be added to main file based on cue points

def ad1_ext():
    ad1 = open(r'C:\Users\admin\PycharmProjects\test2\transform\output_ad1_file_480p.m3u8', 'r')
    count = 0
    ad1_list = []
    while True:
        count += 1
        # Get next line from file
        line = ad1.readline()
        ad1_list.append(line)
        # if line is empty
        # end of file is reached
        if not line:
            break

    ad1_list = (ad1_list[5:9])
    ad1.close()
    return ad1_list

def ad2_ext():
    ad2 = open(r'C:\Users\admin\PycharmProjects\test2\transform\output_ad2_file_480p.m3u8', 'r')
    count = 0
    ad2_list = []
    while True:
        count += 1

        # Get next line from file
        line = ad2.readline()
        ad2_list.append(line)
        # if line is empty
        # end of file is reached
        if not line:
            break

    ad2_list = (ad2_list[5:7])
    ad2.close()
    return ad2_list

#===========================   STEP:4
#### Adding EXTINF from AD files to MAIN file ####
#This functions will add the EXTINF tags for ad1 and ad2 into the main files based on the time calculation and closes cue point
#to the input time given

def ad1_insert():
    main_extinf_list, extinf_time_list, main, main_file = main_reader()
    ad1_list = ad1_ext()
    cue_list = cue_inputs()
    ext_main_list = ext_splitter()


    total = 0
    count = 0
    for ele in range(0, len(list(extinf_time_list))):
        count += 1
        total = total + float(extinf_time_list[ele])
        if total >= cue_list[0]:
            break

    for i in range(len(ad1_list)):
        list(ext_main_list).insert((count * 2) + i, ad1_list[i])
    print("inserted ad1", ext_main_list)

def ad2_insert():
    main_extinf_list, extinf_time_list, main, main_file = main_reader()
    ad2_list = ad2_ext()
    cue_list = cue_inputs()
    ext_main_list = ext_splitter()

    total = 0
    count = 0
    for ele in range(0, len(list(extinf_time_list))):
        count += 1
        total = total + float(extinf_time_list[ele])
        if total >= float(cue_list[1]):
            break

    for i in range(len(ad2_list)):
        list(ext_main_list).insert((count * 2) + i + 4, ad2_list[i])

        if total >= float(cue_list[2]):
            break

    for i in range(len(ad2_list)):
        list(ext_main_list).insert((count * 2) + i + 6, ad2_list[i])

    print("inserted ad1", ext_main_list)


#===========================   STEP:5
#### Making the filanl MANIFEST file ####
#This functions will stich the normal ext tags with the AD and MAIN EXTINF tags

def create_manifest():
    ext_main_list = ext_splitter()
    main_file = open(r'C:\Users\admin\PycharmProjects\test2\transform\output_main_file_480p.m3u8', "r")
    main = main_file.readlines()

    new_manifest = []


    for i in ext_main_list:
        new_manifest.append(i)
    new_manifest.append(main[-1])

    with open(r"C:\Users\admin\PycharmProjects\test2\transform\last_manifest.m3u8", 'w') as file_handler:
        file_handler.write(main[0])
        file_handler.write(main[1])
        file_handler.write(main[2])
        file_handler.write(main[3])
        file_handler.write(main[4])

        for item in new_manifest:
            file_handler.write("{}".format(item))

def convert_mp4():
    input_file = r'C:\Users\admin\PycharmProjects\test2\transform\last_manifest.m3u8'
    out_file = r'C:\Users\admin\PycharmProjects\test2\transform\manifest_video.mp4'
    command = 'ffmpeg -i ' + input_file + ' ' + out_file
    subprocess.run(command)

if __name__ == "__main__":

    main_reader()
    print("main_reader" + " executed")
    ext_splitter()
    print("ext_splitter" + " executed")
    ad1_ext()
    print("ad1_ext" + " executed")
    ad2_ext()
    print("ad2_ext" + " executed")
    ad1_insert()
    print("ad1_insert" + " executed")
    ad2_insert()
    print("ad2_insert" + " executed")
    create_manifest()
    print("create_manifest" + " executed")
    convert_mp4()
    print("convert_mp4" + " executed")