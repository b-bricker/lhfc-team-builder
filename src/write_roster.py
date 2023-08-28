
def write_roster(full_roster_dict, output_file):
    with open(output_file, 'w') as f:
        f.write('Roster\n')
        for division in full_roster_dict:
            f.write(f"  {division}\n")
            for team in full_roster_dict[division]:
                mean_age = sum(player['age'] for player in team) / len(team)
                num_girls = len(list(filter(lambda x: x['Gender'] == 'Female', team)))
                num_boys = len(list(filter(lambda x: x['Gender'] == 'Male', team)))
                f.write(f"    NEW TEAM || Mean Age: {mean_age} || Girls/Boys: {num_girls}/{num_boys}\n")
                for player in team:
                    f.write(f"      Player: {player['First Name']} {player['Last Name']} || Age: {player['age']} || Gender: {player['Gender']}\n")


