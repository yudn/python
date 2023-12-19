#占位输出数据
inf = [('short',2),('int',4),('long',8),('long long',8)]
for type_str, size in inf:
    print('The size of {0:s} is {1:d} bytes.'.format(type_str,size))
