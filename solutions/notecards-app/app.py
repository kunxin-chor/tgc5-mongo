import data

# n = data.get_db()['notes'].find({
#     'tags':{
#         '$in':['important']
#     }
# })
# print(list(n))

x = data.get_notecards(tags=['important'])
print(list(x))