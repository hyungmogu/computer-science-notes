def get_group_score(group):
    """Evaluates the group score

        Precondition: len(group) == 4
    """
    n = 4

    max_year = get_max_year(group)
    min_year = get_min_year(group)
    similarity_list = []

    i = 0

    while i < 4:
        j = 0
        while j < 4:
            # find the scaled distance
            scaled_distance = 0
            if max_year != min_year:
                scaled_distance = abs(group[i]['year'] - group[j]['year']) / float(max_year - min_year)

            # find the similarity
            similarity = 1 - scaled_distance

            # add to list
            similarity_list.append(similarity)

            j += 1
        i += 1

    # find the average
    average = float(sum(similarity_list))/len(similarity_list)
    return average.as_integer_ratio()

def get_max_year(group):
    """returns max value of year in group"""

    max_value = -1

    for student in group:
        max_value = max(student['year'], max_value)

    return max_value

def get_min_year(group):
    """returns min value of year in group"""

    min_value = 100 # this is impossible value

    for student in group:
        min_value = min(student['year'], min_value)

    return min_value


if __name__ == '__main__':
    group_1 = [{'name': 'Primya', 'year': 3},
    {'name': 'Zoe', 'year': 3},
    {'name': 'Francesco', 'year': 3},
    {'name': 'Yimin', 'year': 3}]

    group_2 = [{'name': 'Primya', 'year': 1},
    {'name': 'Zoe', 'year': 1},
    {'name': 'Francesco', 'year': 2},
    {'name': 'Yimin', 'year': 2}]

    group_3 = [{'name': 'Primya', 'year': 5},
    {'name': 'Zoe', 'year': 5},
    {'name': 'Francesco', 'year': 4},
    {'name': 'Yimin', 'year': 3}]


    score_1 =  get_group_score(group_1)
    print(score_1)

    score_2 =  get_group_score(group_2)
    print(score_2)

    score_3 =  get_group_score(group_3)
    print(score_3)

