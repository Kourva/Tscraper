#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Automated Telegram Scraper - Author: KourvA
https://github.com/kourva/Tscraper
"""

# Standard imports
import json
from typing import Dict, ClassVar, Any, NoReturn, Union, List

# Third-party imports
import telethon
from telethon.sync import TelegramClient, events, types

# Internal imports
from sqlutil import add_user

# Get account credential from 'credential.json'
try:
    with open("credential.json", "r") as data:
        credits: Dict[str, Union[int, str]] = json.load(data)

except FileNotFoundError:
    raise SystemExit(":: No credential file found!")


# initialize client and connect to self bot
client: ClassVar[Any] = TelegramClient(
    session=credits["phone_number"][1:], 
    api_id=credits["api_id"],
    api_hash=credits["api_hash"]
)

# Log the process states into terminal
print(":: Attempting to login into Telegram, please wait...")

try:
    client.connect()
except OSError as error:
    print(f"  * Failed to connect due to\n    {error}")


# Get the code OTP code from user and continue login
if not client.is_user_authorized():
    # Send OTP code
    otp_code: ClassVar[Any] = client.send_code_request(
        phone=credits["phone_number"]
    )

    # Get OTP code from user
    code: str = input(
        f"  ? Enter OTP code just sent to {credits['phone_number']}: "
    )
     
    # Login using OTP code
    try:
        self_user: ClassVar[Any] = (
            client.sign_in(
                phone=credits["phone_number"],
                code=code,
                phone_code_hash=otp_code.phone_code_hash
            )
        )

    # Try again using 2FA password if it's required
    except telethon.errors.rpcerrorlist.SessionPasswordNeededError:
        self_user: ClassVar[Any] = (
            client.sign_in(
                password=credits["password"],
            )
        )

    else:
        # Log the process states into terminal
        print("  * Login successful!")
    
# If user has session already...
else:
    print("  * You're already logged in!")


# Event handler for new incoming messages
@client.on(events.Raw())
async def row_update_handler(event: ClassVar[Any]) -> NoReturn:
    """
    Function to handle channel updates using Raw updates

        Basically, when you join or left the group,
        this handler will know it and handle it.

        If action is join, it will scrape the members.
        If action is left, there is nothing do to!

    Parameters:
        event: Update event from telegram

    Returns:
        typing.NoReturn
    """

    # Handle only UpdateChannel updates
    if type(event) is telethon.tl.types.UpdateChannel:
        try:
            # Extract group info from update
            target_group: ClassVar[Any] = await client.get_entity(
                event.channel_id
            )
            
            # Get self info (yourself)
            me: ClassVar[Any] = await client.get_me()
        
            # Exclude 'left the group' updates
            if target_group.left == True:
                raise telethon.errors.rpcerrorlist.ChannelPrivateError
            
            # Check if group is done before or not
            with open("Users/groups.txt", "r") as data:
                groups: List[str] = list(
                    data.read().strip().split("\n")
                )
                if str(target_group.id) in groups:
                    print("Group done before.")
                    return 1

            
            # Iterate through group members
            members: ClassVar[Any] = client.iter_participants(
                target_group, aggressive=True
            )

            # Print the status and add members
            print(f"Getting members from group {target_group.title}")
            await add_user(members, me)

            # Add group ID to groups (to avoid duplication)
            with open("Users/groups.txt", "a") as data:
                data.write(f"{target_group.id}\n")

            # Send status message to saved messages
            await client.send_message(
                entity="me",
                message=(
                    f"Users added to database from:\n"
                    f"{target_group.title}"
                )
            )

        # Handle group exception (left / banned / private)
        except telethon.errors.rpcerrorlist.ChannelPrivateError:
            print(":: You left the group")

        # Log other exceptions
        except Exception as error:
            print(f":: Log -> Error due to {error}")


# Run the bot
with client:
    print("\n:: Self is running...  [Ctrl+C to break]")
    client.run_until_disconnected()
