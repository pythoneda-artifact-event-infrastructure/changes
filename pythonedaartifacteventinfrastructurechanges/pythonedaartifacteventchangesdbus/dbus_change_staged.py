"""
pythonedaartifacteventinfrastructurechanges/pythonedaartifacteventchangesdbus/dbus_change_staged.py

This file defines the DbusChangeStaged class.

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
from pythonedaartifacteventchanges.change_staged import ChangeStaged
from pythonedaartifacteventinfrastructurechanges.pythonedaartifacteventchangesdbus import DBUS_PATH
from typing import List

class DbusChangeStaged(ServiceInterface):
    """
    D-Bus interface for ChangeStaged

    Class name: DbusChangeStaged

    Responsibilities:
        - Define the d-bus interface for the ChangeStaged event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusChangeStaged.
        """
        super().__init__("pythonedaartifactchanges_ChangeStaged")

    @signal()
    def ChangeStaged(self, change: "s"):
        """
        Defines the ChangeStaged d-bus signal.
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
    def transform_ChangeStaged(cls, event: ChangeStaged) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythonedaartifacteventchanges.change_staged.ChangeStaged
        :return: The event information.
        :rtype: List[str]
        """
        return [ json.dumps(event.change), event.id, json.dumps(event.previous_event_ids) ]

    @classmethod
    def signature_for_ChangeStaged(cls, event: ChangeStaged) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythonedaartifacteventchanges.change_staged.ChangeStaged
        :return: The signature.
        :rtype: str
        """
        return 's'

    @classmethod
    def parse_pythonedaartifactchanges_ChangeStaged(cls, message: Message) -> ChangeStaged:
        """
        Parses given d-bus message containing a ChangeStaged event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The ChangeStaged event.
        :rtype: pythonedaartifacteventchanges.change_staged.ChangeStaged
        """
        change, event_id, prev_event_ids = message.body
        return ChangeStaged(json.loads(change), None, event_id, json.loads(prev_event_ids))
