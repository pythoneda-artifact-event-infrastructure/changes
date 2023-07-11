"""
pythonedaartifacteventinfrastructureversioning/pythonedaartifacteventversioningdbus/dbus_version_requested.py

This file defines the DbusVersionRequested class.

Copyright (C) 2023-today rydnr's pythoneda-artifact-event-infrastructure/versioning

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
from pythonedaartifacteventversioning.version_requested import VersionRequested
from pythonedaartifacteventinfrastructureversioning.pythonedaartifacteventversioningdbus import DBUS_PATH
from typing import List

class DbusVersionRequested(ServiceInterface):
    """
    D-Bus interface for VersionRequested

    Class name: DbusVersionRequested

    Responsibilities:
        - Define the d-bus interface for the VersionRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusVersionRequested.
        """
        super().__init__("pythonedaartifactversioning_VersionRequested")

    @signal()
    def VersionRequested(self, repository_url: "s"):
        """
        Defines the VersionRequested d-bus signal.
        :param repository_url: The repository URL.
        :type repository_url: str
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
    def transform_VersionRequested(self, event: VersionRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythonedaartifacteventversioning.version_requested.VersionRequested
        :return: The event information.
        :rtype: List[str]
        """
        print(f'Transforming {event}')
        return [ event.repository_url, event.branch, event.id, json.dumps(event.previous_event_ids) ]

    @classmethod
    def signature_for_VersionRequested(cls, event: VersionRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythonedaartifacteventversioning.version_requested.VersionRequested
        :return: The signature.
        :rtype: str
        """
        return 'ssss'

    @classmethod
    def parse_pythonedaartifactversioning_VersionRequested(cls, message: Message) -> VersionRequested:
        """
        Parses given d-bus message containing a VersionRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The VersionRequested event.
        :rtype: pythonedaartifacteventversioning.version_requested.VersionRequested
        """
        print(f'Parsing {message} for VersionRequested')
        repository_url, branch, event_id, prev_event_id = message.body
        return VersionRequested(repository_url, branch, None, event_id, json.loads(prev_event_id))
