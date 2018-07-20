from firebase_admin import credentials, db
import firebase_admin


cred = credentials.Certificate('./fir-pluspy-firebase-adminsdk-o2mkx-8e5154b252.json')
db_url = {
    'databaseURL': 'https://fir-pluspy.firebaseio.com/'
}
my_firebase_app = firebase_admin.initialize_app(cred, db_url)

users = db.reference('users')

#
# Get Back to dictionary
get_data = users.get()

#
# Get Back to OrderedDict
get_all_data_from_db_users = users.order_by_key().get()

if get_all_data_from_db_users is not None:
    #
    # Parse data from ***'get_all_data_from_db_users'***
    #
    for i in get_all_data_from_db_users.keys():
        for j in get_all_data_from_db_users[i]:

            print(get_all_data_from_db_users[i][j])

    #
    #  Delete data
    #
    temp = input('You want delete data from firebase (Y/N)')

    if temp == 'Y' or temp == 'y':
        for i in get_all_data_from_db_users.keys():
            for j in get_all_data_from_db_users[i]:

                users.delete()

else:
    print('You not have data in your firebase database')
