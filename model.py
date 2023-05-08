from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    ForeignKey,
    Table,
    Date,
    Time,
    Boolean,
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# TODO: database connection + session


class Conference(Base):
    __tablename__ = "Conferences"
    __table_args__ = {"schema": "Dim"}
    ConferenceId = Column(Integer(), primary_key=True)
    Conference = Column(String(3), nullable=False, unique=True)

    divisions = relationship(
        "Divisions"
    )  # If another table has this table as the foreign key, add a relationship to the parent
    teams = relationship("Teams")

    def __init__(self, data):
        data = data or {}
        self.ConferenceId = data.get("ConferenceId")
        self.Conference = data.get("Conference")

    def __repr__(self):
        return f"ConferenceId={self.ConferenceId} Conference={self.Conference}"


class Division(Base):
    __tablename__ = "Divisions"
    __table_args__ = {"schema": "Dim"}

    DivisionId = Column(Integer(), primary_key=True)
    Division = Column(String(5), nullable=False)
    ConferenceId = Column(Integer(), ForeignKey("Conferences.ConferenceId"))

    def __init__(self, data):
        data = data or {}
        self.DivisionId = data.get("DivisionId")
        self.Division = data.get("Division")
        self.ConferenceId = data.get("ConferenceId")

    def __repr__(self):
        return f"DivisionId={self.DivisionId} Division={self.Division} ConferenceId={self.ConferenceId}"


class Season(Base):
    __tablename__ = "Seasons"
    __table_args__ = {"schema": "Dim"}
    SeasonId = Column(Integer(), primary_key=True)
    StartYear = Column(Integer(), nullable=False)
    EndYear = Column(Integer(), nullable=False)

    games = relationship("Games")
    stats = relationship("Stats")

    def __init__(self, data):
        data = data or {}
        self.SeasonId = data.get("SeasonId")
        self.StartYear = data.get("StartYear")
        self.EndYear = data.get("EndYear")

    def __repr__(self):
        return f"SeasonId={self.SeasonId} StartYear={self.StartYear} EndYear={self.EndYear}"


class Team(Base):
    __tablename__ = "Teams"
    _table_args = {"schema": "Dim"}
    TeamId = Column(Integer(), primary_key=True)
    CityName = Column(String(200), nullable=False, unique=True)
    ConferenceId = Column(Integer(), ForeignKey("Conferences.ConferenceId"))
    Nickname = Column(String(200), nullable=False)

    players = relationship("Players")
    games = relationship("Games")
    stats = relationship("Stats")

    def __init__(self, data):
        data = data or {}
        self.TeamId = data.get("TeamId")
        self.CityName = data.get("CityName")
        self.ConferenceId = data.get("ConferenceId")
        self.Nickname = data.get("Nickname")

    def __repr__(self):
        return f"TeamId={self.TeamId} CityName={self.CityName} ConferenceId={self.ConferenceId} Nickname={self.Nickname}"


class Game(Base):
    __tablename__ = "Games"
    _table_args__ = {"schema": "Fact"}
    GameId = Column(Integer(), primary_key=True)
    SeasonId = Column(Integer(), ForeignKey("Seasons.SeasonId"))
    GameType = Column(String(3), nullable=False)
    Week = Column(Integer(), nullable=False)
    GameDate = Column(Date(), nullable=False)
    GameTime = Column(Time(), nullable=False)
    Weekday = Column(String(9), nullable=False)
    HomeScore = Column(Integer(), nullable=False)
    AwayScore = Column(Integer(), nullable=False)
    HomeTeamId = Column(Integer(), ForeignKey("Teams.TeamId"))
    AwayTeamId = Column(Integer(), ForeignKey("Teams.TeamId"))
    Location = Column(String(9), nullable=False)
    Overtime = Column(Boolean(), nullable=False)
    DivGame = Column(Boolean(), nullable=False)
    Roof = Column(String(8), nullable=False)
    Surface = Column(String(10), nullable=False)
    Temp = Column(Integer(), nullable=True)
    Wind = Column(Integer(), nullable=True)

    odds = relationship("Odds")
    stats = relationship("Stats")

    def __init__(self, data):
        data = data or {}
        self.GameId = data.get("GameId")
        self.SeasonId = data.get("SeasonId")
        self.GameType = data.get("GameType")
        self.Week = data.get("Week")
        self.GameDate = data.get("GameDate")
        self.GameTime = data.get("GameTime")
        self.Weekday = data.get("Weekday")
        self.HomeScore = data.get("HomeScore")
        self.AwayScore = data.get("AwayScore")
        self.HomeTeamId = data.get("HomeTeamId")
        self.AwayTeamId = data.get("AwayTeamId")
        self.Location = data.get("Location")
        self.Overtime = data.get("Overtime")
        self.DivGame = data.get("DivGame")
        self.Roof = data.get("Roof")
        self.Surface = data.get("Surface")
        self.Temp = data.get("Temp")
        self.Wind = data.get("Wind")

    def __repr__(self):
        return f"GameId={self.GameId} SeasonId={self.SeasonId} GameType={self.GameType} Week={self.Week} \
            GameDate={self.GameDate} GameTime={self.GameTime} Weekday={self.Weekday} HomeScore={self.HomeScore} AwayScore={self.AwayScore} \
            HomeTeamId={self.HomeTeamId} AwayTeamId={self.AwayTeamId} Location={self.Location} Overtime={self.Overtime} DivGame={self.DivGame} \
            Roof={self.Roof} Surface={self.Surface} Temp={self.Temp} Wind={self.Wind}"


class Odds(Base):
    __tablename__ = "Odds"
    OddsId = Column(Integer(), primary_key=True)
    GameId = Column(Integer(), ForeignKey("Games.Id"))
    HomeMoneyLine = Column(Integer(), nullable=False)
    AwayMoneyLine = Column(Integer(), nullable=False)
    HomeSpreadOdds = Column(Integer(), nullable=False)
    AwaySpreadOdds = Column(Integer(), nullable=False)
    SpreadLine = Column(Float(), nullable=False)
    TotalLine = Column(Float(), nullable=False)
    OverOdds = Column(Integer(), nullable=False)
    UnderOdds = Column(Integer(), nullable=False)

    def __init__(self, data):
        data = data or {}
        self.OddsId = data.get("OddsId")
        self.GameId = data.get("GameId")
        self.HomeMoneyLine = data.get("HomeMoneyLine")
        self.AwayMoneyLine = data.get("AwayMoneyLine")
        self.HomeSpreadOdds = data.get("HomeSpreadOdds")
        self.AwaySpreadOdds = data.get("AwaySpreadOdds")
        self.SpreadLine = data.get("SpreadLine")
        self.TotalLine = data.get("TotalLine")
        self.OverOdds = data.get("OverOdds")
        self.UnderOdds = data.get("UnderOdds")

    def __repr__(self):
        return f"OddsId={self.OddsId} GameId={self.GameId} HomeMoneyLine={self.HomeMoneyLine} AwayMoneyLine={self.AwayMoneyLine} \
            HomeSpreadOdds={self.HomeSpreadOdds} AwaySpreadOdds={self.AwaySpreadOdds} SpreadLine={self.SpreadLine} \
            TotalLine={self.TotalLine} OverOdds={self.OverOdds} UnderOdds={self.UnderOdds}"


class Players(Base):
    __tablename__ = "Players"
    PlayerId = Column(String(), primary_key=True)
    PlayerName = Column(String(), nullable=False)
    FirstName = Column(String(), nullable=False)
    LastName = Column(String(), nullable=False)
    TeamId = Column(Integer(), ForeignKey("Teams.TeamId"))

    stats = relationship("Stats")

    def __init__(self, data):
        data = data or {}
        self.PlayerId = data.get("PlayerId")
        self.PlayerName = data.get("PlayerName")
        self.FirstName = data.get("FirstName")
        self.LastName = data.get("LastName")
        self.TeamId = data.get("TeamId")

    def __repr__(self):
        return f"PlayerId={self.PlayerId} PlayerName={self.PlayerName} FirstName={self.FirstName} LastName={self.LastName} TeamId={self.TeamId}"


class Stats(Base):
    __tablename__ = "Stats"
    StatId = Column(Integer(), primary_key=True)
    PlayerId = Column(Integer(), ForeignKey("Players.PlayerId"))
    TeamId = Column(Integer(), ForeignKey("Teams.TeamId"))
    SeasonId = Column(Integer(), ForeignKey("Seasons.SeasonId"))
    GameId = Column(Integer(), ForeignKey("Games.GameId"))
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

    def __init__(self, data):
        data = data or {}
        self.StatId = data.get("StatId")
        self.PlayerId = data.get("PlayerId")
        self.TeamId = data.get("TeamId")
        self.SeasonId = data.get("SeasonId")
        self.GameId = data.get("GameId")
        self.Carries = data.get("Carries")
        self.Receptions = data.get("Receptions")
        self.Touches = data.get("Touches")
        self.Yards = data.get("Yards")
        self.Touchdowns = data.get("Touchdowns")
        self.Completions = data.get("Completions")
        self.PassingYards = data.get("PassingYards")
        self.PassingTouchdowns = data.get("PassingTouchdowns")
        self.Interceptions = data.get("Interceptions")
        self.PassingTwoPointConversions = data.get("PassingTwoPointConversions")
        self.SpecialTeamsTouchdowns = data.get("SpecialTeamsTouchdowns")
        self.TwoPointConversions = data.get("TwoPointConversions")
        self.Fumbles = data.get("Fumbles")

    def __repr__(self):
        return f"StatId={self.StatId} PlayerId={self.PlayerId} SeasonId={self.SeasonId} GameId={self.GameId} Carries={self.Carries} \
            Receptions={self.Receptions} Touches={self.Touches} Yards={self.Yards} Touchdowns={self.Touchdowns} Completions={self.Completions} \
            PassingYards={self.PassingYards} PassingTouchdowns={self.PassingTouchdowns} Interceptions={self.Interceptions} \
            PassingTwoPointConversions={self.PassingTwoPointConversions} SpecialTeamsTouchdowns={self.SpecialTeamsTouchdowns} TwoPointConversions={self.TwoPointConversions} \
            Fumbles={self.Fumbles}"
