# coinbase-sender
Simple python script that can be used to set up recurring sends from coinbase wallets to personal addresses 

### Usage
`pip install coinbase`

`python3 coinbase-sender.py`

I'm running this via `cron` on a raspberry pi like so:

```
# runs coinbase-sender.py the first Friday of every month and pipes output to a log file
0 12 1-7 * * [ "$(date '+\%a')" = "Fri" ] && python3 /home/pi/coinbase-sender.py >> /home/pi/coinbase-sender.log 2>&1
```
