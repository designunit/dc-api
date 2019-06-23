import search

def get_common_tags(items):
    def tags(item):
        tags = search.get_code(item['code'])
        return [x[0] for x in tags]

    xs = [tags(x) for x in items]
    xs = sum(xs, [])
    return list(set(xs))
