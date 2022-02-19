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

#1
# def mov(a):
#     for i in a:
#         if i["imdb"]>5.5:
#             return True
# print(mov(movies))

#2
# def mov(a):
#     list=[]
#     for i in a:
#         if i["imdb"]>5.5:
#             list.append(i["name"])
#     return list
# print(mov(movies))

#3
# name=input()
# def mov(a,b):
#     list=[]
#     for i in a:
#         if i["category"]==b:
#             list.append(i["name"])
#     return list
# print(mov(movies,name))

#4
# def mov(a):
#     sum=0
#     for i in a:
#         sum+=i["imdb"]
#     return sum/len(a)
# print(mov(movies))

#5
# name=input()
# def mov(a,b):
#     sum=0
#     count=0
#     for i in a:
#         if i["category"]==b:
#             sum+=i["imdb"]
#             count+=1
#     return sum/count
# print(mov(movies,name))

