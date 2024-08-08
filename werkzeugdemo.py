from werkzeug.urls import url_quote

url = "https://example.com/search?query=hello world"
quoted_url = url_quote(url)
print(quoted_url)  # Output: https%3A//example.com/search%3Fquery%3Dhello%20world