def get_group_score(group):
    """Evaluates the list of similarities"""
    similarity_list = []

    i = 0

    while i < len(group): # <- correct solution
        j = i + 1 # <- correct solution
        while j < len(group): # <- correct solution
            # find the scaled distance
            scaled_distance = abs(group[i]['year'] - group[j]['year']) / 5.0 # <- correct solution

            # find the similarity
            similarity = 1 - scaled_distance

            # add to list
            similarity_list.append(similarity)

            j += 1
        i += 1

    return similarity_list


if __name__ == '__main__':
    group_1 = [{'name': 'Primya', 'year': 3},
    {'name': 'Zoe', 'year': 3},
    {'name': 'Francesco', 'year': 3},
    {'name': 'Yimin', 'year': 3}]

    group_2 = [{'name': 'Claire', 'year': 1},
    {'name': 'Kai', 'year': 1},
    {'name': 'Rohit', 'year': 2},
    {'name': 'Alain', 'year': 2}]

    group_3 = [{'name': 'Mohammed', 'year': 4},
    {'name': 'Xiaoyuan', 'year': 5},
    {'name': 'Grace', 'year': 5}]


    list_1 =  get_group_score(group_1)
    print(list_1)

    list_2 =  get_group_score(group_2)
    print(list_2)

    list_3 =  get_group_score(group_3)
    print(list_3)

