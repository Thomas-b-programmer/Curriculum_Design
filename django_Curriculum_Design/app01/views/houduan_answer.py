#houduan_answer.py
import json
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from app01.hanshu1.for_answer import Generate_listof_option_question_answer,evaluate_expression

@csrf_exempt
def homepage_answer(request):
    """视图函数"""

    # GET请求
    if request.method == 'GET':
        # 调用 Generate_listof_option_question_answer 函数生成包含题目、选项和答案的列表
        list_data = Generate_listof_option_question_answer()
        # 渲染 homepage_for_answer.html 模板并传递数据列表
        return render(request, 'homepage_for_answer.html', {"list_data": list_data})

    # POST请求
    # 获取list_data_hidden的值
    list_data_hidden = request.POST.get('list_data_hidden')
    # 将字符串转换为 Python 对象，使用 JSON 解析器，单引号替换为双引号
    list_data = json.loads(list_data_hidden.replace("'", "\""))
    score = 0

    for i in range(1,11):
        str_option =  "answer_" + str(i)
        if request.POST.get(str_option) != list_data[i-1]['answer']:
            list_data[i-1]['judge'] = 0
        elif request.POST.get(str_option) == list_data[i-1]['answer']:
            list_data[i-1]['judge'] = 1
            score += 10
        else:
            list_data[i-1]['judge'] = 2



    list_key = ['score']
    list = []
    list.append(score)
    dict_score = dict(zip(list_key, list))
    list_score = []
    list_score.append(dict_score)

    # 渲染 jieguo_page_for_answer.html 模板并传递数据列表
    return render(request, 'jieguo_page_for_answer.html', {"list_data": list_data,'list_score':list_score
                                                        })
@csrf_exempt
def show_operation(request):

    if request.method == "GET":
        return render(request,'operation.html')
    operation = request.POST.get('opration')
    list_opration = evaluate_expression(operation)

    # 渲染 operation.html 模板并传递数据列表
    return render(request, 'operation.html', {"list_operation": list_opration,'operation':operation})

