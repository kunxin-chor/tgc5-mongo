All those are suppose to be in the Mongo Shell:

## Select a database
    use sample_airbnb

## Find entries
    db.listingsAndReviews.find({    
        }).limit(5).pretty();

## Find entries with critera
    db.listingsAndReviews.find({
        beds:5    
    }).limit(5).pretty();   


## Insert
    db.notecards.insert({
        'title':'My first note',
        'content':'The quick brown fox jumps over the lazy dog',
        'tags':'important'
    });