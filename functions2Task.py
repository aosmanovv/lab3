movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]
def rate(m):
    if (m["imdb"]>5.5):
        return True
    else:
        return False
def best_list(l):
    new_l=[]
    for i in movies:
        #print(rate(i))
        if rate(i)==True:
            new_l.append(i)
    return new_l

def categoryFilter(l):
    c=input()
    new_l=[]
    for i in l:
        if (i["category"]==c):
            new_l.append(i)
    return new_l

def avRate(l):
    av=0
    for i in l:
        av+=i["imdb"]
    av/=len(l)
    return av

def catAvRate(l):
    new_l=categoryFilter()
    return avRate(new_l)

print(rate(movies[0]))
print(best_list(movies))
print(categoryFilter(movies))
print(avRate(movies))