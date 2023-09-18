def farenheit_to_celcius(f):
    result = (f-32) * 5/9
    print("{}°C".format(result))

def celcius_to_farenheit(c):
    result = c * (9/5) + 32
    print("{}K".format(result))

farenheit_to_celcius(32)
celcius_to_farenheit(0)