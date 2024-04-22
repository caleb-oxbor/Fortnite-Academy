
class Player:
    def __init__(self, name,
    score_solo, wins_solo, kd_solo, wr_solo, games_solo, kills_solo, mins_solo,
    score_duo, wins_duo, kd_duo, wr_duo, games_duo, kills_duo, mins_duo,
    score_trio, wins_trio, kd_trio, wr_trio, games_trio, kills_trio, mins_trio,
    score_squad, wins_squad, kd_squad, wr_squad, games_squad, kills_squad, mins_squad,
    score_ltm, wins_ltm, top3_ltm, kd_ltm, wr_ltm, games_ltm, kills_ltm, mins_ltm):

        self.name = name

        self.kd = []
        self.wr = []
        self.mins = []

        # Solo stats
        self.score_solo = int(score_solo)
        self.wins_solo = int(wins_solo)
        self.kd.append(float(kd_solo))
        self.wr.append(float(wr_solo))
        self.games_solo = int(games_solo)
        self.kills_solo = int(kills_solo)
        self.mins.append(mins_solo)

        # Duo stats
        self.score_duo = int(score_duo)
        self.wins_duo = int(wins_duo)
        self.kd.append(float(kd_duo))
        self.wr.append(float(wr_duo))
        self.games_duo = int(games_duo)
        self.kills_duo = int(kills_duo)
        self.mins.append(mins_duo)

        # Trio stats
        self.score_trio = int(score_trio)
        self.wins_trio = int(wins_trio)
        self.kd.append(float(kd_trio))
        self.wr.append(float(wr_trio))
        self.games_trio = int(games_trio)
        self.kills_trio = int(kills_trio)
        self.mins.append(int(mins_trio))

        # Squad stats
        self.score_squad = int(score_squad)
        self.wins_squad = int(wins_squad)
        self.kd.append(float(kd_squad))
        self.wr.append(float(wr_squad))
        self.games_squad = int(games_squad)
        self.kills_squad = int(kills_squad)
        self.mins.append(int(mins_squad))

        # LTM stats, includes top 3 placements
        self.score_ltm = int(score_ltm)
        self.wins_ltm = int(wins_ltm)
        self.top3_ltm = int(top3_ltm)
        self.kd.append(float(kd_ltm))
        self.wr.append(float(wr_ltm))
        self.games_ltm = int(games_ltm)
        self.kills_ltm = int(kills_ltm)
        self.mins.append(int(mins_ltm))
