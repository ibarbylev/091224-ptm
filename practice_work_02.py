"""Напишите программу, которая принимает в качестве аргумента командной строки
 путь к директории и выводит список всех файлов с расширением .txt
 внутри этой директории и ее поддиректорий.
Для этой задачи используйте рекурсивную функцию, которая будет обходить
все поддиректории и искать файлы с расширением .txt.

start_directory:  /home/su/PythonProjects/IT_career_hub/Python_Morning
    [FILE]        2868  practice_tasks_07.txt
    [FILE]        2980  practice_work_08.txt
    [FILE]        3399  tasks.txt
    [FILE]          38  persons.txt
        [FILE]          27  output.txt
        [FILE]          26  input.txt
        [FILE]        1280  triangle_pascale.txt
        [FILE]         238  article.txt
    [FILE]          27  output.txt
    [FILE]        1280  pascal_triangle.txt
    [FILE]          26  input.txt
    [FILE]        1280  triangle_pascale.txt
"""
import os


def get_all_txt_files(path, indent_level=0):
    pass


start_directory = os.path.abspath('../..')
print('start_directory: ', start_directory)
get_all_txt_files(start_directory)
