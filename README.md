# CussRanker-Discord-bot
***Discord server Bot*** used to rank user sentences

# How to use?

## Discord setup

### Discord developer

1. Create new application on discord dev
2. In **Bot** tab check 3 checkboxes:
    _- SERVER MEMBERS INTENT_
    _- MESSAGE CONTENT INTENT_
    _- PRESENCE INTENT_

3. Go to **OAuth2** and do following steps:
    1. Check **bot** scope.
    2. In ***BOT PERMISSIONS*** tab that just popped check:
        _- Send Messages_
        _- Manage Messages_
        _- Mention Everyone_
        _- Read Message History_
        _- Add Reactions_
        _- View channels_
        _- Manage channels_
    3. Copy _url_ generated.

4. Pase ***url*** into browser **search** and add bot to your **server**.

## Runnig the bot

1. Go to the root directory of the project
2. Installing dependencies
3. Create `.env` file with these variables:
    - **`GROQ_API_KEY`**,
    - **`ADD_LINK`** (Optional),
    - **`DISCORD_TOKEN`**
4. Open terminal and type: `python3 main.py`

# Now you are all set. **HAVE FUN**


     

