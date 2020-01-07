# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.redis.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class RedisResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`RedisResource <azure.mgmt.redis.models.RedisResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RedisResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(RedisResourcePaged, self).__init__(*args, **kwargs)
class RedisFirewallRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`RedisFirewallRule <azure.mgmt.redis.models.RedisFirewallRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RedisFirewallRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(RedisFirewallRulePaged, self).__init__(*args, **kwargs)
class RedisPatchSchedulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`RedisPatchSchedule <azure.mgmt.redis.models.RedisPatchSchedule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RedisPatchSchedule]'}
    }

    def __init__(self, *args, **kwargs):

        super(RedisPatchSchedulePaged, self).__init__(*args, **kwargs)
class RedisLinkedServerWithPropertiesPaged(Paged):
    """
    A paging container for iterating over a list of :class:`RedisLinkedServerWithProperties <azure.mgmt.redis.models.RedisLinkedServerWithProperties>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RedisLinkedServerWithProperties]'}
    }

    def __init__(self, *args, **kwargs):

        super(RedisLinkedServerWithPropertiesPaged, self).__init__(*args, **kwargs)