import shutil
import os

# from sys import platform
# if platform == "linux" or platform == "linux2":
#     # linux
#     print("Linux")
# elif platform == "darwin":
#     # OS X
#     pass
# elif platform == "win32":
#     # Windows...
#     print("Windows")


src_folder = "dir_with_subdirs"
dst_folder = "dir_flat_structure"


if not os.path.exists( dst_folder ):
    print("Create destination folder")
    os.makedirs( dst_folder )
else:
    print("Directory already exists")


print("Copy files to ", dst_folder)


thisdir = os.getcwd()
for root, directories, files in os.walk( src_folder ):
    for file in files:
        print("Copying: ", os.path.join( root, file ) )
        shutil.copy( os.path.join( root, file ), os.path.join( dst_folder, file ) )
            
print("\nDone!\n")
