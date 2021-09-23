# Instructions for running `symptom_clean.py`

Tested on:
- Ubuntu 20.04.3 (64-bit)
- Firefox 91.0.1 (64-bit)
- GeckoDriver 0.29.1

First time setup:
- Create a new profile ([about:profiles](about:profiles)) in Firefox and put its path in the script. (Alternatively use your default profile.)
- [Install GeckoDriver](https://github.com/mozilla/geckodriver/releases) and put its path in the script.
- Change the working directory as required.
- Put in your account details.

Every 30 days:
- Open a browser instance using this profile and log in with your CalNet ID using 2FA.
- Last completed 2021-08-22

Every day:
- run `symptom_clean.py`
- alternatively you can add it to your crontab (`crontab -e`):
```
# every day at midnight
@midnight python3 path_to_file/symptom_clean.py

# every time you turn on your computer
@reboot python3 path_to_file/symptom_clean.py
```

## Debugging information
If you need the program to display a browser window (for debugging purposes) you should comment out the line `options=options,` (line 16).
You may also need to first run `export DISPLAY=:0` in your terminal for it to run.