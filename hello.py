import webbrowser

# webbrowser.open(주소) -> 
# 주소에 해당하는 페이지가 브라우저로 열림

url = "https://search.naver.com/search.naver?query="
keywords = ["강다니엘", "방탄소년단"]

for word in keywords:
	webbrowser.open(url + word)