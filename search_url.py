"""Script to get url for search based on user input from user
"""

base_url = "https://www.amazon.in/s/field-keywords="

def get_search_url(keyword):
    """(str) -> str
    """
    parsed_keyword = keyword.replace(" ", '+')
    print base_url+parsed_keyword
    return base_url+parsed_keyword


if __name__ == '__main__':
    keyword = raw_input("Enter the keyword\n")
    print get_search_url(str(keyword))
