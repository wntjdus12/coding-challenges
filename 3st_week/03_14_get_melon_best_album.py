# 멜론 베스트 앨범 뽑기

# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.
#   -> genre_array에서 genre별로 재생횟수를 모두 모아서 비교해준다. 그리고 가장 많이 재생된 장르 별로 노래를 2곡씩 넣어줄거다.
#    어떤 값이 올지 모름.
#    특정 키 값에 대해서 value를 모아서 합쳐주고 싶다.
#    특정 키값은 아직 정해지지 않았다.
#    dict = {}


#     0            1       2           3         4
#    ["classic", "pop", "classic", "classic", "pop"]
#    [500, 600, 150, 800, 2500]

#    0 
#    -> dict = {"classic": 500}
#    -> dict2 = {"classic": [(0, 500)]}

#    1
#    -> dict = {"classic": 500, "pop": 600}
#    -> dict2 = {"classic": [(0, 500)], "pop": [(1, 600)]}
   
#    2
#    -> dict = {"classic": 500 + 150 , "pop": 600}
#    -> dict2 = {"classic": [(0, 500), (2, 150)], "pop": [(1, 600)]}

#    3
#    -> dict = {"classic": 500 + 150 + 800 , "pop": 600}
#    -> dict2 = {"classic": [(0, 500), (2, 150), (3, 800)], "pop": [(1, 600)]}

#    4
#    -> dict = {"classic": 500 + 150 + 800 , "pop": 600 + 2500}
#    -> dict2 = {"classic": [(0, 500), (2, 150), (3, 800)], "pop": [(1, 600), (4, 2500)]}

#    -> 가장 많이 재생된 장르들을 순서대로 알려주세요. ["pop", "classic"]
   
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
#   -> 많이 재생된 장르별로 2곡을 넣어줄 때, 많이 재생된 노래 먼저 넣어줘야 한다.

# 3. 장르 내에서 재생횟수가 같다면, 고유 번호가 낮은, 즉 인덱스가 낮은 노래 먼저 수록해줘야 한다. 


# => 많이 라는 단어가 많이 나온다면 정렬을 써야하는구나 라고 생각할 수 있다. 

def get_melon_best_album(genre_array, play_array):
    # 1. dict에 장르별로 얼마나 재생횟수를 가지고 있는지 나타내는 딕셔너리
    # 2. dict에 장르별로 어느 인덱스에 몇번 재생횟수를 가지고 있는가를 나타내는 딕셔너리

    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}

    for i in range(n):
        genre = genre_array[i] #classic
        play = play_array[i] # 500

        if genre in genre_total_play_dict: #classic 이라는 키값이 있었으면
            genre_total_play_dict[genre] += play #재생횟수를 더해줘야 할테니까요
            genre_index_play_array_dict[genre].append([i, play])
        else: #키 값이 없는 상황이라면
            genre_total_play_dict[genre] = play  #500
            genre_index_play_array_dict[genre] = [[i, play]]

    # 장르별로 가장 재생횟수가 많은 장르들 중, 곡수가 많은 순서대로 2개씩 출력하기
    print(genre_total_play_dict.items())

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item:item[1], reverse=True)

    result = []
    for genre, total_play in sorted_genre_play_array:
        print(genre, total_play)
        print("genre_index_play_array_dict[genre] is ", genre_index_play_array_dict[genre])
        sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda item:item[1], reverse=True)

        print("sorted_genre_index_play_array is", sorted_genre_index_play_array)

        # 장르별로 제일 잘 나가는 2곡만 넣어라.
        genre_song_count = 0
        for index, play in sorted_genre_index_play_array:
            print("index", index, "play", play)
            if genre_song_count >= 2:
                break
            result.append(index)
            genre_song_count += 1

    return result
# print(sorted([123],key=lambda item:item[1], reverse=True)) -> sorted란 함수는 특정 배열 값을 입력받아서 정렬해 줄 수 있게 만드는 함수, reverse=True를 하면 내림차순으로 정렬
# 람다 함수 : 어떤 것으로 정렬할지 결정할 수 있게 해주는 방법  


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))