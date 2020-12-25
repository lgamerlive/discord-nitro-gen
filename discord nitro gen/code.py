import random, string, requests
f=open("Vaild Nitro.txt", "w", encoding='utf-8')

while True:
  code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
  r = requests.get("https://discordapp.com/api/v7/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
  if r.status_code == 200:
    print(f"Vaild nitro code > discord.gift/{code}")
    f.write("discord.gift/{code}\n")
  else:
      print(f"Invaild nitro code > discord.gift/{code}") 