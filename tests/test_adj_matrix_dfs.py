from activity.main import adj_matrix_dfs
import pytest 

def test_adj_matrix_dfs_connected_graph():
    # Arrange
    adj_matrix = [
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]

    # Act 
    result = adj_matrix_dfs(adj_matrix, 1)

    # Assert
    assert result == [1, 0, 2, 3, 4]

def test_adj_matrix_dfs_empty_graph():
    # Arrange
    adj_matrix = []

    # Act
    result = adj_matrix_dfs(adj_matrix, 1)

    # Assert
    assert result == []

def test_adj_matrix_dfs_one_node_graph():
    # Arrange
    adj_matrix = [
        [0]
    ]

    # Act
    result = adj_matrix_dfs(adj_matrix, 0)

    # Assert
    assert result == [0]

def test_adj_matrix_dfs_disconnected_graph():
    # Arrange
    adj_matrix = [
        [0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 0],
    ]

    # Act
    group_one = adj_matrix_dfs(adj_matrix, 3)
    group_two = adj_matrix_dfs(adj_matrix, 5)

    # Assert
    assert group_one == [3, 2, 1, 0, 4]
    assert group_two == [5, 6, 7]

def test_adj_matrix_dfs_directed_graph():
    # Arrange
    adj_matrix = [
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    # Act
    result = adj_matrix_dfs(adj_matrix, 1)

    # Assert
    assert result == [1, 0, 2, 3]