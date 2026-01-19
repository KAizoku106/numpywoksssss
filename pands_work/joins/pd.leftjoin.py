movies_data = [
    {"id": 1, "title": "ARM", "language": "Malayalam", "year": 2024},
    {"id": 2, "title": "Kalki 2898 AD", "language": "Telugu", "year": 2024},
    {"id": 3, "title": "Dune: Part Two", "language": "English", "year": 2024},
    {"id": 4, "title": "Manjummel Boys", "language": "Malayalam", "year": 2024},
    {"id": 5, "title": "Stree 2", "language": "Hindi", "year": 2024},
    {"id": 6, "title": "Toxic", "language": "Kannada", "year": 2025},
    {"id": 7, "title": "The Greatest of All Time", "language": "Tamil", "year": 2024}
]

reviews_data = [
    {"id": 1, "movie_id": 1, "message": "Must watch! Tovino's performance is top-notch.", "rating": 4.5, "owner": "vipin"},
    {"id": 2, "movie_id": 2, "message": "Visual spectacle, but the first half was a bit slow.", "rating": 4.0, "owner": "rahul_k"},
    {"id": 3, "movie_id": 3, "message": "A cinematic masterpiece. The sound design is incredible.", "rating": 5.0, "owner": "cinephile_99"},
    {"id": 4, "movie_id": 4, "message": "Heart-wrenching and beautifully shot. A survival gem.", "rating": 4.8, "owner": "amal_p"},
    {"id": 5, "movie_id": 5, "message": "Hilarious! Perfect sequel to the first one.", "rating": 4.2, "owner": "priya_sharma"},
    {"id": 6, "movie_id": 1, "message": "The 3D effects were actually good for a change.", "rating": 4.0, "owner": "deepu_v"},
    {"id": 7, "movie_id": 7, "message": "Pure fan service, but enjoyed the action sequences.", "rating": 3.5, "owner": "vijay_fan_boy"},
    {"id": 8, "movie_id": 2, "message": "Concept was great, but felt overstretched at 3 hours.", "rating": 3.0, "owner": "anita_review"},
    {"id": 9, "movie_id": 4, "message": "The background score gave me goosebumps.", "rating": 5.0, "owner": "karthik_007"},
    {"id": 10, "movie_id": 7, "message": "The teaser looks promising, can't wait for Yash!", "rating": 4.5, "owner": "yash_army"},
    {"id": 11, "movie_id": 3, "message": "Too long for my taste, though visuals were stunning.", "rating": 3.5, "owner": "mark_robert"},
    {"id": 12, "movie_id": 1, "message": "Storytelling at its best. Malayalam cinema is peaked.", "rating": 4.7, "owner": "sree_mallu"},
    {"id": 13, "movie_id": 5, "message": "Some jokes felt repetitive, but the climax saved it.", "rating": 3.8, "owner": "rohit_verma"},
    {"id": 14, "movie_id": 7, "message": "Average plot, but the music was catchy.", "rating": 3.0, "owner": "sneha_j"},
    {"id": 15, "movie_id": 1, "message": "A bit overhyped but still a solid entertainer.", "rating": 3.5, "owner": "faisal_khan"},
    {"id": 16, "movie_id": 2, "message": "Prabhas is back with a bang! Epic visuals.", "rating": 4.5, "owner": "telugu_talkies"},
    {"id": 17, "movie_id": 4, "message": "The emotion in this movie is so real. I cried.", "rating": 5.0, "owner": "meera_nair"},
    {"id": 18, "movie_id": 3, "message": "Hans Zimmer score is the soul of this film.", "rating": 5.0, "owner": "music_buff"},
    {"id": 19, "movie_id": 7, "message": "The wait for 2025 is going to be long.", "rating": 4.0, "owner": "rockybhai_fan"},
    {"id": 20, "movie_id": 1, "message": "Incredible production quality for a regional film.", "rating": 4.2, "owner": "arjun_v"},
    {"id": 21, "movie_id": 2, "message": "Amitabh Bachchan stole the show as Ashwatthama.", "rating": 4.8, "owner": "bollywood_lover"},
    {"id": 22, "movie_id": 5, "message": "Shraddha and Rajkumar Rao chemistry is gold.", "rating": 4.5, "owner": "desi_critic"},
    {"id": 23, "movie_id": 7, "message": "The de-aging tech was hit and miss for me.", "rating": 2.5, "owner": "tech_guru"},
 
]

import pandas as pd

movies= pd.DataFrame(movies_data)
reviews= pd.DataFrame(reviews_data)

data= pd.merge(movies,reviews,left_on="id",right_on="movie_id",how="left")

print(data)
