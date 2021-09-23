# Instructions for running `symptom_clean.py`

Tested on:

1. 
    - macOS Big Sur 11.5.2 (Apple Silicon)
    - Firefox 92.0.1 (64-bit)
    - GeckoDriver 0.30.0
    - Python 3.8.1

2.
    - Ubuntu 20.04.3 (64-bit)
    - Firefox 91.0.1 (64-bit)
    - GeckoDriver 0.29.1

For every system:
- Rename sample_config.py to config.py
- Download Firefox
- Create a new profile ([about:profiles](about:profiles)) in Firefox and put its path in the config.py file. (Alternatively use your default profile)
- Download [GeckoDriver](https://github.com/mozilla/geckodriver/releases) and put its path in the config.py file.
- Include the directory path of where symptom_clean.py is located in config.py.
- Include your password and username in config.py


Every 30 days:
- Open a browser instance using this profile and log in with your CalNet ID using 2FA. Click on the remember me for 30 days button.

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