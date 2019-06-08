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
