#!/usr/bin/env python3
"""Generate personalised invitation files from a template."""

PLACEHOLDERS = ("name", "event_title", "event_date", "event_location")


def generate_invitations(template, attendees):
    """Write one output_X.txt file per attendee, filled from template."""
    if not isinstance(template, str):
        print("Error: template must be a string, got {}".format(
            type(template).__name__))
        return

    valid_list = isinstance(attendees, list) and all(
        isinstance(attendee, dict) for attendee in attendees)
    if not valid_list:
        print("Error: attendees must be a list of dictionaries, got {}".format(
            type(attendees).__name__))
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template
        for key in PLACEHOLDERS:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        filename = "output_{}.txt".format(index)
        try:
            with open(filename, "w") as file:
                file.write(output)
        except OSError as error:
            print("Error writing {}: {}".format(filename, error))
