def get_melon_best_album(genre_array, play_array):
    #1. dict에 장르별로 얼마나 재생횟수를 가지고있는지 나타내는 딕셔너리
    #2. dict에 장르별로 어느 인덱스에 몇번 재생횟수를 가지고 있는가를 나타내는 딕셔너리
    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}

    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]

        if genre in genre_total_play_dict:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])
        else:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]

    

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item:item[1], reverse=True)
    print(sorted_genre_play_array)

    result= []
    for genre, total_play in sorted_genre_play_array:
        print(genre, total_play)
        print("genre_index_play_array_dict[genre] is ", genre_index_play_array_dict[genre])
        sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda item:item[1], reverse=True)

        print("sorted_genre_index_play_array is", sorted_genre_index_play_array)

        genre_song_count = 0
        for index, play in sorted_genre_index_play_array:
            print("index", index, "play",play )
            if genre_song_count >= 2:
                break
            result.append(index)
            genre_song_count += 1

    return result
            


    

print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))