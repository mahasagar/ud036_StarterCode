import media
import fresh_tomatoes
avengers = media.Movie('Avengers: Endgame',
"https://image.tmdb.org/t/p/w600_and_h900_bestv2/or06FN3Dka5tukK1e9sl16pB3iy.jpg",
"https://www.youtube.com/watch?v=TcMBFSGVi1c");

#print(avengers.storyline);
#avengers.show_trailer();

mad_max = media.Movie('Mad Max',
"https://image.tmdb.org/t/p/w500/kqjL17yufvn9OVLyXYpvtyrFfak.jpg",
"https://youtu.be/akX3Is3qBpw");


avatar = media.Movie('Avatar',
"https://image.tmdb.org/t/p/w600_and_h900_bestv2/kmcqlZGaSh20zpTbuoF0Cdn07dT.jpg",
"https://youtu.be/5MB3Ea6L-gw");


zombieland = media.Movie('Zombieland',
"https://image.tmdb.org/t/p/w600_and_h900_bestv2/vUzzDpVrab1BOG3ogxhRGfLN94d.jpg",
"https://youtu.be/8m9EVP8X7N8");


infinity_war = media.Movie('Avengers: Infinity War',
"https://image.tmdb.org/t/p/w600_and_h900_bestv2/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg",
"https://youtu.be/6ZfuNTqbHE8");


movie_data = [avengers,infinity_war,zombieland,avatar,mad_max];
fresh_tomatoes.open_movies_page(movie_data);