# Write your code here
def format_time(hours, minutes, seconds):
    if hours < 10:
        hours = f"0{hours}"
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    return f"{hours}:{minutes}:{seconds}"