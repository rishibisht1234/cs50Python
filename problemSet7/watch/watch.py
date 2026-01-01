import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'<iframe.*src="(https?://(?:www\.)?youtube\.com/embed/\w*)".*</iframe>',s):
        url=matches.group(1)
        new_url = re.sub(r'.*(www\.)?youtube.com/embed','https://youtu.be',url)
        return new_url
    return None

# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0

if __name__ == "__main__":
    main()
