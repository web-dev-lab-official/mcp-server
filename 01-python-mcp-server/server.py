from typing import Any
from calendar_service import create_event, list_events
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP[Any]("Demo", json_response=True)


@mcp.tool()
def create_calendar_event(
    summary: str,
    date: str,
    start_time: str,
    end_time: str,
    description: str = ""
):
    """
    Tool to create an event in Google Calendar.

    Parameters:
    - summary: Event title
    - date: Date in 'YYYY-MM-DD' format
    - start_time: Start time in 'HH:MM' 24-hour format
    - end_time: End time in 'HH:MM' 24-hour format
    - description: Optional description

    Returns:
    - Event details dictionary if successful, else None
    """
    # Combine date and time for ISO format
    start_iso = f"{date}T{start_time}:00Z"
    end_iso = f"{date}T{end_time}:00Z"

    return create_event(summary, start_iso, end_iso, description)



@mcp.resource("calendar://events/{date}")
def events_by_date(date: str):
    """
    Resource to fetch all events on a specific date.
    
    Parameters:
    - date: 'YYYY-MM-DD'
    
    Returns:
    - List of events on that date
    """
    start_time = f"{date}T00:00:00Z"
    end_time = f"{date}T23:59:59Z"
    return list_events(start_time, end_time)


@mcp.prompt()
def calendar_prompt(
    action: str, 
    event_name: str = "", 
    date: str = "", 
    start_time: str = "", 
    end_time: str = "", 
    description: str = ""
) -> str:
    """
    Generate a natural language instruction for calendar actions.

    Parameters:
    - action: 'create', 'view_month', 'view_date'
    - event_name: Event title (required for 'create')
    - date: Event date in 'YYYY-MM-DD' (required for 'create' and 'view_date')
    - start_time: Start time 'HH:MM' (required for 'create')
    - end_time: End time 'HH:MM' (required for 'create')
    - description: Optional event description

    Returns:
    - Instruction string to guide the MCP server or AI to take action.
    """
    if action == "create":
        return (
            f"Create a calendar event named '{event_name}' on {date} "
            f"from {start_time} to {end_time}. Description: {description or 'No description'}."
        )
    elif action == "view_month":
        return "Show all events of the current month in my Google Calendar."
    elif action == "view_date":
        return f"Show all events scheduled on {date}."
    else:
        return "Invalid action. Please choose 'create', 'view_month', or 'view_date'."

