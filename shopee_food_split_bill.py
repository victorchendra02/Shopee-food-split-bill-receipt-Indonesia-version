# Shopee food split bill
class ShopeeFoodSplitBillReceipt:
    def under_limit(self, discount_amount: float, maks: int, prices: list, names: list):
        discount_amount = discount_amount / 100

        discount_price = []
        for x in prices:
            discount_price.append(int(discount_amount * x))

        price_after_discount = []
        for index, each_item in list(enumerate(prices)):
            price_after_discount.append(each_item - discount_price[index])

        total_price = sum(prices)
        total_discount = sum(discount_price)
        total_price_after_discount = sum(price_after_discount)

        # gui text
        print(f"{'':_^98s}")
        print(f" No| {'Nama Makanan':^30s} | {'Harga normal':^18s} | {'Discount':^16s} | {'Harga di-discount':^19} ")
        print(f"___|_{'':_^30s}_|_{'':_^18s}_|_{'':_^16s}_|_{'':_^19s}_")

        for y, each_price in list(enumerate(prices)):
            print(f" {y + 1}.| {names[y]:<30s} | Rp{'{:,}'.format(each_price):>16s} | Rp{'{:,}'.format(discount_price[y]):>14s} | Rp{'{:,}'.format(price_after_discount[y]):>17s} ")
            # print(f" {y + 1}.| {names[y]:<30s} | Rp{'{:,}'.format(each_price):>16s} | Rp{'{:,}'.format(discount_price[y]):>14s} | Rp{'{:,}'.format(price_after_discount[y]):>17s} ")

        print(f"{'':_^98s}")
        print(f"{'': ^36s}| Rp{'{:,}'.format(total_price):>16s} | Rp{'{:,}'.format(total_discount):>14s} | Rp{'{:,}'.format(total_price_after_discount):>17s}")
        print(f"{'': ^36s}{'':_^62s}")

        print(f"  Summary: ")
        print(f"   Subtotal         = Rp {'{:,}'.format(total_price):>8s}                      Discount               =  {int(discount_amount * 100)}%")
        print(f"   Discount earned  = Rp {'{:,}'.format(total_discount):>8s}                      Maximum discount       =  Rp    {'{:,}'.format(maks)}")
        print(f"   Total            = Rp {'{:,}'.format(total_price_after_discount):>8s}                      Earn maximum discount  =  Rp    {'{:,}'.format(self.minimum_shopping_to_get_maximum_discount(discount_amount, maks))}")
        print()
        print(f"  Note: ")
        print(f"   *Total biaya diatas belum termasuk biaya ongkir dan\n"
              f"     biaya layanan lainnya.")

    def over_limit(self, discount_amount: float, maks: int, prices: list, names: list):
        discount_amount = discount_amount / 100

        discount_price = int(maks / len(prices))

        price_after_discount = []
        for index, each_item in list(enumerate(prices)):
            price_after_discount.append(each_item - discount_price)

        total_price = sum(prices)
        total_discount = maks
        total_price_after_discount = int(sum(price_after_discount))

        # gui text
        print(f"{'':_^98s}")
        print(f" No| {'Nama Makanan':^30s} | {'Harga normal':^18s} | {'Discount':^16s} | {'Harga di-discount':^19} ")
        print(f"___|_{'':_^30s}_|_{'':_^18s}_|_{'':_^16s}_|_{'':_^19s}_")

        for y, each_price in list(enumerate(prices)):
            print(f" {y + 1}.| {names[y]:<30s} | Rp{'{:,}'.format(each_price):>16s} | Rp{'{:,}'.format(discount_price):>14s} | Rp{'{:,}'.format(price_after_discount[y]):>17s} ")
            # print(f" {y + 1}.| {names[y]:<30s} | Rp{'{:,}'.format(each_price):>16s} | Rp{'{:,}'.format(discount_price[y]):>14s} | Rp{'{:,}'.format(price_after_discount[y]):>17s} ")

        print(f"{'':_^98s}")
        print(
            f"{'': ^36s}| Rp{'{:,}'.format(total_price):>16s} | Rp{'{:,}'.format(total_discount):>14s} | Rp{'{:,}'.format(total_price_after_discount):>17s}")
        print(f"{'': ^36s}{'':_^62s}")

        print(f"  Summary: ")
        print(f"   Subtotal         = Rp {'{:,}'.format(total_price):>8s}                      Discount               =  {int(discount_amount * 100)}%")
        print(f"   Discount earned  = Rp {'{:,}'.format(total_discount):>8s}                      Maximum discount       =  Rp    {'{:,}'.format(maks)}")
        print(f"   Total            = Rp {'{:,}'.format(total_price_after_discount):>8s}                      Earn maximum discount  =  Rp    {'{:,}'.format(self.minimum_shopping_to_get_maximum_discount(discount_amount, maks))}")
        print()
        print(f"  Note: ")
        print(f"   *Total biaya diatas belum termasuk biaya ongkir dan\n"
              f"     biaya layanan lainnya.")

    def minimum_shopping_to_get_maximum_discount(self, discount_amount: float, maks: int):
        return int(maks / discount_amount)

    def is_over_the_discount_limit(self, discount_amount: float, maks: int, total_price: list):
        discount_amount = discount_amount / 100
        a = self.minimum_shopping_to_get_maximum_discount(discount_amount, maks)

        total_price = int(sum(total_price))
        if a >= total_price:
            return "under limit"
        else:
            return "over limit"

    def run(self):
        print()
        diskon = float(input("Discount (%)         : "))
        print("Jika tidak ada maksimal diskon, masukkan '-1'")
        maks = int(input("Maksimum diskon (Rp) : "))
        names = list(map(str, input("Jenis-jeins makanan: ").split(", ")))
        prices = list(map(int, input("Harga per item: ").split(",")))
        print()

        status = self.is_over_the_discount_limit(diskon, maks, prices)
        # with discount limitation
        if maks > 0:
            if status == "under limit":
                return self.under_limit(diskon, maks, prices, names)
            else:
                return self.over_limit(diskon, maks, prices, names)
        # without discount limitation
        else:
            return self.under_limit(diskon, maks, prices, names)


if __name__ == '__main__':
    split_bill = ShopeeFoodSplitBillReceipt()
    split_bill.run()
