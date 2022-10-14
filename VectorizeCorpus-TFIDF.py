import pickle
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import TSNE

corpus = []
# 读入数据集
with open('generatedComments.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        corpus.append(line.strip('\n'))

# 预处理
# 去除所有 没有评论的数据
while '' in corpus:
    corpus.remove('')
print('Size of Corpus:', len(corpus))

# 创建 TF-IDF 向量化器
vectorizer = TfidfVectorizer()

# 对数据集每行进行向量化
vectorized_comments_matrix = vectorizer.fit_transform(corpus)
vectorized_comments_list = vectorized_comments_matrix.toarray()

# 画散点图之前，首先用 TSNE 降维
tsne = TSNE(n_components=2)
decomposition_data = tsne.fit_transform(vectorized_comments_list)
x = []
y = []
for i in decomposition_data:
    x.append(i[0])
    y.append(i[1])

fig = plt.figure(figsize=(50, 50))
ax = plt.axes()
plt.scatter(x, y, marker='x')
for i in range(len(x)):
    plt.text(x[i] * 1.01, y[i] * 1.01, i, fontsize=10)
plt.show()

# 保存向量化后的数据集结果到文件
with open('model/vectorized_comments_matrix.pkl', 'wb') as fw:
    pickle.dump(vectorized_comments_matrix, fw)

# 保存向量化器
with open('model/vectorizer.pkl', 'wb') as fw:
    pickle.dump(vectorizer, fw)