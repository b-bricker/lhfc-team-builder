def switch_div(div):
    print(div)
    if div == '6U':
        return [4, 6]
    elif div == '8U':
        return [6, 10]
    elif div == '10U':
        return [7, 12]
    elif div == '12U':
        return [7, 12]
    elif div == '14U':
        return [7, 12]

def divide_division(players, division):
    num_players = len(players)
    [min_size, target_size] = switch_div(division)
    
    if num_players < min_size:
        print(f"Not enough players to form a team, have {num_players} but need {min_size}")
        return []
    
    num_teams = max(int(num_players / target_size), 1)

    if num_teams == 1:
        return [players]
    
    teams = {}
    for i in range(num_teams):
        teams[str(i)] = []
    
    index = 0
    for player in players:
        teams[str(index)].append(player)
        if index == num_teams - 1:
            index = 0
        else:
            index += 1

    result = []
    for team in teams:
        result.append(teams[team])

    return result
