def read_file(in_file_name, out_file_name):
    line_num = 0
    with open(in_file_name) as in_file:
        data = in_file.readlines()
        print(data,"asdfghjk")
    with open(out_file_name, 'w') as out_file:
        while True:
            two_lines = data[line_num:line_num+2]
            if not two_lines:
                break
            alt_lines = two_lines[::-1]
            print(alt_lines)
            print("*****", line_num)
            out_file.writelines(alt_lines)
            line_num += 2


if __name__ == '__main__':
    read_file('rough.csv', 'rough_out.txt')