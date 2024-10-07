env_vars = {
  # Get From my.telegram.org
  "API_HASH": "167668e5b34bee09d76dbb14cf0afcd4",
  # Get From my.telegram.org
  "API_ID": "6859352",
  #Get For @BotFather
  "BOT_TOKEN": "7421937596:AAGz19eTDaHYTsvxJUsi4JuADgZcVjLMGBI",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "psql 'postgresql://postgres:t7kDBeWbLKBiGKEt@healthfully-warm-possum.data-1.use1.tembo.io:5432/postgres'",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "",
  # Force Subs Channel username without @
  "CHANNEL": "",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "",
  # Put Thumb Link 
  "THUMB": ""
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
