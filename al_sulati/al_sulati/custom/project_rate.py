import frappe

@frappe.whitelist()
def fetch_rate_values(sales_order=None):  # Make sales_order argument optional with a default value of None
    if sales_order:
        sales_order_items = frappe.get_all('Sales Order Item',
                                           filters={'parent': sales_order},
                                           fields=['custom_rate_selection', 'rate'])

        if sales_order_items:
            # Assuming you want to fetch values from the first item only
            return {
                'custom_rate_selection': sales_order_items[0].get('custom_rate_selection'),
                'rate': sales_order_items[0].get('rate')
            }

    return None