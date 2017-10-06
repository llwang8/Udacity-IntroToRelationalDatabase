#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE * FROM matches;")
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE * FROM players;")
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) as num FROM players;")
    result = int(cursor.fetchall()[0][0])
    conn.close()
    return result


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO players VALUES (%s);"
    cursor.execute(query, name)
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT id, name, wins, matches FROM players, scoresByPlayers, matchesByPlayers where scores.pid = players.id and matchesByPlayers.id = players.id order by wins desc;"
    cursor.execute(query)
    result = cursor.fetechall()
    conn.close()
    return result



def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    cursor = conn.cursor()
    if int(winner) < int(loser):
        mid = cursor.execute("SELECT mid from tmatches where a_id = winner and b_id = loser;")
    else:
        mid = cursor.execute("SELECT mid from tmatches where a_id = loser and b_id = winner;")
    cursor.execute("INSERT into scores VALUES (winner, mid, 1);")
    cursor.commit()
    cursor.execute("INSERT into scores VALUES (loser, mid, 0);")
    cursor.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairings = []
    player = playerStandings()
    if len(player) < 2:
        raise KeyError("Not enough players")
    for i in range(0, len(player), 2):
        pairings.append(players[i][0], players[i][1], players[i+1][0], players[i+1][1])

    return pairings



