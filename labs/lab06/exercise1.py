
TotalCoffee = 3.50*2
TotalMuffin = 2.10*3
TotalWater  = 1.05*4
Subtotal    = float(TotalCoffee + TotalMuffin + TotalWater)
Tax         = float(0.06 * Subtotal)
Total       = float(Tax + Subtotal)

receipt = print (f"========== RECEIPT ==========\nItem\tPrice\tQty\tTotal\nCoffee\t$3.50\t2\t${round(TotalCoffee,2)}\nMuffin\t$2.10\t3\t${round(TotalMuffin,2)}\nWater\t$1.05\t4\t${TotalWater}\n------------------------------\nSubtotal\t${Subtotal}\nTax (6%)\t${Tax}\nTotal\t    ${Total}\n============================")
