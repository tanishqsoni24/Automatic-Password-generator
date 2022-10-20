import random
import string
a=string.ascii_lowercase
b=string.ascii_uppercase
c=string.punctuation
d=string.digits
i=(random.choice(a))+(random.choice(b))+(random.choice(c))+(random.choice(d))
random.shuffle(list(i))
temp=a+b+c+d
s=random.choices(temp,k=random.randint(4,5))
fn="".join(s)
print("Your Password is = ",i+fn)