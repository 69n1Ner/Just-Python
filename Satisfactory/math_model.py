from asyncio import shield
from math import fabs
from typing import Any
from venv import logger


def separated_division(num: int,delimiter: int) -> list[Any] | None:
    if num % delimiter == 0:
        ans = []
        for _ in range(delimiter):
            ans.append(num//delimiter)
        return ans
    return None
    #raise "деление не нацело "+ str(num) +" "+ str(delimiter)
#
def recalculate(calc_list: list[Any], calc_list_index: int,required_output: int):
    intermediate_res = 0
    print("_________ recalculate _________")
    cnt = 0
    while True:

        print("cnt="+str(cnt),"current_calc_list_index="+str(calc_list_index))
        print("--intermediate_res=" + str(intermediate_res))
        intermediate_res += calc_list[cnt]
        print("++intermediate_res=" + str(intermediate_res))

        if intermediate_res == required_output:
            break
        print("cond="+str(calc_list_index == cnt))

        if calc_list_index == cnt:
            break
        cnt+=1

    print("____________________________________")
    return intermediate_res, cnt



    # for i in range(0,intermediate_input_connections_number):
    #     print("--intermediate_res=" + str(intermediate_res),"i="+str(i))
    #     intermediate_res += calc_list[i]
    #     print("++intermediate_res=" + str(intermediate_res))

    return intermediate_res

#1 input 2 outputs (1 required 1 extra)
def calculate(required_output:int,input:int):
    if input < required_output:
        raise f"Величина выхода {required_output} больше входной {input}"

    is_error = False
    best_res = ([],[])
    for delimiter in (2,3,5):
        print(f"====== new delimiter ({delimiter}) ======")
        calc_list = []
        if input == required_output:
            return [input],[]
        if is_error:
            raise "поделить не получится нацело"
        div_res = separated_division(input,delimiter)
        if div_res is None:
            if delimiter == 5: is_error = True
            continue

        calc_list.extend(div_res)
        print("-"+str(calc_list))
        intermediate_res = 0
        calc_list_index = 0 #является индексом последнего входного потока в calc_list

        current_calc_list = calc_list
        current_calc_list_index = 0
        for delimiter1 in (2,3,5):
            print(f"====== new while ({delimiter1}) ======")
            print("current_calc_list="+str(current_calc_list))
            wrong_delimiter = False
            err_counter = 0
            while not wrong_delimiter:
                # в случае когда не хватает выходов, чтобы набрать до требуемого количества
                # просто увеличиваем количество входов на 1
                # т.е. просто к intermediate_res добавляем следующий элемент из current_calc_list

                if intermediate_res > required_output:
                    print(2)
                    current_calc_list_index -= 1
                    if current_calc_list_index < 0: current_calc_list_index = 0
                    err_counter+=1
                    print("delimiter=" + str(delimiter), "delimiter1=" + str(delimiter1),
                          "current_calc_list_index=" + str(current_calc_list_index))
                    print("current_calc_list=" + str(current_calc_list))
                    print("-intermediate_res="+str(intermediate_res))
                    # print("current_calc_list[intermediate_input_connections_number]=" + str(current_calc_list[intermediate_input_connections_number]))
                    if err_counter == 4:
                        print("-----because err-----")
                        break
                    #


                    if current_calc_list_index < 0:
                        wrong_delimiter = True
                        continue
                    curr_div = separated_division(current_calc_list[current_calc_list_index],delimiter1)
                    print("curr_div="+str(curr_div))
                    if curr_div is not None:
                        current_calc_list[current_calc_list_index:current_calc_list_index+1] = curr_div
                        print("current_calc_list=" + str(current_calc_list))
                        intermediate_res,current_calc_list_index = recalculate(current_calc_list, current_calc_list_index,required_output)
                        print("+intermediate_res="+str(intermediate_res))
                    else:
                        wrong_delimiter = True

                if intermediate_res < required_output:
                    print(1)
                    print("delimiter=" + str(delimiter), "delimiter1=" + str(delimiter1), "current_calc_list_index=" + str(current_calc_list_index))
                    print("-intermediate_res="+str(intermediate_res))

                    intermediate_res,current_calc_list_index = recalculate(current_calc_list, current_calc_list_index,required_output)
                    current_calc_list_index += 1
                    # if current_calc_list_index > len(current_calc_list) - 1:
                    #     wrong_delimiter = True
                    #     continue

                    print("+intermediate_res="+str(intermediate_res))

                if intermediate_res == required_output:
                    print(3)
                    total_list = current_calc_list[0:current_calc_list_index]
                    if len(total_list) == 0: total_list.append(current_calc_list.pop(0))
                    current_calc_list[0:current_calc_list_index] = []
                    print("----------- result -----------")
                    print(total_list,current_calc_list)
                    if len(best_res[0]) < len(total_list) and sum(best_res[0]) < sum(total_list):
                        best_res = total_list,current_calc_list
                        break
                    print("---------------------------------")
    return best_res

level = 2
# stream_value : stream_amount

input =  180
required_output = 5
output = {}
# print("ans= " + str(calculate(required_output,input)))



