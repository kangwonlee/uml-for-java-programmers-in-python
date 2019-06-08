import pytest

import TreeMap


@pytest.fixture
def TreeNode():
    tree = TreeMap.TreeNode('key', 'value')

    yield tree

    del tree


def test_TreeNode_constructor(TreeNode):
    result = TreeNode

    assert isinstance(result, TreeMap.TreeNode), type(result)
    assert 'key' == result.itsKey, result.itsKey
    assert 'value' == result.itsValue, result.itsValue
    assert result.nodes[result.LESS] is None
    assert result.nodes[result.GREATER] is None


@pytest.fixture
def ThreeTreeNodes(TreeNode):
    top = TreeNode
    top.itsKey = 0
    top.nodes[top.LESS] = TreeMap.TreeNode(-1, 'less')
    top.nodes[top.GREATER] = TreeMap.TreeNode(1, 'greater')

    yield top

    del top


def test_TreeNode_select_sub_node(ThreeTreeNodes):
    top = ThreeTreeNodes

    result_index_less = top.selectSubNode(-1)
    assert top.LESS == result_index_less, result_index_less
    result_index_greater = top.selectSubNode(1)
    assert top.GREATER == result_index_greater, result_index_greater

    try:
        _ = top.selectSubNode(0)
    except AssertionError:
        pass


def test_TreeNode_find_less_exists(ThreeTreeNodes):
    top = ThreeTreeNodes

    result_node_less = top.find(-1)
    assert result_node_less == top.nodes[top.LESS].itsValue, result_node_less


def test_TreeNode_find_greater_exists(ThreeTreeNodes):
    top = ThreeTreeNodes

    result_node_greater = top.find(1)
    assert result_node_greater == top.nodes[top.GREATER].itsValue, result_node_greater


def test_TreeNode_find_less_doesnt_exist(ThreeTreeNodes):
    top = ThreeTreeNodes

    result_node_less_none = top.find(-2)
    assert result_node_less_none is None, result_node_less_none


def test_TreeNode_find_greater_doesnt_exist(ThreeTreeNodes):
    top = ThreeTreeNodes

    result_node_greater_none = top.find(2)
    assert result_node_greater_none is None, result_node_greater_none


def test_TreeNode_add_less_minus_2(ThreeTreeNodes):
    top = ThreeTreeNodes

    # method under test
    top.add(-2, '-2')

    result = top.find(-2)

    assert '-2' == result, result
    assert '-2' == top.nodes[top.LESS].nodes[top.LESS].itsValue


def test_TreeNode_add_less_minus_05(ThreeTreeNodes):
    top = ThreeTreeNodes

    # method under test
    top.add(-0.5, '-0.5')

    result = top.find(-0.5)

    assert '-0.5' == result, result
    assert '-0.5' == top.nodes[top.LESS].nodes[top.GREATER].itsValue


def test_TreeNode_add_more_plus_05(ThreeTreeNodes):
    top = ThreeTreeNodes

    # method under test
    top.add(0.5, '0.5')

    result = top.find(0.5)

    assert '0.5' == result, result
    assert '0.5' == top.nodes[top.GREATER].nodes[top.LESS].itsValue


def test_TreeNode_add_more_plus_2(ThreeTreeNodes):
    top = ThreeTreeNodes

    # method under test
    top.add(2, '2')

    result = top.find(2)

    assert '2' == result, result
    assert '2' == top.nodes[top.GREATER].nodes[top.GREATER].itsValue


@pytest.fixture
def treemap_tree():
    tree = TreeMap.TreeMap()

    yield tree

    del tree


def test_TreeMap_constructor(treemap_tree):
    assert isinstance(treemap_tree, TreeMap.TreeMap)


@pytest.fixture
def three_node_tree(ThreeTreeNodes):
    tree = TreeMap.TreeMap()
    tree.topNode = ThreeTreeNodes

    yield tree

    del tree


def test_TreeMap_get_less_exists(three_node_tree):
    top = three_node_tree

    result_value_less = top.get(-1)
    assert result_value_less == top.topNode.nodes[top.topNode.LESS].itsValue, result_value_less


def test_TreeMap_get_greater_exists(three_node_tree):
    top = three_node_tree

    result_value_greater = top.get(1)
    assert result_value_greater == top.topNode.nodes[top.topNode.GREATER].itsValue, result_value_greater
