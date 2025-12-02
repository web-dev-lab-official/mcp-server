# test_calendar.py
from calendar_service import create_event, list_events
import datetime

def test_create_and_list_month():
    now = datetime.datetime.now(datetime.timezone.utc)

    # Define a test event 5 minutes from now
    start_time = (now + datetime.timedelta(minutes=5)).isoformat()
    end_time = (now + datetime.timedelta(minutes=30)).isoformat()

    # Create an event
    create_event("Test Event", start_time, end_time, description="This is a test event.")

    # List all events of the current month
    events = list_events()  # time_min and time_max default to current month

    if not events:
        print("❌ No events found for this month.")
    else:
        print(f"📌 Found {len(events)} event(s) for the current month:")
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(f"- {start} | {event.get('summary')}")

if __name__ == "__main__":
    test_create_and_list_month()
