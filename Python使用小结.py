#采集一个人的身高、体重、性别、年龄  计算输出体脂率是否正常

#计算BMI
def computeBMI(weight,height):
    result = weight/height*height
    return  result

#计算体质率
def computebodyfatrate(bmi,age,sex):
    result = 1.2*bmi + 0.23*age -5.4-10.8*sex
    return result

#判断是否正常
def judgeNormal(rate,sex):
    if sex == 0: #女
        if rate >=0.25 and rate <= 0.28:
            print("这位女士您的体脂率正常")
        elif rate > 0.28:
            print('这位女士您的体脂率偏高')
        else:
            print('这位女士您的体脂率偏低')

    else:  #男
        if rate >=0.15 and rate <= 0.18:
            print("这位男士您的体脂率正常")
        elif rate > 0.18:
            print('这位男士您的体脂率偏高')
        else:
            print('这位男士您的体脂率偏低')





while True:
    height = float(input("请输入您的身高是(cm):\n"))
    height = height/100

    weight = float(input('请输入您的体重是(kg):\n'))

    age = int(input('请输入您的年龄\n'))

    sex =  int(input('请输入您的性别(男输入1 女输入0):\n'))

    bmi = computeBMI(weight,height)

    rate = computebodyfatrate(bmi,age,sex)

    judgeNormal(rate,sex)

    break