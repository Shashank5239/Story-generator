import random
when =['a few year ago', 'Yesterday', 'Last night', 'On 12th november']
who =['a man','an old man','a child','a young man','a guy']
name = ['shiv','pankaj','himanshu','vipin','deepak']
residence =['India','Japan','America','England','Bhutan']
went =['cinema','university','seminar','school','hotel']
happened =['made a lot of friends.','eats a pizza.','found a key.','wrote a book.','solved a mystery.']

print(random.choice(when)+', ' + random.choice(who) + ' named ' + random.choice(name) + ' that lived in ' + 
random.choice(residence) + ', went to the ' +  random.choice(went) + ' and '  + random.choice(happened))
