#movies__details = {movies name:{"hero":deep,"herioine":21,""}} 

movies_details = {}

for i in range(1,6):
    movie_name = input("enter movie name : ")

    m_name = {}

    hero = input("enter hero name : ")
    heroine = input("enter heroine name :")

    #m_name["movie name"] = movie_name
    m_name["hero"] = hero 
    m_name["heroine"] = heroine 

    movies_details[movie_name] = m_name 


print(movies_details)


# For handling key collision 

for i in range(1,6):
    movie_name = input("enter movie name : ")
    m_name = {}
    if movie_name not in movies_details:

        hero = input("enter hero name : ")
        heroine = input("enter heroine name :")

        #m_name["movie name"] = movie_name
        m_name["hero"] = hero 
        m_name["heroine"] = heroine 

        movies_details[movie_name] = m_name 


print(movies_details)