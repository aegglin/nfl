import model

import os
import pandas as pd
import sqlalchemy
import rpy2.robjects as robjects


def import_data():

    robjects.r('''
        library(nflfastR)
        library(dplyr)
        data <- nflfastR::load_pbp(2020:2022) %>%
        dplyr::filter(season_type == "REG") %>%
        nflfastR::calculate_player_stats(weekly = TRUE) %>%
        dplyr::mutate(
            yards = rushing_yards + receiving_yards, 
            touches = carries + receptions, 
            tds = rushing_tds + receiving_tds,
            fumbles = sack_fumbles_lost + rushing_fumbles_lost + receiving_fumbles_lost,
            two_point_conversions = receiving_2pt_conversions + rushing_2pt_conversions
        ) %>%
        dplyr::arrange(-yards) %>%s
        dplyr::select(player_name, season, recent_team, week, carries, receptions, touches, yards, tds, completions, passing_yards, passing_tds, interceptions, passing_2pt_conversions, special_teams_tds, two_point_conversions, fumbles)

        data <- data[order(data$week, data$player_name),]
        write.csv(data, "data.csv")

        write.csv(nflfastR::teams_colors_logos, "teams.csv")
        write.csv(nflfastR::fast_scraper_schedules(2020:2022, "schedule.csv")
    ''')

    data = pd.read_csv('data.csv', index_col = 0)
    teams = pd.read_csv('teams.csv', index_col = 0)
    schedule = pd.read_csv('schedule.csv', index_col=0)

    # delete the files
    os.remove('data.csv')
    os.remove('teams.csv')
    os.remove('schedule.csv')

    return data, teams, schedule

def main():
    data, teams = import_data()
    
    for team in teams:
        pass