"""
pythonedaartifacteventinfrastructurechanges/pythonedaartifacteventchangesdbus/dbus_change_staging_requested.py

This file defines the DbusChangeStagingRequested class.

Copyright (C) 2023-today rydnr's pythoneda-artifact-event-infrastructure/changes

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from dbus_next import Message
from dbus_next.service import ServiceInterface, signal
import json
from pythonedaartifacteventchanges.change_staging_requested import ChangeStagingRequested
from pythonedaartifacteventinfrastructurechanges.pythonedaartifacteventchangesdbus import DBUS_PATH
from typing import List

class DbusChangeStagingRequested(ServiceInterface):
    """
    D-Bus interface for ChangeStagingRequested

    Class name: DbusChangeStagingRequested

    Responsibilities:
        - Define the d-bus interface for the ChangeStagingRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusChangeStagingRequested.
        """
        super().__init__("pythonedaartifactchanges_ChangeStagingRequested")

    @signal()
    def ChangeStagingRequested(self, change: "s"):
        """
        Defines the ChangeStagingRequested d-bus signal.
        :param change: The change.
        :type change: str
        """
        pass

    @classmethod
    def path(cls) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH

    @classmethod
    def transform_ChangeStagingRequested(self, event: ChangeStagingRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythonedaartifacteventchanges.change_staging_requested.ChangeStagingRequested
        :return: The event information.
        :rtype: List[str]
        """
        print(f'Transforming {event}')
        return [ str(event.change), event.id, json.dumps(event.previous_event_ids) ]

    @classmethod
    def signature_for_ChangeStagingRequested(cls, event: ChangeStagingRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythonedaartifacteventchanges.change_staging_requested.ChangeStagingRequested
        :return: The signature.
        :rtype: str
        """
        return 'sss'

    @classmethod
    def parse_pythonedaartifactchanges_ChangeStagingRequested(cls, message: Message) -> ChangeStagingRequested:
        """
        Parses given d-bus message containing a ChangeStagingRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The ChangeStagingRequested event.
        :rtype: pythonedaartifacteventchanges.change_staging_requested.ChangeStagingRequested
        """
        print(f'Parsing {message} for ChangeStagingRequested')
        change_json, event_id, prev_event_id = message.body
        return ChangeStagingRequested(json.loads(change_json), None, event_id, json.loads(prev_event_id))
