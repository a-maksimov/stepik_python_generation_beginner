def build_query_string(params):
    url = ''
    sorted_params = sorted(params.keys())
    for param in sorted_params:
        url += param + '=' + str(params.get(param)) + '&'
    return url.strip('&')


print(build_query_string({'name': 'timur', 'age': 28}))
