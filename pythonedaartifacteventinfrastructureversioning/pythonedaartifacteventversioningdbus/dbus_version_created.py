"""
pythonedaartifacteventinfrastructureversioning/pythonedaartifacteventversioningdbus/dbus_version_created.py

This file defines the DbusVersionCreated class.

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
from pythonedaartifacteventversioning.version_created import VersionCreated
from pythonedaartifacteventinfrastructureversioning.pythonedaartifacteventversioningdbus import DBUS_PATH
from typing import List

class DbusVersionCreated(ServiceInterface):
    """
    D-Bus interface for VersionCreated

    Class name: DbusVersionCreated

    Responsibilities:
        - Define the d-bus interface for the VersionCreated event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusVersionCreated.
        """
        super().__init__("pythonedaartifactversioning_VersionCreated")

    @signal()
    def VersionCreated(self, version: "s", repository_url: "s"):
        """
        Defines the VersionCreated d-bus signal.
        :param version: The version.
        :type version: str
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
    def transform_VersionCreated(cls, event: VersionCreated) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythonedaartifacteventversioning.version_created.VersionCreated
        :return: The event information.
        :rtype: List[str]
        """
        return [ event.version, event.repository_url, event.id, json.dumps(event.previous_event_ids) ]

    @classmethod
    def signature_for_VersionCreated(cls, event: VersionCreated) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythonedaartifacteventversioning.version_created.VersionCreated
        :return: The signature.
        :rtype: str
        """
        return 'ssss'

    @classmethod
    def parse_pythonedaartifactversioning_VersionCreated(cls, message: Message) -> VersionCreated:
        """
        Parses given d-bus message containing a VersionCreated event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The VersionCreated event.
        :rtype: pythonedaartifacteventversioning.version_created.VersionCreated
        """
        version, repository_url, event_id, prev_event_ids = message.body
        return VersionCreated(version, repository_url, None, event_id, json.loads(prev_event_ids))
