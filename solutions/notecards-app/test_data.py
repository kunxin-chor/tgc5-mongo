import data

TEST_DB = "cardpad_test"
data.DB_NAME = TEST_DB


def setup_function():
    conn = data.get_db()
    # create mock data
    conn['notes'].insert_one({
        'title': 'The quick brown fox',
        'tags': ['important'],
        'content': 'The quick brown fox'
    })

    conn['notes'].insert_one({
        'title': 'The quick brown fox',
        'tags': ['important', 'test'],
        'content': 'The quick brown fox'
    })


# Drop the test database
def teardown_function():
    data.get_client().drop_database(TEST_DB)


def test_can_fetch_notes():
    notes = data.get_notecards()
    assert len(list(notes)) == 2


def test_can_find_by_tags():
    notes = list(data.get_notecards(tags=['important']))
    assert len(notes) == 2

    notes = list(data.get_notecards(tags=['test']))
    assert len(notes) == 1


def test_can_insert_notes():
    data.insert_notecard(
                            "Test add",
                            "This is the result of adding",
                            ["testing"]
                         )
    notes = list(data.get_notecards())

    assert len(notes) == 3
    assert notes[2]['title'] == 'Test add'
    assert notes[2]['content'] == "This is the result of adding"
    assert notes[2]['tags'] == ['testing']
