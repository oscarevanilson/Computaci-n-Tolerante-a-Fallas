# specify start image
FROM python
# all commands start from this directory
WORKDIR /count-bot
# copy all files from this folder to working directory (ignores files in .dockerignore)
COPY . .
# set a default environment variable for the name of your bot
ENV BOT_NAME='Docker Bot'
# set the start command
CMD [ "python3", "count-bot.py" , "./test.txt", "n"]