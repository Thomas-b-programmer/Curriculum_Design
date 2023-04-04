# linked_list.py
from app01 import models
class LinkNode: #单链表结点类
    def __init__(self,data=None): #构造方法
        self.data=data #data属性
        self.next=None #next属性

class Student:
    def __init__(self,no,name,sex,birthday,chinese,math,english,total):
        self.no=no #学号
        self.name=name
        self.sex = sex
        self.birthday = birthday
        self.chinese = chinese
        self.math = math
        self.english = english
        self.total = total

class LinkList: #单链表类
    def __init__(self): #构造方法
        self.head=LinkNode() #头结点head
        self.head.next=None

    def Add(self, e): #在线性表的末尾添加一个元素e
        s=LinkNode(e) #新建结点s
        p=self.head
        while p.next is not None: #查找尾结点p
            p=p.next
        p.next=s #在尾结点之后插入结点

    #根据学号删除学生
    def delete_by_no(self, no):
        p = self.head.next
        pre = self.head
        while p is not None:
            if p.data.no == no:
                pre.next = p.next
                break
            pre = p
            p = p.next

        # 把操作后的学生信息写回数据库
        self.write_to_databases()

    #通过指定属性，并按此属性排序
    def sort_by_someone(self, attribute_name, judge):
        p = self.head.next
        nodes = []
        while p is not None:
            nodes.append(p.data)
            p = p.next
        nodes.sort(key=lambda x: int(getattr(x, attribute_name))
                            if getattr(x, attribute_name).isdigit()
                            else str(getattr(x, attribute_name)), reverse=judge)
        self.head.next = None
        for node in nodes:
            self.Add(node)

        # 把操作后的学生信息写回数据库
        self.write_to_databases()

    # 在线性表中查找包含关键字的元素，并返回一个包含这些元素的学生学号列表
    def search(self, keyword):
        no = []
        p = self.head.next
        while p is not None:
            if (keyword in p.data.name) or (keyword in p.data.no):
                no.append(p.data.no)
                p = p.next
            else:
                p = p.next
        return no

    #把数据库数据写入单链表
    def operation_on_database(self):
        #清空上次使用的单链表
        self.head.next = None
        # 获取数据库的数据
        students = models.database_Student.objects.all()
        #把数据库数据添加到单链表中
        for obj in students:
            self.Add(Student(obj.student_id,obj.name,obj.gender,obj.birthday,obj.chinese_score,obj.math_score,obj.english_score,obj.total_score))

    #把单链表写入数据库
    def write_to_databases(self):
        # 删除数据库中的所有学生数据
        models.database_Student.objects.all().delete()

        p = self.head.next
        while p is not None:
            models.database_Student.objects.create(student_id=p.data.no, birthday=p.data.birthday, name=p.data.name, gender=p.data.sex,
                                                   chinese_score=p.data.chinese, english_score=p.data.english,
                                                   math_score=p.data.math, total_score=p.data.total)
            p = p.next
