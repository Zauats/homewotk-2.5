import os
import subprocess

def folder():
    file_list = os.listdir(os.getcwd())
    if "Result" in file_list:
        pass
    else:
        os.mkdir("Result")


way_Sourse = os.path.join(os.getcwd(), "Source")
way_Result = os.path.join(os.getcwd(), "Result")


def image_magic():
    picture_list = os.listdir(way_Sourse)
    index = 1
    for picture in picture_list:
        call_programm = "convert " + os.path.join(way_Sourse, picture) + \
                        " -resize 200 " + os.path.join(way_Result, str(index))
        index += 1
        subprocess.run(call_programm)


folder()