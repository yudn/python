import itertools  
  
# 定义三个列表，每个列表包含a,b,c,d,e,f  
list1 = ['a', 'b', 'c', 'd', 'e', 'f']  
list2 = ['a', 'b', 'c', 'd', 'e', 'f']  
list3 = ['a', 'b', 'c', 'd', 'e', 'f']  
  
# 使用itertools.product生成所有可能的组合  
combinations = list(itertools.product(list1, list2, list3))  
print(combinations)
# 输出所有组合结果  
for combination in combinations:  
    print(combination)