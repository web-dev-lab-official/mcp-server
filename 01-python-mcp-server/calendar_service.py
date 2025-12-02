# calendar_service.py
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from auth import get_credentials
import datetime

def get_calendar_service():
    """Return an authorized Google Calendar API service."""
    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)
    return service

def create_event(summary, start_time, end_time, description=None):
    """Create an event on the primary calendar."""
    service = get_calendar_service()

    event_body = {
        "summary": summary,
        "description": description or "",
        "start": {"dateTime": start_time, "timeZone": "UTC"},
        "end": {"dateTime": end_time, "timeZone": "UTC"},
    }

    try:
        event = service.events().insert(calendarId="primary", body=event_body).execute()
        print(f"✅ Event created: {event.get('summary')} ({event.get('id')})")
        return event
    except HttpError as error:
        print(f"❌ An error occurred while creating event: {error}")
        return None

def list_events(time_min=None, time_max=None, max_results=250):
    """
    Fetch events from the primary calendar within a time range.
    By default, fetches all events for the current month.
    """
    service = get_calendar_service()

    if not time_min or not time_max:
        now = datetime.datetime.now(datetime.timezone.utc)

        # First day of current month, 00:00 UTC
        first_day = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        # First day of next month
        if now.month == 12:
            next_month = first_day.replace(year=now.year + 1, month=1)
        else:
            next_month = first_day.replace(month=now.month + 1)

        time_min = first_day.isoformat()
        time_max = next_month.isoformat()

    try:
        events_result = service.events().list(
            calendarId="primary",
            timeMin=time_min,
            timeMax=time_max,
            singleEvents=True,
            orderBy="startTime",
            maxResults=max_results,
        ).execute()

        events = events_result.get("items", [])
        return events

    except HttpError as error:
        print(f"❌ An error occurred while fetching events: {error}")
        return []