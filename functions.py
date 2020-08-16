def bust_check(entity):
    while entity.hand_value > 21 and entity.ace_count:
        
        entity.hand_value -= 10
        entity.ace_count -= 1

    return entity.hand_value > 21
