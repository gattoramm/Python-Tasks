if __name__ == "__main__":
    count = int(input())
    str_num = input()
    s_num = [int(x) for x in str_num.split(' ')]
    s_num_sort = sorted(s_num)
    for _ in s_num:
        pos = s_num.index(_)
        tmp = s_num_sort[:pos] + s_num_sort[pos+1:]
        #tmp = s_num_sort.copy()
        #tmp.remove(_)
        print(tmp[(count+1)//2-1])
