import re


def normalize_phone(phone_number:str)->str:
    """
    Function return  normalize phone numbers in the format +380XXXXXXXXXX if fone number is not correct it returns an empty string
    
    Args:
        phone_number (str): The phone number string in various formats.
    Returns:
        str: The normalized phone number in '+380XXXXXXXXX' format,
             or an empty string if the input number is not valid
             according to the normalization and validation rules.
    """
    cleaned_phone = re.sub(r'[^\d+]', '', phone_number)
    if cleaned_phone.startswith('+'):
        normalized_phone = cleaned_phone
    elif cleaned_phone.startswith('380'):
        normalized_phone = '+' + cleaned_phone
    elif cleaned_phone.startswith('80'):
        normalized_phone = '+3' + cleaned_phone 
    else:
        normalized_phone = '+38' + cleaned_phone

    #check if the phone number is in the correct format
    if len(normalized_phone) != 13 or normalized_phone.count('+') > 1:
        # wrong phone number format
        normalized_phone =""

    return normalized_phone