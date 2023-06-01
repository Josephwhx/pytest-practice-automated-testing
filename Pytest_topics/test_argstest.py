import pytest

def test_argtest01(CmdOpt):
    # print(CmdOpt.readline())
    assert CmdOpt.readline().index('Lab')