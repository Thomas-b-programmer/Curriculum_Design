#urls.py
from django.urls import path
from app01.views import houduan_answer,houduan_student,houduan_huffman

urlpatterns = [
    #四则运算
    path('homepage_answer/',houduan_answer.homepage_answer,name = 'homepage_answer'),
    path('show_operation/',houduan_answer.show_operation,name = 'show_operation'),

    #学生管理系统
    path('manage_student/',houduan_student.manage_student),
    path('insert_student/',houduan_student.insert_student),
    path('edit_student/',houduan_student.edit_student),
    path('delete_student/', houduan_student.delete_student, name='delete_student'),

    #Huffman编码
    path('index_code/',houduan_huffman.index_code),
    path('encode/', houduan_huffman.encode_file, name='encode_file'),
    path('decode/', houduan_huffman.decode_file, name='decode_file'),

    # 新的URL模式：
    path('download_encoded_file/<str:file_name>/', houduan_huffman.download_encoded_file, name='download_encoded_file'),

]
