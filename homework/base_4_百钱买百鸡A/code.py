for cock in range(1,20):
    for hen in range(1, 33):
        if (100 - cock - hen) % 3 == 0 and cock * 5 + hen * 3 + (100 - cock - hen) / 3 == 100:
            print(cock, hen, 100-cock-hen)
# 一条语句实现
# [print(*i) for i in [[cock,hen,100-cock-hen] for cock in range(1,20) for hen in range(1,33) if (100-cock-hen)%3==0 and cock*5+hen*3+(100-cock-hen)/3==100]]