import pandas as pd
products = pd.read_csv('https://goo.gl/zWN5gg')
products.purchased = products.purchased.astype('category',                 ordered = True, 
                                                  categories = ['Online', 'In-store']
).cat.codes
print(products)