from django.shortcuts import render,redirect
from app01.hanshu1.encode_decode import *
from django.http import HttpResponse
from django.urls import reverse
import tempfile

def index_code(request):
    return render(request, 'encode_decode.html')


def encode_file(request):
    encoded_file_url = None

    if request.method == "POST":
        uploaded_file = request.FILES['encode-file']
        print(uploaded_file)
        file_content = uploaded_file.read().decode('utf-8')
        freq_dict = count_freq(file_content)
        root = build_huffman_tree(freq_dict)
        dict_table = build_huffman_table(root)

        encoded_content = encode_with_huffman(dict_table, file_content)
        print(encoded_content)

        # 创建一个临时文件
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            # 将编码后的内容写入临时文件
            temp_file.write(encoded_content.encode())

        # 将临时文件作为HTTP响应返回给前端
        encoded_file_url = request.build_absolute_uri(reverse('download_encoded_file', args=[temp_file.name]))

    return redirect("/index_code/", {'encoded_file_url': encoded_file_url})

def decode_file(request):
    pass

def download_encoded_file(request, file_name):
    with open(file_name, 'rb') as file:
        response = HttpResponse(file.read(), content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=encoded_file.txt'
        return response

