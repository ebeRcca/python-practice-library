# Challenge 2 – Webstore

# User input
registered = input("Is the user registered? (yes/no): ")
cart_items = int(input("How many items are in their shopping cart? "))
guest_login = input("Is the user using a guest login? (yes/no): ")
gift_card = input("Is the user purchasing a gift card? (yes/no): ")

# User can purchase
if registered == "yes" and cart_items > 0:
    can_purchase = True

# Exception: guest login AND buying a gift card
elif guest_login == "yes" and gift_card == "yes":
    can_purchase = True

# User can not purchase
else:
    can_purchase = False

print("Purchase allowed:", can_purchase)

# Assertion 1:
# registered = yes, cart_items = 2, guest_login = no, gift_card = no
# Expected result = True

# Assertion 2:
# registered = no, cart_items = 0, guest_login = yes, gift_card = yes
# Expected result = True  (guest gift card exception)

# Assertion 3:
#registered = yes, cart_items = 0, guest_login = no, gift_card = yes
# Expected result = False