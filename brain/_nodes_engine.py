#!/usr/bin/env python3
from argparse import Namespace

from brain.engine_base.node_base import NodeManager
from brain.nodes.test_node import TestNode_1, TestNode_2


def start_nodes_engine(args: Namespace):
	# Arguments handeling
	if not args.nocan:
		from brain.nodes.can_node import CanNode

	# NodeManager singleton
	man = NodeManager.get_instance()

	# Adding all nodes
	if not args.nocan:
		man.add_node(CanNode, kwargs={'dev': 'can0'})
	man.add_node(TestNode_1, kwargs={'intervale': 1.5})
	man.add_node(TestNode_2)

	# Starting all nodes
	man.start_nodes()

	# TODO: wait for readyness

	# Wait for all nodes to stop (which means that the brain has shutdown)
	for node in man.get_all_nodes():
		for t in node.threads:
			t.join()


if __name__ == '__main__':
	start_nodes_engine()
