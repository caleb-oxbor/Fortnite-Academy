
class Player:
    def __init__(self, name,
    score_solo, wins_solo, kd_solo, wr_solo, games_solo, kills_solo, mins_solo,
    score_duo, wins_duo, kd_duo, wr_duo, games_duo, kills_duo, mins_duo,
    score_trio, wins_trio, kd_trio, wr_trio, games_trio, kills_trio, mins_trio,
    score_squad, wins_squad, kd_squad, wr_squad, games_squad, kills_squad, mins_squad,
    score_ltm, wins_ltm, top3_ltm, kd_ltm, wr_ltm, games_ltm, kills_ltm, mins_ltm):

        self.name = name

        # Solo stats
        self.score_solo = int(score_solo)
        self.wins_solo = int(wins_solo)
        self.kd_solo = float(kd_solo)
        self.wr_solo = float(wr_solo)
        self.games_solo = int(games_solo)
        self.kills_solo = int(kills_solo)
        self.mins_solo = int(mins_solo)

        # Duo stats
        self.score_duo = int(score_duo)
        self.wins_duo = int(wins_duo)
        self.kd_duo = float(kd_duo)
        self.wr_duo = float(wr_duo)
        self.games_duo = int(games_duo)
        self.kills_duo = int(kills_duo)
        self.mins_duo = int(mins_duo)

        # Trio stats
        self.score_trio = int(score_trio)
        self.wins_trio = int(wins_trio)
        self.kd_trio = float(kd_trio)
        self.wr_trio = float(wr_trio)
        self.games_trio = int(games_trio)
        self.kills_trio = int(kills_trio)
        self.mins_trio = int(mins_trio)

        # Squad stats
        self.score_squad = int(score_squad)
        self.wins_squad = int(wins_squad)
        self.kd_squad = float(kd_squad)
        self.wr_squad = float(wr_squad)
        self.games_squad = int(games_squad)
        self.kills_squad = int(kills_squad)
        self.mins_squad = int(mins_squad)

        # LTM stats, includes top 3 placements
        self.score_ltm = int(score_ltm)
        self.wins_ltm = int(wins_ltm)
        self.top3_ltm = int(top3_ltm)
        self.kd_ltm = float(kd_ltm)
        self.wr_ltm = float(wr_ltm)
        self.games_ltm = int(games_ltm)
        self.kills_ltm = int(kills_ltm)
        self.mins_ltm = int(mins_ltm)


