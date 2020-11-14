import time
import sys
import requests
import time

class BestBuy():
    def __init__(self, api_key, postal_code, product_sku):
        self.api_key = api_key
        self.postal_code = postal_code
        self.product_sku = product_sku
    
    def is_product_available(self):
        """
            This function will return if a store is carrying a product near you
            :api_key
            :product_sku
            :postal_code

            If there is a store near the given postal code, the function will return data that is structered as the following
            
            [
                {low_stock: False, address: "123 south st"},
                {low_stock: True, address: "516 main st"},
                {low_stock: False, address: "117 chuck e dr"},
                {low_stock: True, address: "611 turnip ave"},
            ]
            Else the function returns False
        """
        link = "https://api.bestbuy.com/v1/products/{0}/stores.json?postalCode={1}&apiKey={2}".format(self.product_sku, self.postal_code, self.api_key)

        data = requests.get(link).json()
        if not data['ispuEligible']:
            return False

        store_list = []
        stores = data['stores']
        for i in stores:
            storeObj = {
                # This will be a true or false value
                "low_stock": i['lowStock']
                "address": i['address']
            }
            
            store_list.append(storeObj)
        
        return store_list

        
if __name__ == "__main__":  
    # BOOL
    API_KEY=sys.argv[0]
    POSTAL_CODE=sys.argv[1]
    PRODUCT_SKU = sys.argv[2]
    
    isAvailable = BestBuy(API_KEY, POSTAL_CODE, PRODUCT_SKU).is_product_available()

    if isAvailable:
        # Handle email or sos here
        print(isAvailable)
    else:
        print("{0} is not available near {1}".format(PRODUCT_SKU, POSTAL_CODE))
    



