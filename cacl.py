#!/usr/bin/python3
#coding = UFT-8
'''
    好好学习，天天向上
'''
dayup0 = pow(1.001, 365)
dayup1 = pow(1.01, 365)
dayup2 = pow(1.1, 365)
daydown = pow(0.999, 365)
daydown1 = pow(0.99, 365)
daydown2 = pow(0.9, 365)
print("好好学习，天天向上")
print("向上力为1.001时365天后的结果为：{:.2f}，向上力为1.001时365天后的结果为：{:.2f},向上力为1.001时365天后的结果为：{:.2f}".format(
    dayup0, dayup1, dayup2))
print("向上力为1.001时365天后的结果为：{:.2f}，向上力为1.001时365天后的结果为：{:.2f},向上力为1.001时365天后的结果为：{:.2f}".format(
    dayup0, dayup1, dayup2))
print("向上力为1.001时365天后的结果为：{:.2f}，向上力为1.001时365天后的结果为：{:.2f},向上力为1.001时365天后的结果为：{:.2f}".format(
    dayup0, dayup1, dayup2))

print("不好好学习，天天向下")
print("向上力为0.999时365天后的结果为：{:.2f}, 向上力为 0.99时365天后的结果为：{:.2f},向上力为  0.9时365天后的结果为：{:.2f}".format(
    daydown, daydown1, daydown2))
print("向上力为0.999时365天后的结果为：{:.2f}, 向上力为 0.99时365天后的结果为：{:.2f},向上力为  0.9时365天后的结果为：{:.2f}".format(
    daydown, daydown1, daydown2))
print("向上力为0.999时365天后的结果为：{:.2f}, 向上力为 0.99时365天后的结果为：{:.2f},向上力为  0.9时365天后的结果为：{:.2f}".format(
    daydown, daydown1, daydown2))


dayup = 1.0 
dayfactor = 0.01 
for i in range(365): 
    if i % 7 in [6, 0]:        
        dayup = dayup*(1-dayfactor) 
        print("工作日的力量：{:.2f} ".format(dayup))
    else:        
        dayup = dayup*(1+dayfactor) 
        print("工作日的力量：{:.2f} ".format(dayup))



def dayUP(df):     
    dayup = 1     
    for i in range(365):        
        if i % 7 in [6,0]:           
            dayup = dayup*(1 - 0.01)        
        else:            
            dayup = dayup*(1 + df)     
        return dayup 
dayfactor = 0.01 
while dayUP(dayfactor) < 37.78:     
    dayfactor += 0.001 
print("工作日的努力参数是：{:.3f} ".format(dayfactor))       