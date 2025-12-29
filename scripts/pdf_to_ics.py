import re
from datetime import datetime
from pathlib import Path

PDF_TEXT = Path("dienstplaene/kids_church.txt").read_text()
OUTPUT = Path("kalender/kalender.ics")

EVENTS = []

for line in PDF_TEXT.splitlines():
    if "Luke" in line:
        date_match = re.search(r"\d{2}\.\d{2}\.\d{2}", line)
        if not date_match:
            continue

        date = datetime.strptime(date_match.group(), "%d.%m.%y")
        EVENTS.append(date)

def event_block(date):
    uid = f"kidschurch-{date.strftime('%Y%m%d')}@luke"
    return f"""
BEGIN:VEVENT
UID:{uid}
DTSTAMP:{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}
DTSTART;TZID=Europe/Berlin:{date.strftime('%Y%m%d')}T093000
DTEND;TZID=Europe/Berlin:{date.strftime('%Y%m%d')}T120000
SUMMARY:Kids. Church
LOCATION:Life Church Hameln
BEGIN:VALARM
TRIGGER:-P2D
ACTION:DISPLAY
DESCRIPTION:Kids. Church in 2 Tagen
END:VALARM
BEGIN:VALARM
TRIGGER:-P1D
ACTION:DISPLAY
DESCRIPTION:Kids. Church morgen
END:VALARM
END:VEVENT
"""

calendar = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n"
for d in EVENTS:
    calendar += event_block(d)
calendar += "\nEND:VCALENDAR"

OUTPUT.write_text(calendar)
