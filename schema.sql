-- Cricbuzz LiveStats Database Schema

DROP TABLE IF EXISTS player_performances;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS venues;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE venues (
    venue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    venue_name TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    capacity INTEGER
);

CREATE TABLE players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    country TEXT NOT NULL,
    playing_role TEXT CHECK(playing_role IN ('Batsman', 'Bowler', 'All-rounder', 'Wicket-keeper')),
    batting_style TEXT,
    bowling_style TEXT
);

CREATE TABLE matches (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_description TEXT NOT NULL,
    team1_id INTEGER,
    team2_id INTEGER,
    venue_id INTEGER,
    match_date TEXT NOT NULL,
    format TEXT CHECK(format IN ('Test', 'ODI', 'T20I')),
    winner_team_id INTEGER,
    toss_winner_id INTEGER,
    toss_decision TEXT,
    victory_margin INTEGER,
    victory_type TEXT,
    FOREIGN KEY (team1_id) REFERENCES teams(team_id),
    FOREIGN KEY (team2_id) REFERENCES teams(team_id),
    FOREIGN KEY (venue_id) REFERENCES venues(venue_id),
    FOREIGN KEY (winner_team_id) REFERENCES teams(team_id)
);

CREATE TABLE player_performances (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER,
    player_id INTEGER,
    runs_scored INTEGER DEFAULT 0,
    balls_faced INTEGER DEFAULT 0,
    fours INTEGER DEFAULT 0,
    sixes INTEGER DEFAULT 0,
    wickets_taken INTEGER DEFAULT 0,
    overs_bowled REAL DEFAULT 0.0,
    runs_conceded INTEGER DEFAULT 0,
    catches INTEGER DEFAULT 0,
    stumpings INTEGER DEFAULT 0,
    batting_position INTEGER,
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);
