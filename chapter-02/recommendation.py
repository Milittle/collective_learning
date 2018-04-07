
from math import sqrt
from math import pow

critics = \
    {   'Lisa Rose': 
        {   'Lady in the Water': 2.5, 
            'Snakes on a Plane': 3.5, 
            'Just My Luck': 3.,
            'Superman Return': 3.5, 
            'You, Me and Dupree': 2.5, 
            'The Night Listener': 3.
        },
        'Gene Seymour':
        {   'Lady in the Water': 3., 
            'Snakes on a Plane': 3.5, 
            'Just My Luck': 1.5,
            'Superman Return': 5., 
            'You, Me and Dupree': 3.5, 
            'The Night Listener': 3.
        },
        'Michael Phillips':
        {   'Lady in the Water': 2.5,
            'Snakes on a Plane': 3.,
            'Superman Return': 3.5,
            'The Night Listener': 4.
        },
        'Claudia Puig':
        {   'Snakes on a Plane': 3.5, 
            'Just My Luck': 3.,
            'Superman Return': 4., 
            'You, Me and Dupree': 2.5, 
            'The Night Listener': 4.5
        },
        'Mick LaSalle':
        {   'Lady in the Water': 3., 
            'Snakes on a Plane': 4., 
            'Just My Luck': 2.,
            'Superman Return': 3., 
            'You, Me and Dupree': 2., 
            'The Night Listener': 3.
        },
        'Jack Matthews':
        {   'Lady in the Water': 3., 
            'Snakes on a Plane': 4., 
            'The Night Listener': 3.,
            'Superman Return': 5.,
            'You, Me and Dupree': 3.5, 
        },
        'Toby':
        {   'Snakes on a Plane': 4.5, 
            'You, Me and Dupree': 1., 
            'Superman Return': 4.
        }
    }


# 计算两个人之间评论过的电影的欧氏距离
def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0:
        return 0
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]])
    return 1 / (1. + sqrt(sum_of_squares))


# 计算p1 和 p2的皮尔逊系数
def sim_person(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    n = len(si)
    if n == 0:
        return 1.

    sum1 = sum([prefs[p1][item] for item in si])
    sum2 = sum([prefs[p2][item] for item in si])

    sumq1 = sum([pow(prefs[p1][item], 2.) for item in si])
    sumq2 = sum([pow(prefs[p2][item], 2.) for item in si])

    p_sum = sum([prefs[p1][item] * prefs[p2][item] for item in si])

    num = p_sum - (sum1 * sum2) / n

    den = sqrt((sumq1 - pow(sum1, 2.) / n) * (sumq2 - pow(sum2, 2.) / n))

    if den == 0:
        return 0
    return num / den

if __name__ == '__main__':
    print('the distance is {dis}'.format(dis = sim_distance(critics, 'Lisa Rose', 'Gene Seymour')))
