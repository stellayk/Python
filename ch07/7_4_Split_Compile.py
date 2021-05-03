from re import split, match, compile

multi_line = """http://www.naver.com
http://www.daum.net
www.hongkildong.com"""

web_site = split("\n", multi_line)
print(web_site)

pat=compile("http://")

sel_site=[site for site in web_site if match(pat, site)]
print(sel_site)