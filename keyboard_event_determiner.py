from subprocess import run, TimeoutExpired

try:
    run(["python", "event_namer.py"], check=True, timeout=3)
    print("scraped :)", "event_namer.py")
except TimeoutExpired:
    message_timeout = "Write down the number you see above. That is your keyboard event ID"
    print(message_timeout)
