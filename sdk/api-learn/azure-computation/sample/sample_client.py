# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import os
from azure.identity import DefaultAzureCredential
from azure.computation import ComputationClient
from azure.core.exceptions import ResourceNotFoundError

def main():
    nodename = os.environ['API-LEARN_NODENAME']
    credentials = DefaultAzureCredential()
    client = ComputationClient(nodename, credentials)

    # list
    try:
        nodes = client.list_compute_nodes()
        for node in nodes:
            print(node.name)
    except ResourceNotFoundError:
        raise

    # get
    try:
        node = client.get_compute_node()
        print(node.name)
    except ResourceNotFoundError:
        raise

    # create
    try:
        node = client.create_compute_node()
        print(node.name)
    except ResourceNotFoundError:
        raise

    # post pi
    try:
        client.compute_pi()
    except ResourceNotFoundError:
        raise

    # get operation
    try:
        operation = client.get_operation()
        print(operation.status)
    except ResourceNotFoundError:
        raise

if __name__ == "__main__":
    main()
