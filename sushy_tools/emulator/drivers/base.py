# Copyright 2018 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import abc
import six


@six.add_metaclass(abc.ABCMeta)
class AbstractDriver(object):
    """Base class for all virtualization drivers"""

    @abc.abstractproperty
    def driver(self):
        """Return human-friendly driver information

        :returns: driver information as `str`
        """

    @abc.abstractproperty
    def systems(self):
        """Return available computer systems

        :returns: list of computer systems names.
        """

    @abc.abstractmethod
    def uuid(self, identity):
        """Get computer system UUID

        The universal unique identifier (UUID) for this system. Can be used
        in place of system name if there are duplicates.

        If virtualization backend does not support non-unique system identity,
        this property may just return the `identity`.

        :returns: computer system UUID
        """

    @abc.abstractmethod
    def get_power_state(self, identity):
        """Get computer system power state

        :returns: current power state as *On* or *Off* `str` or `None`
            if power state can't be determined
        """

    @abc.abstractmethod
    def set_power_state(self, identity, state):
        """Set computer system power state

        :param state: string literal requesting power state transition.
            If not specified, current system power state is returned.
            Valid values  are: *On*, *ForceOn*, *ForceOff*, *GracefulShutdown*,
            *GracefulRestart*, *ForceRestart*, *Nmi*.
        :raises: `FishyError` if power state can't be set
        """

    @abc.abstractmethod
    def get_boot_device(self, identity):
        """Get computer system boot device name

        :returns: boot device name as `str` or `None` if device name
            can't be determined
        """

    @abc.abstractmethod
    def set_boot_device(self, identity, boot_source):
        """Set computer system boot device name

        :param boot_source: string literal requesting boot device change on the
            system. If not specified, current boot device is returned.
            Valid values are: *Pxe*, *Hdd*, *Cd*.
        :raises: `FishyError` if boot device can't be set
        """

    @abc.abstractmethod
    def get_total_memory(self, identity):
        """Get computer system total memory

        :returns: available RAM in GiB as `int` or `None` if total memory
            count can't be determined
        """

    @abc.abstractmethod
    def get_total_cpus(self, identity):
        """Get computer system total count of available CPUs

        :returns: available CPU count as `int` or `None` if CPU count
            can't be determined
        """