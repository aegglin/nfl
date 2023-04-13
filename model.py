from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table, Date, Time, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Conference(Base):
    __tablename__ = 'Conferences'
    __table_args__ = {'schema': 'Dim'}
    ConferenceId = Column(Integer(), primary_key=True)
    Conference = Column(String(3), nullable=False, unique=True)

    def __init__(self, data):
        data = data or {}
        self.ConferenceId = data.get('ConferenceId')
        self.Conference = data.get('Conference')

    def __repr__(self):
        return f"ConferenceId={self.ConferenceId} Conference={self.Conference}"
    
class Division(Base):
    __tablename__ = 'Divisions'
    __table_args__ = {'schema': 'Dim'}

    DivisionId = Column(Integer(), primary_key=True)
    Division = Column(String(5), nullable = False)
    ConferenceId = Column(Integer(), ForeignKey('Conferences.ConferenceId'))

    def __init__(self, data):
        data = data or {}
        self.DivisionId = data.get('DivisionId')
        self.Division = data.get('Division')
        self.ConferenceId = data.get('ConferenceId')

    def __repr__(self):
        return f"DivisionId={self.DivisionId} Division={self.Division} ConferenceId={self.ConferenceId}"


class Season(Base):
    __tablename__ = 'Seasons'
    __table_args__ = {'schema':'Dim'}
    SeasonId = Column(Integer(), primary_key=True)
    StartYear = Column(Integer(), nullable=False)
    EndYear = Column(Integer(), nullable=False)

    def __init__(self, data):
        data = data or {}
        self.SeasonId = data.get('SeasonId')
        self.StartYear = data.get('StartYear')
        self.EndYear = data.get('EndYear')

    def __repr__(self):
        return f"SeasonId={self.SeasonId} StartYear={self.StartYear} EndYear={self.EndYear}"


class Team(Base):
    __tablename__ = 'Teams'
    _table_args = {'schema':'Dim'}
    TeamId = Column(Integer(), primary_key=True)
    CityName = Column(String(200), nullable=False, unique=True)
    ConferenceId = Column(Integer(), ForeignKey('Conferences.ConferenceId'))
    Nickname = Column(String(200), nullable=False)

    def __init__(self, data):
        data = data or {}
        self.TeamId = data.get('TeamId')
        self.CityName = data.get('CityName')
        self.ConferenceId = data.get('ConferenceId')
        self.Nickname = data.get('Nickname')

    def __repr__(self):
        return f"TeamId={self.TeamId} CityName={self.CityName} ConferenceId={self.ConferenceId} Nickname={self.Nickname}"
    
class Game(Base):
    __tablename__ = 'Games'
    _table_args__ = {'schema':'Fact'}
    GameId = Column(Integer(), primary_key=True)
    SeasonId = Column(Integer(), ForeignKey('Seasons.SeasonId'))
    GameType = Column(String(3), nullable=False)
    Week = Column(Integer(), nullable=False)
    GameDate = Column(Date(), nullable=False)
    GameTime = Column(Time(), nullable=False)
    Weekday = Column(String(9), nullable=False)
    HomeScore = Column(Integer(), nullable=False)
    AwayScore = Column(Integer(), nullable=False)
    HomeTeamId = Column(Integer(), ForeignKey('Teams.TeamId'))
    AwayTeamId = Column(Integer(), ForeignKey('Teams.TeamId'))
    Location = Column(String(9), nullable=False)
    Overtime = Column(Boolean(), nullable=False)
    DivGame = Column(Boolean(), nullable=False)
    Roof = Column(String(8), nullable=False)
    Surface = Column(String(10), nullable=False)
    Temp = Column(Integer(), nullable=True)
    Wind = Column(Integer(), nullable=True)

    def __repr__(self):
        return f"GameId={self.GameId} SeasonId={self.SeasonId} GameType={self.GameType} Week={self.Week} \
            GameDate={self.GameDate} GameTime={self.GameTime} Weekday={self.Weekday} HomeScore={self.HomeScore} AwayScore={self.AwayScore} \
            HomeTeamId={self.HomeTeamId} AwayTeamId={self.AwayTeamId} Location={self.Location} Overtime={self.Overtime} DivGame={self.DivGame} \
            Roof={self.Roof} Surface={self.Surface} Temp={self.Temp} Wind={self.Wind}"
    
class Odds(Base):
    __tablename__ = 'Odds'
    OddsId = Column(Integer(), primary_key=True)
    GameId = Column(Integer(), ForeignKey('Games.Id'))
    HomeMoneyLine = Column(Integer(), nullable=False)
    AwayMoneyLine = Column(Integer(), nullable=False)
    HomeSpreadOdds = Column(Integer(), nullable=False)
    AwaySpreadOdds = Column(Integer(), nullable=False)
    SpreadLine = Column(Float(), nullable=False)
    TotalLine = Column(Float(), nullable=False)
    OverOdds = Column(Integer(), nullable=False)
    UnderOdds = Column(Integer(), nullable=False)

    def __repr__(self):
        return f"OddsId={self.OddsId} GameId={self.GameId} HomeMoneyLine={self.HomeMoneyLine} AwayMoneyLine={self.AwayMoneyLine} \
            HomeSpreadOdds={self.HomeSpreadOdds} AwaySpreadOdds={self.AwaySpreadOdds} SpreadLine={self.SpreadLine} \
            TotalLine={self.TotalLine} OverOdds={self.OverOdds} UnderOdds={self.UnderOdds}"
    
class Players(Base):
    __tablename__ = 'Players'
    PlayerId = Column(String(), primary_key=True)
    PlayerName = Column(String(), nullable=False)
    FirstName = Column(String(), nullable=False)
    LastName = Column(String(), nullable=False)
    TeamId = Column(Integer(), ForeignKey('Teams.TeamId'))

    def __repr__(self):
        return f"PlayerId={self.PlayerId} PlayerName={self.PlayerName} FirstName={self.FirstName} LastName={self.LastName} TeamId={self.TeamId}"
    
class Stats(Base):
    __tablename__ = 'Stats'
    StatId = Column(Integer(), primary_key=True)
    PlayerId = Column(Integer(), ForeignKey('Players.PlayerId'))
    SeasonId = Column(Integer(), ForeignKey('Seasons.SeasonId'))
    GameId = Column(Integer(), ForeignKey('Games.GameId'))
    Carries = Column(Integer(), nullable=False)
    Receptions = Column(Integer(), nullable=False)
    Touches = Column(Integer(), nullable=False)
    Yards = Column(Integer(), nullable=False)
    Touchdowns = Column(Integer(), nullable=False)
    Completions = Column(Integer(), nullable=False)
    PassingYards = Column(Integer(), nullable=False)
    PassingTouchdowns = Column(Integer(), nullable=False)
    Interceptions = Column(Integer(), nullable=False)
    PassingTwoPointConversions = Column(Integer(), nullable=False)
    SpecialTeamsTouchdowns = Column(Integer(), nullable=False)
    TwoPointConversions = Column(Integer(), nullable=False)
    Fumbles = Column(Integer(), nullable=False)

    def __repr__(self):
        return f"StatId={self.StatId} PlayerId={self.PlayerId} SeasonId={self.SeasonId} GameId={self.GameId} Carries={self.Carries} \
            Receptions={self.Receptions} Touches={self.Touches} Yards={self.Yards} Touchdowns={self.Touchdowns} Completions={self.Completions} \
            PassingYards={self.PassingYards} PassingTouchdowns={self.PassingTouchdowns} Interceptions={self.Interceptions} \
            PassingTwoPointConversions={self.PassingTwoPointConversions} SpecialTeamsTouchdowns={self.SpecialTeamsTouchdowns} TwoPointConversions={self.TwoPointConversions} \
            Fumbles={self.Fumbles}"
