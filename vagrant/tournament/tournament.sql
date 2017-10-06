-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE database tournament;
\c tournament;

CREATE table players (
    id serial primary key,
    name varchar(30),
    --wins integer default 0,
    --matches integer default 0
);

CREATE table tmatches(
    mid serial primary key,
    win_id integer references players,
    loser_id integer references players

);

CREATE table scores(
    pid integer,
    mid integer,
    scores integer

);

CREATE view scoresByPlayers as
    SELECT pid, sum(scores) as wins
    from scores group by pid;

CREATE view matchesByPlayers as
    SELECT id, count(mid) as matches
    from players, tmatches where a_id = id or b_id = id group by id;



