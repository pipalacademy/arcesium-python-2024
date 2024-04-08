
def test_function_name():
    import findfiles
    assert hasattr(
        findfiles, "findfiles"), "Could not find function findfiles"


def test_findfiles():
    from findfiles import findfiles
    assert set(findfiles(".", "test", ".txt")) == {'testdata1.txt',
                                                   'testdata2.txt',
                                                   'testdata3.txt',
                                                   'testdata4.txt',
                                                   'testdata5.txt',
                                                   'testdata6.txt'}
