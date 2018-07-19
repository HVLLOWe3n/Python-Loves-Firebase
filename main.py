import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('./fir-pluspy-firebase-adminsdk-o2mkx-8e5154b252.json')
db_url = {
    'databaseURL': 'https://fir-pluspy.firebaseio.com'
}
default_app = firebase_admin.initialize_app(cred, db_url)

root = db.reference()
new_user = root.child('users').push({
    'name': 'Roman',
    'age': 20
})

new_user.update({
    'age': 21
})

roman = db.reference('users/{}'.format(new_user.key)).get()

print(type(roman))
print(roman)
