def sol(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()

        if cacheSize:
            if not city in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                answer += 5
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
        else:
            answer += 5
    return answer