import random
import matplotlib.pyplot as plt

wantedSize = input('Please enter the size of the data set to be generated (default is 1000): ') or '1000'

# 先根据正态分布生成每篇文章 Comments 的长度
randCount = []

print("Generate the number of each essay's comment based on a normal distribution")

for i in range(int(wantedSize)):
    # 生成范围在 0~30 的、服从正态分布的随机数
    randCount.append(int(random.gauss(15, 5)))

count = {}

for i in range(len(randCount)):
    # 处理 randCount[i] < 0 的情况
    if randCount[i] < 0:
        randCount[i] = 0
    # 处理 randCount[i] > 30 的情况
    if randCount[i] > 30:
        randCount[i] = 30
    # 统计次数
    if randCount[i] in count:
        count[randCount[i]] += 1
    else:
        count[randCount[i]] = 1

print('The length of each randomly generated Comment is counted as:', count)

x = count.keys()
y = count.values()

plt.scatter(x, y)
plt.show()


# 定义输出的 Data Set
comments = []

# 根据观察 LANCET 数据得出的 Comments 的类别的概率分布
# 6 Content+(CP) 10%，6 Content-(CN) 10%
# 12 Language+(LP) 5%，12 Language-(LN) 55%
# 6 Organization+(OP) 10%，6 Organization-(ON) 10%
for countCurrentEssayComment in randCount:
    currentEssayComments = []
    for currentComment in range(countCurrentEssayComment):
        commentType = ['CP', 'CN', 'LP', 'LN', 'OP', 'ON']
        commentTypeWeights = [0.1, 0.1, 0.05, 0.55, 0.1, 0.1]
        randCommentType = random.choices(commentType, commentTypeWeights)[0]

        if randCommentType in ['CP', 'CN', 'OP', 'ON']:
            currentEssayComments.append(randCommentType + str(random.randint(1, 6)))
        elif randCommentType in ['LP', 'LN']:
            currentEssayComments.append(randCommentType + str(random.randint(1, 12)))
    comments.append(' '.join(currentEssayComments))

with open('generatedComments.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(comments))
input('The generated Data Set has been exported to generatedComments.txt')
