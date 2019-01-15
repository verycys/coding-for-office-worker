# 클래스 class

##### Article variables

# title1 = "개발"
# author1 = "마르코"
# content1 = "개발은 쉬어요"
# view_count1 = 0

title2 = "코칭"
author2 = "마르코"
content2 = "코칭은 쉬워요"
view_count2 = 0

title3 = "창업"
author3 = "마르코"
content3 = "창업은 쉬어요"
view_count3 = 0

##### Article class
# class Article:
#     title = "개발"
#     author = "마르코"
#     content = "개발은 쉬어요"
#     view_count = 0
#
# article1 = Article()
# print(article1.title)
# article2 = Article()
# article2.title = "코칭"
# print(article1.title)
# print(article2.title)

##### Article class with __init__
class Article:
    author = "마르코"
    view_count = 0

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def read(self):
        self.view_count = self.view_count + 1

article1 = Article("개발", "개발은 쉬워요")
article2 = Article("코칭", "코칭은 쉬워요")
article3 = Article("창업", "창업은 쉬워요")

# print(article1.view_count)
# article1.read()
# print(article1.view_count)

##### Article class inheretance 상속
# class BrunchArticle:
#     author = "마르코"
#     view_count = 0
#     source = "브런치"
#
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def read(self):
#         self.view_count = self.view_count + 1

# 위의 각주처리와 아래의 상속을 활용한 코드는 같은 내용임.
class BrunchArticle(Article):
    source = "브런치"

    # 위에서는 뷰카운트 1씩 더했는데 자식클래스에서는 2씩 더해보기 (override)
    def read(self):
        self.view_count = self.view_count + 2

brunch_article = BrunchArticle("개발", "개발은 쉬워요")
print(brunch_article.title)
print(brunch_article.author)
print(brunch_article.source)
brunch_article.read()
print(brunch_article.view_count)
