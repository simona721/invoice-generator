#Product names and prices
product1_name, product1_price = 'Books', 50.95
product2_name, product2_price = 'Computer', 598.99
product3_name, product3_price = 'Monitor', 156.89

#Company imformation
company_name = "Somecompany"
company_address = "123 Random St."
company_city = "New York"

#Ending message
message = "Thanks for shopping with us!"

print("*" * 50)
print(f"\t\t{company_name}")
print(f"\t\t{company_address}")
print(f"\t\t{company_city}")

print('=' * 50)

print('\t{}\t\t${}'.format(product1_name.title(), product1_price))
print('\t{}\t${}'.format(product2_name.title(), product2_price))
print('\t{}\t\t${}'.format(product3_name.title(), product3_price))

print('=' * 50)

total = product1_price + product2_price + product3_price
print('\t\t\t${}'.format(total))

print('=' * 50)


print('\n\t{}\n'.format(message))

print('*' * 50)


