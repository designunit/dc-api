import aiohttp
from functools import reduce
from sanic import Sanic
from sanic.response import json
from sanic_cors import cross_origin
import api
import search
from lib import get_common_tags

app = Sanic()


def tag_factory(x):
    if not x[1]:
        return x[0]
    return x[0] + x[1]


def item_factory(item):
    # code = search.get_code(item['code'])
    # tags = [tag_factory(x) for x in code]
    tags = list(
        search.get_item_search_tags(item)
    )
    return {
        **item,
        'tags': tags,
    }


@app.route('/search/tags')
@cross_origin(app)
async def get_search_tags(request):
    data = await api.get_data()
    tags = [search.get_item_search_tags(x) for x in data]
    tags = reduce(lambda tags, x: tags | x, tags, set())
    tags = sorted(tags)

    return json({
        'data': tags,
    })


@app.route('/items')
@cross_origin(app)
async def get_items(request):
    data = await api.get_data()
    data = [item_factory(x) for x in data]

    return json({
        'data': data,
    })


@app.route('/tags/<tag>/children')
@cross_origin(app)
async def get_tag_children(request, tag):
    tag = tag.lower()
    data = await api.get_data()

    items = []
    for item in data:
        tags = search.get_code(item['code'])
        if tags[0][0].lower() == tag:
            items.append(item)

    children = get_common_tags(items)
    children = [x for x in children if x.lower() != tag]

    return json({
        'data': children,
    })


if __name__ == '__main__':
    import os
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
