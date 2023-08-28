from read_roster import read_roster
from arg_parser import arg_parser
from sort_players import sort_players
from divide_division import divide_division
from write_roster import write_roster

[input_file, cutoff, output_file] = arg_parser()

players = read_roster(input_file)

sorted_players = sort_players(players, cutoff)

for div in sorted_players:
    sorted_players[div] = divide_division(sorted_players[div], div)

write_roster(sorted_players, output_file)
    