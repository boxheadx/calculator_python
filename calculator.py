inp_str = str(input(">"))

ops = ["+", "-", "*", "/"]
nums = ["1","2","3","4","5","6","7","8","9","0"]

split_in = []
buf_ = ""
c = 0
result_buffer = 0

def set_pos(op):
    pos_buffer = 0
    op_pos = []
    for op_ in split_in:
        if(op_ == op):
            op_pos.append(pos_buffer)
        pos_buffer += 1
    return op_pos

def pop_split_in(list_, rb):
    count = 0
    for op_e in range(-1, 2):
        split_in.pop(int(list_[0] - count) + op_e)
        count += 1
    split_in.insert(int(list_[0]) - 1, rb)

for i in inp_str:
    if(i in nums):
        buf_ += str(i)

    if(i in ops):
        split_in.append(buf_)
        split_in.append(i)
        buf_ = ""

    if(c == len(inp_str) - 1):
        split_in.append(buf_)
    c += 1 

if(split_in[0] in nums):
    split_in.insert(0, "+")

print(split_in)

div_pos = []

if("/" in split_in):
    div_pos = set_pos("/")
    print("div_pos = " + str(div_pos))
    while len(div_pos) != 0:
        result_buffer = float(split_in[int(div_pos[0]) - 1]) / float(split_in[int(div_pos[0]) + 1])
        pop_split_in(div_pos, result_buffer)
        div_pos = set_pos("/")
    
    
mul_pos = []

if("*" in split_in):
    mul_pos = set_pos("*")
    print("mul_pos = " + str(mul_pos))
    while len(mul_pos) != 0:
        result_buffer = float(split_in[int(mul_pos[0]) - 1]) * float(split_in[int(mul_pos[0]) + 1])
        pop_split_in(mul_pos, result_buffer)
        mul_pos = set_pos("*")

add_pos = []
p_res_1 = 0

if("+" in split_in):
    add_pos = set_pos("+")
    print("add_pos = " + str(add_pos))
    for pos_add_n in add_pos:
        p_res_1 += float(split_in[int(pos_add_n) + 1])

sub_pos = []
p_res_2 = 0

if("-" in split_in):
    sub_pos = set_pos("-")
    print("sub_pos = " + str(sub_pos))
    for pos_sub_n in sub_pos:
        p_res_2 += float(split_in[int(pos_sub_n) + 1])

final_result = p_res_1 - p_res_2

print(final_result)
