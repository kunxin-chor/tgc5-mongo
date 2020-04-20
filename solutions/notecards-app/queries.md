## Select database
    use notecards;

## Insert into collection
    db.notes.insert({
        "title":"My first note",
        "tags":"important,todo",
        "content":"The quick brown fox jumps over the lazy dog"
    });

    

## Group by:
    db.listingsAndReviews.aggregate([
        {
            $group: {
                _id:'$property_type',
                count:{$sum:1}
            }
        }
    ])

#m_flix database

1. Count how many movies there are:

    db.movies.find({}).count()

2. Count how many movies there are before year 2000

    db.movies.find({year:{$lt:2000}}).count()

3. Show the first ten titles of movies produced in the USA:

    db.movies.find({
        countries:{
            $in:[
                'USA'
            ]
        }
    },{title:1, countries:1}).limit(10).pretty()

4. Show the first ten titles of movies produced ONLY in the USA:

    db.movies.find({
        countries:{
            $all:[
                'USA'
            ]
        }
    },{title:1, countries:1}).limit(10).pretty()

5. db.movies.find({
    countries:{
        $not:{
            $in:['USA']
        }
    }
   }, {title:1, countries:1}).limit(10).pretty()

6. db.movies.find({
    'awards.wins':{
        $gte:3
    }  
  }, {title:1, awards:1}).limit(10).pretty()


7. db.movies.find({
    'awards.nominations':{
        $gte:3,
    }
}, {title:1, awards:1}).limit(10).pretty()

8. db.movies.find({
    cast:'Tom Cruise'
}, {title:1, cast:1}).limit(10).pretty()

9. db.movies.find({
    directors:'Charles Chaplin'
}, {title:1, directors:1}).limit(10).pretty()