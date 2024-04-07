
class Player:
    def __init__(self, name,
    score_solo, wins_solo, kd_solo, wr_solo, games_solo, kills_solo, mins_solo,
    score_duo, wins_duo, kd_duo, wr_duo, games_duo, kills_duo, mins_duo,
    score_trio, wins_trio, kd_trio, wr_trio, games_trio, kills_trio, mins_trio,
    score_squad, wins_squad, kd_squad, wr_squad, games_squad, kills_squad, mins_squad,
    score_ltm, wins_ltm, top3_ltm, kd_ltm, wr_ltm, games_ltm, kills_ltm, mins_ltm):

        self.name = name

        # Solo stats
        self.score_solo = score_solo
        self.wins_solo = wins_solo
        self.kd_solo = kd_solo
        self.wr_solo = wr_solo
        self.games_solo = games_solo
        self.kills_solo = kills_solo
        self.mins_solo = mins_solo

        # Duo stats
        self.score_duo = score_duo
        self.wins_duo = wins_duo
        self.kd_duo = kd_duo
        self.wr_duo = wr_duo
        self.games_duo = games_duo
        self.kills_duo = kills_duo
        self.mins_duo = mins_duo

        # Trio stats
        self.score_trio = score_trio
        self.wins_trio = wins_trio
        self.kd_trio = kd_trio
        self.wr_trio = wr_trio
        self.games_trio = games_trio
        self.kills_trio = kills_trio
        self.mins_trio = mins_trio

        # Squad stats
        self.score_squad = score_squad
        self.wins_squad = wins_squad
        self.kd_squad = kd_squad
        self.wr_squad = wr_squad
        self.games_squad = games_squad
        self.kills_squad = kills_squad
        self.mins_squad = mins_squad

        # LTM stats, includes top 3 placements
        self.score_ltm = score_ltm
        self.wins_ltm = wins_ltm
        self.top3_ltm = top3_ltm
        self.kd_ltm = kd_ltm
        self.wr_ltm = wr_ltm
        self.games_ltm = games_ltm
        self.kills_ltm = kills_ltm
        self.mins_ltm = mins_ltm


