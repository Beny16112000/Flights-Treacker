from ..models import Keys
from .. import db
import secrets


# Create API key for access to the API


class Key:

    def create(self):
        create_key = secrets.token_hex(16)
        save = Keys(key=create_key)
        db.session.add(save)
        db.session.commit()
        return create_key

    
    def check(self, key):
        check_key = Keys.query.filter_by(key=key).first()
        if check_key:
            return 'Success'
        else:
            return None


    def key_error(self):
        return {
            'message': 'The key is incorrect'
        }


