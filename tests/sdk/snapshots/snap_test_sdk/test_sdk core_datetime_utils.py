# This file was auto-generated by Fern from our API Definition.

import datetime as dt


def serialize_datetime(v: dt.datetime) -> str:
    """
    Serialize a datetime including timezone info.

    Uses the timezone info provided if present, otherwise uses the current runtime's timezone info.
    """

    if v.tzinfo is not None:
        return v.isoformat()
    else:
        local_tz = dt.datetime.now().astimezone().tzinfo
        localized_dt = v.replace(tzinfo=local_tz)
        return localized_dt.isoformat()