file_name = "recipes.txt"

def catalog_reader(file_name):
    with open(file_name) as file_obj:
        result = {}
        for line in file_obj:
            product_name = line
            print(f"ingredient_name: {product_name}")
            goods = []
            for item in range(int(file_obj.readline())):
                good = file_obj.readline()
                goods.append(good.strip())
            result[product_name] = goods
            file_obj.readline()
        return result


catalog_reader(file_name)