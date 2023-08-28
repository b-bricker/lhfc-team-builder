from datetime import datetime


def calculate_age(birth_date, cutoff_date):
        date_format = '%m/%d/%Y'
        birth = datetime.strptime(birth_date, date_format)
        end = datetime.strptime(cutoff_date, date_format)
        diff = end - birth
        rounded_diff_years = round(diff.days/365, 2)
        return rounded_diff_years

def sort_division(players, division):
    division_players = list(filter(lambda x: x['Division'] == division, players))
    division_players.sort(key=lambda x: x['age'], reverse=True)

    girls = list(filter(lambda x: x['Gender'] == 'Female', division_players))
    boys = list(filter(lambda x: x['Gender'] == 'Male', division_players))
    division_players = girls + boys
    return division_players

def sort_players(players, cutoff):
    for player in players:
        player['age'] = calculate_age(player['Date of Birth'], cutoff)

    return {
         '6U': sort_division(players, 'Under Age 6'),
         '8U': sort_division(players, 'Under Age 8'),
         '10U': sort_division(players, 'Under Age 10'),
         '12U': sort_division(players, 'Under Age 12'),
         '14U': sort_division(players, 'Under Age 14')
    }