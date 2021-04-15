# LINUX ONLY
# Execute with:
# $ python convert-pcap-to-txt.py

import os
import re

def convert(srcfile, dstfile):
    command = 'tshark -x -r ' + srcfile + ' > ' + dstfile
    os.system(command)


if __name__ == '__main__':

    """ If target directory exists, delete everything """
    if ( os.path.isdir('./txt') ):
        os.system('rm -rf txt')

    """ Walk through the input files in folders and subfolders """
    for subdir, dirs, files in os.walk('/media/sf_p4sde/captures/'):
        subfoldername = re.sub('/media/sf_p4sde/captures/', '/media/sf_p4sde/captures/txts/', subdir)
        os.mkdir(subfoldername)

        for filename in files:
            filepath = subdir + os.sep + filename

            if filepath.endswith(".pcap") :
                print "Converting", filename, "into txt..."
                
                convert(filepath, subfoldername + os.sep + re.sub('.pcap', '.txt', filename))
    
    print("\nExiting")
