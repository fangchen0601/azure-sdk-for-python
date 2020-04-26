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
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.eventhub.v2018_01_01_preview.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class ClusterPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Cluster <azure.mgmt.eventhub.v2018_01_01_preview.models.Cluster>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Cluster]'}
    }

    def __init__(self, *args, **kwargs):

        super(ClusterPaged, self).__init__(*args, **kwargs)
class EHNamespacePaged(Paged):
    """
    A paging container for iterating over a list of :class:`EHNamespace <azure.mgmt.eventhub.v2018_01_01_preview.models.EHNamespace>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[EHNamespace]'}
    }

    def __init__(self, *args, **kwargs):

        super(EHNamespacePaged, self).__init__(*args, **kwargs)
class IpFilterRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`IpFilterRule <azure.mgmt.eventhub.v2018_01_01_preview.models.IpFilterRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[IpFilterRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(IpFilterRulePaged, self).__init__(*args, **kwargs)
class VirtualNetworkRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkRule <azure.mgmt.eventhub.v2018_01_01_preview.models.VirtualNetworkRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkRulePaged, self).__init__(*args, **kwargs)