#houduan_student.py
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from app01.hanshu1.linked_list import LinkList
from app01 import models

#实例化对象
linked_list = LinkList()
@csrf_exempt
def manage_student(request):
    # 得到前端按钮传来的uid的值，然后进行相应的操作
    linked_list.operation_on_database()  # 把数据库数据实例化成LinkList类
    if request.method == "GET":
        uid = request.GET.get('uid')
        #用字典来存储排序类型和对应的属性名和排序方式
        sort_types = {
            1: ('no', False),2: ('no', True),
            3: ('name', False),4: ('name', True),
            5: ('sex', False),6: ('sex', True),
            7: ('birthday', False),8: ('birthday', True),
            9: ('math', False),10: ('math', True),
            11: ('chinese', False),12: ('chinese', True),
            13: ('english', False),14: ('english', True),
            15: ('total', False),16: ('total', True)
        }
        if uid is None:
            pass
        elif int(uid) in sort_types:
            attr_name, judge = sort_types[int(uid)]
            linked_list.sort_by_someone(attr_name, judge)

        students = models.database_Student.objects.all()
        return render(request, 'manage_student.html', {'students': students})
    if request.method == "POST":
        #模糊查找
        keyword = request.POST.get('keyword')
        if keyword is not None:
            #得到具有相关keyword的学生学号
            no = linked_list.search(keyword)
            students = []
            for i in no:
                # 得到符合条件keyword的学生的信息
                students += list(models.database_Student.objects.filter(student_id=i))
            return render(request, 'manage_student.html', {'students': students})

        #从数据库获得学生信息，传给用户端
        students = models.database_Student.objects.all()
        return render(request, 'manage_student.html', {'students': students})

@csrf_exempt
def delete_student(request):
    if request.method == "POST":
        # 获取要删除的学生的 ID
        student_id = request.POST.get('s_id')
        print(student_id)
        if student_id is not None:
            # 调用 LinkList 的 delete_by_no 方法，删除该学生
            linked_list.delete_by_no(student_id)

    # 从数据库获得学生信息，传给用户端
    students = models.database_Student.objects.all()
    # 重定向到 manage_student 页面
    return redirect('/manage_student/', {'students': students})

@csrf_exempt
def insert_student(request):
    if request.method == "GET":
        return render(request,'insert_student.html')

    # 从前端获得输入的信息
    student_ID = int(request.POST.get('student_ID'))
    birthday = request.POST.get('birthday')
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    chinese_score = request.POST.get('chinese_score')
    english_score = request.POST.get('english_score')
    math_score = request.POST.get('math_score')
    total_score = int(chinese_score) + int(english_score) + int(math_score)

    # 创建数据库学生数据
    models.database_Student.objects.create(student_id=student_ID,birthday=birthday,name=name,gender=gender,chinese_score=chinese_score,english_score=english_score,
                                  math_score=math_score,total_score=total_score)
    return render(request,'insert_student.html')


@csrf_exempt
def edit_student(request):
    uid = request.GET.get('uid')
    if request.method == "GET":
        data = models.database_Student.objects.filter(id=uid)
        return render(request,'edit_student.html',{'data':data})

    # 从前端获得修改的信息
    student_ID = request.POST.get('student_ID')
    birthday = request.POST.get('birthday')
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    chinese_score = request.POST.get('chinese_score')
    english_score = request.POST.get('english_score')
    math_score = request.POST.get('math_score')
    total_score = int(chinese_score) + int(english_score) + int(math_score)

    #更新数据库学生信息
    models.database_Student.objects.filter(id=uid).update(student_id=student_ID,birthday=birthday,name=name,gender=gender,chinese_score=chinese_score,english_score=english_score,
                                  math_score=math_score,total_score=total_score)
    data = models.database_Student.objects.filter(id=uid)
    return render(request, 'edit_student.html', {'data': data})
