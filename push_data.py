import firebase_admin
from firebase_admin import credentials, db


cred = credentials.Certificate('./fir-pluspy-firebase-adminsdk-o2mkx-8e5154b252.json')
db_url = db_url = {
    'databaseURL': 'https://fir-pluspy.firebaseio.com/'
}
my_firebase_app = firebase_admin.initialize_app(cred, db_url)

#
# include database from firebase
#
fb_db = db.reference('users')

new_data = fb_db.push({
    'name': 'Alex',
    'age': 12
})


temp = input('Do you want update data (y/n): ')

if temp == 'Y' or temp == 'y':
    new_data.update({
        'age': 20
    })
    print('data was been updated!')

else:
    print('Okay data is not updated!')
