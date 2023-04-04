class LinkNode: #单链表结点类
    def __init__(self,data=None): #构造方法
        self.data=data #data属性
        self.next=None #next属性

class LinkList: #单链表类
    def __init__(self): #构造方法
        self.head=LinkNode() #头结点head
        self.head.next=None

    def CreateListF(self, a): #头插法：由数组a整体建立单链表
        for i in range(0,len(a)): #循环建立数据结点s
            s=LinkNode(a[i]) #新建存放a[i]元素的结点s
            s.next=self.head.next #将s结点插入到开始结点之前,头结点之后
            self.head.next=s

    def Add(self, e): #在线性表的末尾添加一个元素e
        s=LinkNode(e) #新建结点s
        p=self.head
        while p.next is not None: #查找尾结点p
            p=p.next
        p.next=s #在尾结点之后插入结点

    def geti(self, i):  # 返回序号为i的结点
        p = self.head
        j = -1
        while (j < i and p is not None):
            j += 1
            p = p.next
        return p

    def Insert(self, i, e): #在线性表中序号i位置插入元素e
        assert i>=0 #检测参数i正确性的断言
        s=LinkNode(e) #建立新结点s
        p=self.geti(i-1) #找到序号为i-1的结点p
        assert p is not None #p不为空的检测
        s.next=p.next #在p结点后面插入s结点
        p.next=s

    def Delete(self,i): #在线性表中删除序号i位置的元素
        assert i>=0 #检测参数i正确性的断言
        p=self.geti(i-1) #找到序号为i-1的结点p
        assert p!=None and p.next!=None #p和p.next不为空的检测
        p.next=p.next.next #删除p结点的后继结点

    def display(self):
        p=self.head.next
        i = 1
        print('-------------学生信息----------------')
        while p is not None:
            print(f"第{i}位学生：",p.data.no, p.data.name,p.data.sex,p.data.chinese,p.data.math,p.data.english,p.data.total,end=",")
            p=p.next
            i += 1
            print()

    def delete_by_no(self, no):
        p = self.head.next
        pre = self.head
        while p is not None:
            if p.data.no == no:
                pre.next = p.next
                del p
                return True
            pre = p
            p = p.next
        return False

    def sort_by_score(self):
        # 按成绩排序
        subject = input("请输入你想要排序的学科：")
        p = self.head.next
        if hasattr(p.data,subject):
            nodes = []
            while p is not None:
                nodes.append(p.data)
                p = p.next
            nodes.sort(key=lambda x: x.subject,reverse=True)
            self.head.next = None
            for node in nodes:
                self.Add(node)
        print("没有这类学科")

    def sort_by_no(self):
        # 按学号排序
        p = self.head.next
        nodes = []
        while p is not None:
            nodes.append(p.data)
            p = p.next
        nodes.sort(key=lambda x: x.no)
        self.head.next = None
        for node in nodes:
            self.Add(node)

    def sort_by_name(self):
        # 按姓名排序
        p = self.head.next
        nodes = []
        while p is not None:
            nodes.append(p.data)
            p = p.next
        nodes.sort(key=lambda x: x.name)
        self.head.next = None
        for node in nodes:
            self.Add(node)

    def search(self, keyword):
        p = self.head.next
        while p is not None:
            if any(keyword in str(getattr(p.data, attr)) for attr in['name', 'no', 'sex', 'birthday', 'chinese', 'math', 'english', 'total']):
                p = p.next
            else:
                # 删除节点
                if p == self.head:
                    self.head = self.head.next
                else:
                    prev = self.head
                    while prev.next != p:
                        prev = prev.next
                    prev.next = p.next
                p = p.next

    def fuzzy_search(self, keyword):
        p = self.head.next
        a = 0
        while p is not None:
            if keyword in p.data.no:
                print("查找到的信息：", p.data.no, p.data.name, p.data.sex, p.data.chinese, p.data.math, p.data.english,
                      p.data.total)
                a = 1
            if keyword in p.data.name:
                print("查找到的信息：", p.data.no, p.data.name, p.data.sex, p.data.chinese, p.data.math, p.data.english,
                      p.data.total)
                a = 1
            p = p.next
        if a == 1:
            print("-----以上就是查找到的全部信息-------")
        if a == 0:
            print("------没有找到相关信息--------")


class Student:
    def __init__(self,no,name,sex,chinese,math,english,total):
        self.no=no #学号
        self.name=name
        self.sex = sex
        self.chinese = chinese
        self.math = math
        self.english = english
        self.total = total

def operate_students(linklist):
    while True:
        print("1. 添加学生")
        print("2. 修改学生信息")
        print("3. 删除学生信息")
        print("4. 按成绩排序")
        print("5. 按姓名排序")
        print("6. 按学号排序")
        print("7. 展示学生信息")
        print("8. 输入信息进行模糊查找")
        print("0. 返回上级菜单")
        op = int(input("请选择操作："))
        if op == 0:
            break
        elif op == 1:
            while True:
                try:
                    print("请输入添加的学生信息（学号 姓名 性别 语文 数学 英语 ）：")
                    no ,name, sex, chinese, math, english = input().split()
                    total = int(chinese) + int(math) + int(english)
                    print(total)
                except ValueError:
                    print("输入格式错误！")
                else:
                    student = Student(no, name, sex,chinese , math, english, total)
                    linklist.Add(student)
                    print("添加成功！")
                    break
        elif op == 2:
            print("请输入要修改的学生的学号：")
            no = input()
            p = linklist.head.next
            while p is not None:
                if p.data.no == no:
                    while True:
                        try:
                            print("请输入修改后的信息（姓名 性别 语文 数学 英语 ）：")
                            name, sex, chinese, math, english = input().split()
                            total = int(chinese) + int(math) + int(english)
                        except ValueError :
                            print("输入格式错误！")
                        else:
                            p.data.name = name
                            p.data.sex = sex
                            p.data.chinese = chinese
                            p.data.math = math
                            p.data.english = english
                            p.data.total = total
                            print("修改成功！")
                            break
                p = p.next
            else:
                print("未找到该学生！")
        elif op == 3:
            print("请输入要删除的学生的学号：")
            no = input()
            if linklist.delete_by_no(no):
                print("删除成功！")
            else:
                print("未找到该学生！")
        elif op == 4:
            linklist.sort_by_score()
            linklist.display()
        elif op == 5:
            linklist.sort_by_name()
            linklist.display()
        elif op == 6:
            linklist.sort_by_no()
            linklist.display()
        elif op == 7:
            linklist.display()
        elif op == 8:
            keyword = input("请输入你想要查找的信息：")
            linklist.fuzzy_search(keyword)
        else:
            print("无效的操作！")

linklist = LinkList()
linklist.CreateListF([Student('001', '张三', '男','85','85','85','255'), Student('002', '李三', '男','70','70','70','210'), Student('003', '王五', '男','40','40','40','120')])
linklist.search('1')