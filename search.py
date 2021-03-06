import re


def get_tag(tag):
    search_tag = re.search(r'^([a-zA-Z]+)?(\d+)?$', tag)
    return search_tag.group(1, 2)


def is_alone(x):
    prefix, n = x
    return not prefix


def get_code(code):
    parts = code.split('-')
    result = []
    previous_tag = (None, None)
    for part in parts:
        tag = get_tag(part)
        if is_alone(tag):
            tag = (previous_tag[0], tag[1])
        result.append(tag)
        previous_tag = tag
    return result


def item_title_to_search_tags_set(title):
    return set([x.strip().lower() for x in title.split(' ') if len(x) > 3])


def get_item_search_tags(item):
    alias = item['alias']
    title = item_title_to_search_tags_set(item['title'])
    code = get_tag_set(get_code(item['code']))
    return {alias} | title | code


def get_tag_set(code):
    result = set()
    for tag in code:
        result.add(tag[0])
        if tag[1]:
            result.add(tag[0] + tag[1])
    return result


if __name__ == '__main__':
    import requests
    res = requests.get('https://raw.githubusercontent.com/designunit/dc-data/master/data.json')
    data = res.json()
    codes = [list(get_item_search_tags(x)) for x in data]
    tags = sorted(set(sum(codes, [])))

    for x in tags:
        print(x)
