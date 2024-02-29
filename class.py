class Member:
    def __init__(self, name, username, password):
        # name = input('사용자 이름을 입력하세요: ')
        # username = input('사용자 아이디를 입력하세요: ')
        # password = input('사용자 비밀번호를 입력하세요: ')
        self.name = name
        self.username = username
        self.password = password
        members.append(self)

    def display(self):
        print(f'이름: {self.name}')
        print(f'아이디: {self.username}')


class Post:
    def __init__(self, title, content, author):
        # title = input('게시글 제목을 입력하세요: ')
        # content = input('게시글 내용을 입력하세요: ')
        self.title = title
        self.content = content
        self.author = author
        posts.append(self)


members = []
posts = []

member1 = Member(name="AAA", username="idaa", password="1234")
member2 = Member(name="BBB", username="idbb", password="5678")
member3 = Member(name="CCC", username="idcc", password="9101")

post1 = Post(title="240226", content="여행, 점심, 맑음", author=member1.name)
post2 = Post(title="240227", content="운동, 저녁, 흐림", author=member1.name)
post3 = Post(title="240228", content="휴식, 아침, 비", author=member1.name)
post4 = Post(title="240229", content="여행, 저녁, 비", author=member2.name)
post5 = Post(title="240301", content="운동, 점심, 흐림", author=member2.name)
post6 = Post(title="240302", content="휴식, 점심, 맑음", author=member2.name)
post7 = Post(title="240303", content="밥, 저녁, 맑음", author=member2.name)
post8 = Post(title="240304", content="여행, 아침, 흐림", author=member3.name)
post9 = Post(title="240305", content="운동, 점심, 비", author=member3.name)
post10 = Post(title="240306", content="밥, 저녁, 맑음", author=member3.name)

search_member = input('찾고 싶은 게시자를 입력하세요: ')
for member in members:
    if search_member in member.name:
        print(member.name)

search_content = input('찾고 싶은 단어를 입력하세요: ')
for post in posts:
    if search_content in post.content:
        print(post.title)