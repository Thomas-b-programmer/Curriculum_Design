import heapq
import json
# 定义一个哈夫曼树类
class HuffmanNode:
    def __init__(self, value, freq):
        # 节点值，对于叶子节点，它表示一个字符；对于非叶子节点，它可以是None。
        self.value = value
        # 节点权值，即节点代表的字符在文本中出现的次数。
        self.freq = freq
        # 左子节点，如果该节点为叶子节点，则该属性为None。
        self.left = None
        # 右子节点，如果该节点为叶子节点，则该属性为None。
        self.right = None

    #定义了一个__lt__()方法，该方法将根据节点的频率（即权值）进行小于号cfdfsREaz比较运算
    def __lt__(self, other):
        return self.freq < other.freq

# 统计文本文件中各字符的个数
def count_freq(file_name):
    freq_dict = {} #{'某个字符串':对应出现的次数(权值),......}
    with open(file_name, 'r', encoding='utf-8') as f:
        while True:
            c = f.read(1)  # 从文件对象中读取一个字节
            if not c:  # 如果读取到的字节为空，表示到达了文件末尾
                break  # 退出循环，读取结束
            if c in freq_dict:
                freq_dict[c] += 1
            else:
                freq_dict[c] = 1
    return freq_dict

# 生成哈夫曼树
def build_huffman_tree(freq_dict):
    # 初始化一个空堆
    heap = []

    # 遍历频率字典中的键值对，为每个字符创建一个哈夫曼树节点，并将其加入堆中
    for key, value in freq_dict.items():
        node = HuffmanNode(key, value)
        # heap是一个列表对象，表示一个堆；node是要插入的元素，heapq会自动维护堆的特性，即堆中最小的元素位于堆顶
        heapq.heappush(heap, node)

    # 最小元素先出，循环直到堆中只剩一个节点
    while len(heap) > 1:
        # 弹出堆顶的两个最小节点
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        # 创建一个新节点，将两个最小节点作为其左右子节点，将新节点加入堆中
        new_node = HuffmanNode(None, node1.freq + node2.freq)
        new_node.left = node1
        new_node.right = node2
        heapq.heappush(heap, new_node)

    # 返回堆中剩下的最后一个节点，即哈夫曼树的根节点
    return heap[0]

# 生成哈夫曼编码表
def build_huffman_table(root):
    dict_table = {} #{'某个字符串':字符串对应的编码,.......}
    #递归遍历huffman树
    def traverse(node, code):
        if node.value is not None:
            dict_table[node.value] = code
            return
        traverse(node.left, code + '0')
        traverse(node.right, code + '1')
    traverse(root, '')
    return dict_table

def encode_with_huffman(dict_table, file_name):
    # 打开原始文件和新文件
    with open(file_name, 'r') as infile, open(file_name + '.huffman_encode', 'w') as outfile:
        # 读取原始文件内容
        original_content = infile.read()

        # 创建一个空字符串变量，用于存储哈夫曼编码后的内容
        encoded_content = ''

        # 遍历原始字符串中的每个字符
        for char in original_content:
            # 将字符对应的哈夫曼编码添加到新字符串变量中
            encoded_content += dict_table[char]

        # 将哈夫曼编码字典转换为 JSON 字符串
        dict_str = json.dumps(dict_table)

        # 将编码后的内容和字典写入新文件中
        outfile.write(dict_str + '\n')
        outfile.write(encoded_content)

def decode_with_huffman(encoded_file):
    # 打开编码文件和输出文件
    with open(encoded_file, 'r') as infile, open('new_'+encoded_file, 'w') as outfile:
        # 读取编码文件内容
        lines = infile.readlines()

        # 将哈夫曼编码字典从 JSON 字符串转换回 Python 对象
        dict_table = json.loads(lines[0])

        # 将编码字符串中的字典部分和编码部分分别取出
        encoded_content = ''.join(lines[1:])

        # 创建一个空字符串变量，用于存储解码后的内容
        decoded_content = ''

        # 反转哈夫曼编码字典，使其键值对翻转
        reversed_dict = {value: key for key, value in dict_table.items()}

        # 遍历编码字符串中的每个字符
        current_code = ''
        for char in encoded_content:
            current_code += char
            # 如果当前编码已经在反转字典中有对应的键，说明找到了一个字符
            if current_code in reversed_dict:
                # 将对应的字符添加到解码后的字符串变量中
                decoded_content += reversed_dict[current_code]
                # 重置当前编码字符串
                current_code = ''

        # 将解码后的内容写入输出文件中
        outfile.write(decoded_content)
# 测试代码
if __name__ == '__main__':
    file_name = 'huffman.txt'
    new_file_name = file_name + ".huffman_encode"
    freq_dict = count_freq(file_name)
    root = build_huffman_tree(freq_dict)
    dict_table = build_huffman_table(root)
    print(dict_table)
    encode_with_huffman(dict_table,file_name)
    decode_with_huffman(new_file_name)
