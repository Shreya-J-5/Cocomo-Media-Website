import re

with open(r'd:\Desktop\cocomo\cocomo_code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The brandLogos array looks like: const brandLogos = [ {name:"Brand", img:`data...`} ]
matches = re.findall(r'name:\s*["\']([^"\']+)["\']', content)
print("Brands found:", matches)
