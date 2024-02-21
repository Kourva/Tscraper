#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard imports
import sqlite3
from typing import ClassVar, NoReturn, Any


async def add_user(members: ClassVar[Any], me: ClassVar[Any]) -> NoReturn:
    """
    Function to add list of users to SQLite3 database

    Parameters:
        members: Telegram users

    Returns:
        Typing.NoReturn
    """

    # Connect to SQLite3 database inside the 'Users' directory
    connection: ClassVar[Any] = sqlite3.connect("Users/tuser.db")

    # Make a cursor for command execution
    cursor: ClassVar[Any] = connection.cursor()

    # Add user to database
    # Note: We already made a table for users, so if you don't have table, 
    # make one before using this tool
    # CREATE TABLE "users" (
    #     "chat_id"     INTEGER UNIQUE,
    #     "username"    TEXT,
    #     "access_hash" TEXT
    # );
    # Add members to database
    async for member in members:
        # Print status
        print(f"Adding {member.first_name}", end="\r", flush=True)

        # Exclude self bot (yourself)
        if me.id == member.id:
            continue
        
        # Execute add command
        cursor.execute(
            "INSERT OR IGNORE INTO users VALUES (?, ?, ?)", (
                member.id, member.username, member.access_hash
            )
        )

    # Print done message
    print("\n:: Add done.")

    # Commit changes
    connection.commit()

    # Close connection
    connection.close()
