## Show all databases
    show databases

## Create a new databases
    use my_new_db

* The `db` variable will refer to the database you are using
* You won't see the new database when you type `show databases` until you insert a document into it

## Create a new collection

* Just insert a new document into the collection

    db['users'].insert({
        'name':'Tan Ah Kow'
    })

    db.users.insert({
        'name':'Julian Lee
    })

## Know which database you are using
    db


# FIND

Find is similair to `SELECT .. FROM table` in MySQL. 

## To refer to a collection
Generally, it's
    db.nameOfCollection

## To find every documents in a collection
    db.listingsAndReviews.find()

Assuming that we are using the sample_mflix listingsAndReviews collection.

## Limit number of results
    db.listingsAndReviews.find().limit(5);

## Prettify
    db.listingsAndReviews.find().limit(5).pretty();

## Select which properties to show? (or attributes)
Or how do we a `SELECT <col1>,<col2> FROM <table>`?
The concept is known as projection

    db.listingsAndReviews.find({
        // empty objects mean to find everything
    }, {name:1, 
        listing_url:1,
         description:1
    }).limit(5).pretty()

### Select from listingsAndReviews and only show the name, number of bedrooms and bathrooms 
    db.listingsAndReviews.find({

    }, {
        name:1,
        bedrooms:1,
        bathrooms:1
    }).limit(3).pretty()

## To filter, we add in the critera to the first argument

### Matching exact

Find all listings that have 2 bedrooms:

    db.listingsAndReviews.find({
        bedrooms:2
    }, {name:1, bedrooms:1}).limit(10).pretty()


Find all listings that has property_type of apartments

    db.listingsAndReviews.find({
        property_type: 'Apartment'
    }, {name:1, property_type:1, bedrooms:1}).limit(10).pretty()

Find all listings that are apartments and have 2 bedrooms

    db.listingsAndReviews.find({
        property_type: 'Apartment',
        bedrooms: 2
    }, {name:1, property_type:1, bedrooms:1} ).limit(10).pretty()

Find all the listing with two bathrooms and is a private room

    db.listingsAndReviews.find({
        bathrooms:2,
        room_type:'Private room'
    }, {name:1, room_type:1, bathsrooms:1}).limit(10).pretty()

### Find listings by a substring

Similiar to `SELECT * FROM emplyoees WHERE jobTitle LIKE '%sales%'

    db.listingsAndReviews.find({
        name: {$regex: 'nice room', $options:'i'}
    }, {name:1}).limit(10).pretty();


    db.listingsAndReviews.find({
        name: {$regex: 'artistic', $options:'i'}
    }, {name:1}).limit(10).pretty();

### Critera with a range

Similiar to `SELECT * FROM studetns WHERE score >= 50 AND score <=30`

    Find all listings that have more than 2 bedrooms
    db.listingsAndReviews.find({
        bedrooms: {
            $gt: 2
        }
    }, {name:1, bedrooms:1}).limit(10).pretty()

* We use `gt` for greater than, `gte` for greater than or equal
* We use `lt` for lesser than, `lte` for lesser than or equal

    Find all listings that have 2 or 3 bedrooms:

    db.listingsAndReviews.find({
        bedrooms: {
            $gte:2,
            $lte:3
        }
    }, {name:1, bedrooms:1}).limit(10).pretty()

# Find all listings that have 2 or 3 bedrooms and have 2 or more bathrooms

    db.listingsAndReviews.find({
        bedrooms: {
            $gte:2,
            $lte:3
        },
        bathrooms:{
            $gte:2
        }
    }, {name:1, bedrooms:1, bathrooms:1}).limit(10).pretty()

### Find all listings that are in Canada

    db.listingsAndReviews.find({
        'address.country': 'Canada'
    }, {name:1, 'address.country':1).limit(10).pretty()

### Find all listings that are in Canada, and display their lat lng
    db.listingsAndReviews.find({
        'address.country': 'Canada'
    }, {name:1, 'address.country':1, 'address.location.coordinates':1}).limit(10).pretty()

### Find all listings that have the host's total listing count greater than 2, and display the name and the total listing counted
    db.listingsAndReviews.find({
        'host.host_total_listings_count':{
            $gt:2
        }
    }, {name:1, 'host.host_total_listings_count':1}).limit(10).pretty()

### Find by an item in an array


    db.listingsAndReviews.find({
        amenities:'Hot tub' 
    }, {name:1, amenities:1}).limit(5).pretty()


    Find listings that have wifi and laptop friendly workspace

    db.listingsAndReviews.find({
        amenities: {
            $all: ['Wifi', 'Laptop friendly workspace']
        }
    }, {name:1, amenities:1}).limit(5).pretty()

    Find listings that have a doorman OR that the host greets you
    db.listingsAndReviews.find({
        amenities:{
            $in:['Doorman', 'Host greets you']
        }
    }, {name:1, amenities:1}).limit(5).pretty()

## GROUP by
    db.listingsAndReviews.aggregate([
        {$group:{
            _id:'$property_type',
            count:{
                $sum:1
            }
        }}
    ]);

# HOW TO CREATE/UPDATE AND DELECT documents

* Document exists in collections
* Collections exist in database

1. Use the database (even if we haven't created it yet)
2. Insert a document into a collection
3. Done

## Create the animal-shelter database

Use the new database even though it doesn't exists
    use animal_shelter

Inserting an animal (this will also create the collection if the collection is empty or doesn't exist)
    db.animals.insert({
         "_id":ObjectId("5e9e5cc77fb3bf5da545666a"), // optional
        "name":"Biscuit",
        "breed":"Golden Retriever"
    })

Update an animal by replacing it with a new object (will replace the entire document)
    db.animals.update({
        // the matching critera
        _id:ObjectId("5e9e5cc77fb3bf5da545666a")
    }, {
        "breed":"German Shepherd",
        "checkups":[
            {
                "_id":ObjectId(),
                "vet":"Dr. Chua",
                "diagnosis":"Need to rest the hip more",
                "date":new Date("2020-04-21")
            }
        ]
    })

Update an animal piecemeal (only replacing what is specified). Example: to change breed to German 
    db.animals.update({
        // the matching critera
        _id:ObjectId("5e9e5cc77fb3bf5da545666a")
    }, {
        $set: {
            "breed":"German Shepherd"
        }
    })


Delete
    db.animals.remove({
        _id:ObjectId("5e9e5cc77fb3bf5da545666a")
    })