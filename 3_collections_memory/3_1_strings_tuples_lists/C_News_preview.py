max_len = int(input())
n = int(input())
news_list = [input() for _ in range(n)]

for news in news_list:
    print(f'{news[:max_len - 3]}...' if len(news) > max_len else news)
