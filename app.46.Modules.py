import converters
from converters import kg_to_lbs
import utils
from utils import find_max
import ecommerce.shipping
from ecommerce.shipping import calc_shipping, calc_tax
from ecommerce import shipping

kg_to_lbs(100)

print(converters.kg_to_lbs(70))  # 155.55555555555554 from line 2
print(converters.lbs_to_kg(120))  # 54.0 from line 2

# utils.find_max()       from line 3
numbers = [10, 3, 6, 2, 5]
maximum = find_max(numbers)
print(maximum)  # 10 from line 4

ecommerce.shipping.calc_shipping()  # calc_shipping from line 5
ecommerce.shipping.calc_tax()  # calc_tax from line 5
calc_shipping()  # calc_shipping from line 6
calc_tax()  # calc_tax from line 6
shipping.calc_tax()  # calc_tax from line 7
shipping.calc_shipping()  # calc_shipping from line 7
shipping.cal_order()      # calc_order from line 7
