from project import remaining_cells,hidden_mat,look_around
import pytest

#test look_around method
def test_look_around_corner():
     mat=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
     assert look_around(mat,0,0)=={(0, 1), (1, 0), (1, 1)}
     assert look_around(mat,0,4)=={(0, 3), (1, 3), (1, 4)}
     assert look_around(mat,4,0)=={(3, 1), (4, 1), (3, 0)}
     assert look_around(mat,4,4)=={(3, 3), (3, 4), (4, 3)}

def test_look_around_sides():
     mat=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
     assert look_around(mat,0,2)=={(0, 1), (1, 2), (1, 1), (0, 3), (1, 3)}
     assert look_around(mat,2,0)=={(2, 1), (3, 1), (1, 1), (3, 0), (1, 0)}
     assert look_around(mat,4,2)=={(4, 3), (3, 1), (3, 3), (3, 2), (4, 1)}
     assert look_around(mat,2,4)=={(3, 4), (1, 4), (2, 3), (3, 3), (1, 3)}

def test_look_around_inside():
     mat=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
     assert look_around(mat,1,1)=={(0, 1), (1, 2), (2, 1), (0, 0), (2, 0), (0, 2), (2, 2), (1, 0)}
     assert look_around(mat,1,3)=={(2, 4), (1, 2), (0, 4), (0, 3), (1, 4), (2, 3), (0, 2), (2, 2)}
     assert look_around(mat,3,1)=={(4, 0), (2, 1), (2, 0), (4, 2), (3, 0), (2, 2), (3, 2), (4, 1)}
     assert look_around(mat,3,3)=={(4, 4), (2, 4), (3, 4), (4, 3), (4, 2), (2, 3), (2, 2), (3, 2)}

def test_look_around_out_of_range():
    mat=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    with pytest.raises(IndexError):
        look_around(mat,5,0)
    with pytest.raises(IndexError):
        look_around(mat,0,5)
    with pytest.raises(IndexError):
        look_around(mat,-1,0)
    with pytest.raises(IndexError):
        look_around(mat,0,-1)

#test hidden_mat method
def test_hidden_mat_one_mine():
    assert hidden_mat(2,[1])==[['x',1],[1,1]]
    assert hidden_mat(2,[2])==[[1,'x'],[1,1]]
    assert hidden_mat(2,[3])==[[1, 1], ['x', 1]]
    assert hidden_mat(2,[4])==[[1, 1], [1, 'x']]

def test_hidden_mat_corners_sides():
    assert hidden_mat(5,[1,3,5,11,15,21,23,25])==[['x', 2, 'x', 2, 'x'],
    [2, 3, 1, 3, 2], ['x', 1, 0, 1, 'x'], [2, 3, 1, 3, 2], ['x', 2, 'x', 2, 'x']]

def test_hidden_mat_inside_mines():
    assert hidden_mat(5,[7,9,13,17,19])==[[1, 1, 2, 1, 1],
    [1, 'x', 3, 'x', 1], [2, 3, 'x', 3, 2], [1, 'x', 3, 'x', 1], [1, 1, 2, 1, 1]]

def test_hidden_mat__mine_extra_test():
    assert hidden_mat(5,[i for i in range(1,26,2)])==[['x', 3, 'x', 3, 'x'],
                                                        [3, 'x', 4, 'x', 3], ['x', 4, 'x', 4, 'x'],
                                                        [3, 'x', 4, 'x', 3], ['x', 3, 'x', 3, 'x']]

def test_hidden_mat_out_of_range():
    assert(hidden_mat(2,[]))==[[0,0],[0,0]]
    with pytest.raises(IndexError):
        hidden_mat(2,[5])
    with pytest.raises(IndexError):
        hidden_mat(2,[0])

#test remaining_cells
def test_remaining_cells():

    assert remaining_cells([])==0
    assert remaining_cells([''])==0
    assert remaining_cells([[1,2],[3,4]])==0
    assert remaining_cells([[[1,2],[3,4]]])==0
    assert remaining_cells([' ','⬜'])==1
    assert remaining_cells([' ','    ⬜    '])==1
    assert remaining_cells(['⬜','    ⬜    '])==2
    assert remaining_cells([['⬜','123'],['123','    ⬜    ']])==2
