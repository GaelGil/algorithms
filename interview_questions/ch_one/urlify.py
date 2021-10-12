sample_string = 'this is a spaced string'

def urlify(sample_string:str):
    return "%20".join(sample_string.split())

print(urlify(sample_string))