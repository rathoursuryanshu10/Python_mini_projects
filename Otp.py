import random as rn
def generate_otp(length):
    min_value = 10 ** (length - 1)
    max_value = 10 ** length - 1
    return rn.randint(min_value, max_value)
otp_length = 6
otp = generate_otp(otp_length)
print("Generated OTP:", otp)
