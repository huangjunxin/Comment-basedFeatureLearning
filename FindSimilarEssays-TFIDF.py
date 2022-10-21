from sklearn.metrics.pairwise import cosine_similarity
import pickle

corpus = []
# 读入原始数据集
with open('generatedComments.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        corpus.append(line.strip('\n'))
# 导入向量化后的数据集
vectorized_comments_matrix = pickle.load(open('model/vectorized_comments_matrix.pkl', 'rb'))
# 导入向量化器
vectorizer = pickle.load(open('model/vectorizer.pkl', 'rb'))

currentEssayComments = input('Please enter comments from one essay: ')

# 利用向量化器对 currentEssayComments 进行向量化
vectorized_input_comments = vectorizer.transform([currentEssayComments])

# 计算余弦相似度
res = cosine_similarity(vectorized_input_comments, vectorized_comments_matrix)[0]
res_index = res.argsort()[-10:].tolist()[::-1]

print('The index of the most similar 10 essays are: ', res_index)

print('The most similar 10 essays are:')
for index in res_index:
    print(corpus[index])
