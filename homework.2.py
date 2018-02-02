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
picture_list = os.listdir(way_Sourse) # по идее это не нужно, но я сделал
                                      #  для удобства, что бы были видны все файлы


def image_magic(picture, picture_change):
    call_programm = "convert " + os.path.join(way_Sourse, picture) +  \
                    " -resize 200 " + os.path.join(way_Result, picture_change)
    subprocess.run(call_programm)


folder()