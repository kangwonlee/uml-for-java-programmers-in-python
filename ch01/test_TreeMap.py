import pytest

import TreeMap


@pytest.fixture
def TreeNode():
    return TreeMap.TreeNode('key', 'value')


def test_TreeNode_constructor(TreeNode):
    result = TreeNode

    assert isinstance(result, TreeMap.TreeNode), type(result)
    assert 'key' == result.itsKey, result.itsKey
    assert 'value' == result.itsValue, result.itsValue
    assert result.nodes[result.LESS] is None
    assert result.nodes[result.GREATER] is None


def test_TreeNode_select_sub_node(TreeNode):
    top = TreeNode
    top.itsKey = 0
    top.nodes[top.LESS] = TreeMap.TreeNode(-1, 'less')
    top.nodes[top.GREATER] = TreeMap.TreeNode(1, 'greater')

    result_index_less = top.selectSubNode(-1)
    assert top.LESS == result_index_less, result_index_less
    result_index_greater = top.selectSubNode(1)
    assert top.GREATER == result_index_greater, result_index_greater

    try:
        result_raise = top.selectSubNode(0)
    except AssertionError:
        pass
