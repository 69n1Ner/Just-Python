import re
import networkx as nx
import matplotlib.pyplot as plt

delimiters = (2,3,5)

def separated_division(num: int,delimiter: int) -> list[int] | None:
    if num % delimiter == 0:
        ans = []
        for _ in range(delimiter):
            ans.append(num//delimiter)
        return ans
    return None

def recalculate(lst:list[int], ordinal_num: int):
    if ordinal_num <= 0:
        raise Exception("ordinal_num must be greater than 0")
    curr_sum = 0
    for num in range(ordinal_num):
        curr_sum += lst[num]
    return curr_sum

def possible_divisions(lst:list[int],ordinal_num: int):
    ans = {}
    for delimiter in delimiters:
        curr_el = lst[ordinal_num - 1]
        curr_ans =  separated_division(curr_el, delimiter)
        if curr_ans is None:
            continue
        ans[delimiter] = curr_ans
    return ans

def div_and_change_first_possible_variant(lst:list[int], ordinal_num: int):
    all = possible_divisions(lst,ordinal_num)
    for delimiter in delimiters:
        if delimiter in all:
            lst[ordinal_num-1:ordinal_num] = all[delimiter]
            return lst,f"/{delimiter}"
    return None

def calculate_one_step(output: int,curr_sum: int,ordinal_num: int,curr_lst:list[int]):
    str_interpretation = "="
    if curr_sum > output:
        buf_lst,str_interpretation = div_and_change_first_possible_variant(curr_lst, ordinal_num)
        if buf_lst is None: raise Exception("impossible to count")
        curr_lst = buf_lst
        curr_sum = recalculate(curr_lst, ordinal_num)
    elif curr_sum < output:
        ordinal_num += 1
        str_interpretation = "+"
        curr_sum = recalculate(curr_lst, ordinal_num)
    return curr_lst, curr_sum, ordinal_num, str_interpretation

# Функция добавления ребра с автоматическим созданием узлов
def add_flow(G, source, target, weight):
    G.add_edge(source, target, weight=weight)
    # Автоматически проставляем значения, если их нет
    if 'value' not in G.nodes[source]:
        G.nodes[source]['value'] = weight
    if 'value' not in G.nodes[target]:
        G.nodes[target]['value'] = weight

def math_to_graph(G:nx.DiGraph):
    A = nx.nx_agraph.to_agraph(G)

    # Параметры расстояний:
    # ranksep — расстояние между уровнями (по умолчанию 0.5)
    # nodesep — расстояние между узлами на одном уровне (по умолчанию 0.25)
    A.graph_attr['ranksep'] = '0.3'  # сжимаем по вертикали
    A.graph_attr['nodesep'] = '0.2'  # сжимаем по горизонтали

    # Можно также задать направление
    A.graph_attr['rankdir'] = 'BT'  # TB=top-bottom, LR=left-right

    # Запускаем layout
    A.layout(prog='dot')

    # Извлекаем позиции
    pos = {
        node: tuple(map(float, A.get_node(node).attr['pos'].split(',')))
        for node in G.nodes()
    }

    # Отрисовка
    plt.figure(figsize=(8, 5))
    nx.draw_networkx_nodes(G, pos, node_size=1500, node_color='lightblue', edgecolors='gray')
    nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=40, edge_color='gray', width=2)

    node_labels = {node: f"{node}\n({data['value']})" for node, data in G.nodes(data=True)}
    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color='red')

    plt.axis('off')
    plt.show()

def calc_all(input:int,output:int):

    G = nx.DiGraph()
    G.add_node("Input", value=input)

    end = False
    curr_sum = input
    ordinal_num = 1
    curr_lst = [input]
    str_interpretation = ""
    while not end:
        curr_lst, curr_sum, ordinal_num, curr_str = calculate_one_step(output, curr_sum, ordinal_num, curr_lst)
        if curr_str == "=":
            end = True
            str_interpretation+= f" = {output}"
            continue
        elif curr_str == "+":
            prev_interpretation = re.search(r"/\d(?:/\d)*$",str_interpretation).group()
            str_interpretation += f" + {input}{prev_interpretation}"

        else:
            str_interpretation+= f"{curr_str}"
    print(f"curr_lst={curr_lst}, curr_sum={curr_sum}, ordinal_num={ordinal_num}, str_interpretation='{input}{str_interpretation}'")
    return str_interpretation

# node: /<delimiter>-№<ord_number>-L_<level>
def add_node_to_graph(G: nx.DiGraph,level:int,ordinal_num:int,delimiter:int,input:int):
    G.add_node(f"/{delimiter}-№{ordinal_num}-L{level}",level=level,weight=input//delimiter)

def connect_node_level(G: nx.DiGraph,level:int,ordinal_num:int):
    necessary_node = None
    delimiter = None
    for node in G.nodes():
        if necessary_node is None:
            lvl = int(re.match(r"-L\d+$",node).group())
            ord = int(re.match(r"-№\d+-",node).group())
            if lvl == level and ord == ordinal_num:
                necessary_node = node
                delimiter = int(re.match(r"/\d+-", node).group())

        else:
            G.add_edge(necessary_node, node, weight=G.nodes[necessary_node]['weight']//delimiter)

def str_to_graph(string:str):
    curr_sum = 0
    curr_str_num = re.match(r"\d+(?:/\d+)+", string).group()




lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# ca = possible_divisions(lst,1)
# print(div_and_change_first_possible_variant(lst, 15))
# print(calculate_one_step(90,90,1,[90,90]))
calc_all(180,36)








