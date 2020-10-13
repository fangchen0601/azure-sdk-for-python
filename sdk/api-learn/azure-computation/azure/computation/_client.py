from ._generated.models import ComputeNode
from ._generated.models import Operation
from azure.core.paging import ItemPaged

class ComputationClient(object):
    """A Client for the AppConfiguration Service.

    :param str node_name: The name of the compute node.
    :param TokenCredential credential: The credentials to authenticate with the service.
    """

    def __init__(
        self,
        node_name,  # type: str
        credential,  # type: "TokenCredential"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        pass

    @classmethod
    def from_connection_string(cls, connection_string, **kwargs):
        # type: (str) -> ComputationClient
        """Build an ComputationClient from a connection string.

        :param str connection_string: A connection string, as retrieved
         from the Azure portal.
        """
        pass

    def list_compute_nodes(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> ItemPaged[ComputeNode]
        """list compute nodes

        :return: list of ComputeNode
        :rtype: ItemPaged[ComputeNode]
        :raises: ~azure.core.exceptions.ResourceNotFoundError: If no matching configuration setting exists.
        """
        pass

    def get_compute_node(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> ComputeNode
        """get a compute node

        :return: the compute node
        "rtype: ComputeNode
        :raises: ~azure.core.exceptions.ResourceNotFoundError: If no matching configuration setting exists.
        """
        pass

    def create_compute_node(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> ComputeNode
        """create a compute node

        :keyword ComputeNode compute_node: The computer node
        :return: ComputeNode
        :rtype: ComputeNode
        :raises: ~azure.core.exceptions.ResourceNotFoundError: If no matching configuration setting exists.
        """
        pass

    def compute_pi(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Begin a compute pi operation on a compute node.

        :keyword int precision: A custom type or function that will be passed the direct response
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.ResourceNotFoundError: If no matching configuration setting exists.
        """
        pass

    def get_operation(
        self,
        operation_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Operation
        """Get the compute operation status.

        :param operation_id:
        :type operation_id: str
        :return: Operation
        :rtype: Operation
        :raises: ~azure.core.exceptions.ResourceNotFoundError: If no matching configuration setting exists.
        """
        pass
