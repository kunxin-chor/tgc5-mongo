## Select database
    use notecards;

## Insert into collection
    db.notes.insert({
        "title":"My first note",
        "tags":"important,todo",
        "content":"The quick brown fox jumps over the lazy dog"
    });