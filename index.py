# task 1

def update_profile(user_id, **kwargs):
    return {
        'updated_fields': kwargs,
        'id': user_id
    }

# task 2

def get_domains(emails):
    return [email.split('@')[1] for email in emails]

# task 3

def filter_target_audience(users):
    return [user for user in users if user['age'] >= 18 and user['is_premium'] == True]

# task 4

def build_response(status_code, *errors, **payload):
    return {
        'status': status_code,
        'errors': errors,
        'data': payload
    }

# task 5

def calculate_total_spent(transactions):
    return sum(transaction.get('amount', 0) for transaction in transactions)