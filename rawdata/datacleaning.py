# requires module "chess"
import chess.pgn

names = []


names_fin = []
win_fin = []
names_elo_fin = []
others_elo_fin = []
pair_names_fin = []
other_names_fin = []

num_players = 1000000000

count = 0

# replace with own directory
d = '/Users/kms299/Library/CloudStorage/OneDrive-YaleUniversity/classes/algo mind/final project/chess_final_proj'

# /lichess_db_standard_rated_2013-01.pgn is the smallest file
with open(d+'/lichess_db_standard_rated_2013-01.pgn') as pgn:
    while count < num_players:
        headers = chess.pgn.read_headers(pgn)
        if headers is None:
            break
        if headers.get("White") not in names:
            count +=1
            names.append(headers.get("White"))
   
   
count = 0
for name in names:
    name_wins = []
    name_elo = []
    others_elo =[]
    pair = []
    other_name=[]
    
    with open(d + '/lichess_db_standard_rated_2013-01.pgn') as pgn:
        while True:
            header = chess.pgn.read_headers(pgn)
            if header is None:
                break
            if name in header.get("White"):
                if header.get("Result") == '1-0':
                    name_wins.append(1)
                else:
                    name_wins.append(0)
                if header.get("WhiteElo") != '?' and header.get("BlackElo") != '?': 
                    self_elo = int(header.get("WhiteElo"))
                    other_elo = int(header.get("BlackElo")) 
                else:
                    self_elo = 9999
                    other_elo = 9999
                name_elo.append(self_elo)     
                others_elo.append(other_elo)
                pair.append(','.join([header.get("White"),header.get("Black")]))
                other_name.append(header.get("Black"))
            elif name in header.get("Black"):
                if header.get("Result") == '0-1':
                    name_wins.append(1)
                else:
                    name_wins.append(0)
                if header.get("WhiteElo") != '?' and header.get("BlackElo") != '?': 
                    self_elo = int(header.get("BlackElo"))
                    other_elo = int(header.get("WhiteElo")) 
                else:
                    self_elo = 9999
                    other_elo = 9999
                name_elo.append(self_elo)     
                others_elo.append(other_elo)
                pair.append(','.join([header.get("White"),header.get("Black")]))
                other_name.append(header.get("White"))
        if len(name_wins) > 100:
            names_fin.append(name)
            win_fin.append(name_wins)
            names_elo_fin.append(name_elo)
            others_elo_fin.append(others_elo)
            pair_names_fin.append(pair)
            other_names_fin.append(other_name)
            count+=1
            
            print('Done with player ('+  str(len(name_wins))+' games)')
        else:
            print('Done with player (not recorded, too few games: '+  str(len(name_wins))+')')
    
    
temp5 = []
for (i,num_player) in enumerate(pair_names_fin):
    n = names_fin[i]
    temp1 = []
    for game in num_player:
        temp2 = set(game)- set([names_fin[0]])
        temp1.append(str(temp2))
    temp5.append(temp1)
data = {
    'Name': names_fin,
    'Pair_names': pair_names_fin,
    'Other_name': other_names_fin,
    'Self_elo': names_elo_fin,
    'Other_elo': others_elo_fin,
    'Win': win_fin
}


dict_as_string = str(data)  # Using str() function

# Save the string representation to a file
with open(d + '/data_Jan2013.txt', 'w') as file:
    file.write(dict_as_string)
