-- Sample Seed Data

INSERT INTO teams (team_id, team_name, country) VALUES 
(1, 'India', 'India'),
(2, 'Australia', 'Australia'),
(3, 'England', 'England');

INSERT INTO venues (venue_id, venue_name, city, country, capacity) VALUES 
(1, 'Wankhede Stadium', 'Mumbai', 'India', 33000),
(2, 'Melbourne Cricket Ground', 'Melbourne', 'Australia', 100000),
(3, 'Lord\'s Cricket Ground', 'London', 'England', 30000);

INSERT INTO players (player_id, full_name, country, playing_role, batting_style, bowling_style) VALUES 
(1, 'Virat Kohli', 'India', 'Batsman', 'Right-hand bat', 'Right-arm medium'),
(2, 'Rohit Sharma', 'India', 'Batsman', 'Right-hand bat', 'Right-arm offbreak'),
(3, 'Ravindra Jadeja', 'India', 'All-rounder', 'Left-hand bat', 'Slow left-arm orthodox'),
(4, 'Jasprit Bumrah', 'India', 'Bowler', 'Right-hand bat', 'Right-arm fast'),
(5, 'Pat Cummins', 'Australia', 'Bowler', 'Right-hand bat', 'Right-arm fast');

INSERT INTO matches (match_id, match_description, team1_id, team2_id, venue_id, match_date, format, winner_team_id, toss_winner_id, toss_decision, victory_margin, victory_type) VALUES 
(1, 'India vs Australia 1st ODI', 1, 2, 1, '2026-01-15', 'ODI', 1, 1, 'bat', 45, 'runs'),
(2, 'India vs England 2nd Test', 1, 3, 3, '2026-02-10', 'Test', 1, 3, 'bowl', 6, 'wickets');

INSERT INTO player_performances (match_id, player_id, runs_scored, balls_faced, fours, sixes, wickets_taken, overs_bowled, runs_conceded, catches, stumpings, batting_position) VALUES 
(1, 1, 112, 105, 10, 3, 0, 0.0, 0, 1, 0, 3),
(1, 2, 85, 72, 9, 4, 0, 0.0, 0, 0, 0, 1),
(1, 3, 30, 22, 2, 1, 3, 10.0, 48, 2, 0, 7),
(1, 4, 2, 5, 0, 0, 4, 9.2, 52, 0, 0, 10),
(1, 5, 15, 20, 1, 0, 2, 10.0, 60, 1, 0, 8);
