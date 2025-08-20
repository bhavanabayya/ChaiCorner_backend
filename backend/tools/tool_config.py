from langchain.agents import Tool

from backend.tools.cart.cart_tool import cart_tools

from backend.tools.customer.create_customer_tool import create_customer_tool
from backend.tools.customer.create_guest_tool import create_guest_tool
from backend.tools.customer.rename_customer_tool import rename_customer_tool
from backend.tools.customer.validate_customer_tool import validate_customer_tool

from backend.tools.product.products_tool import products_tool
from backend.tools.product.summary_tool import generate_summary

from backend.tools.quickbooks.create_invoice_tool import create_invoice_tool
from backend.tools.fedex.fedex_tool import create_fedex_shipment as fedex_tool

from backend.tools.payment.applepay.apple_pay_tool import apple_pay_tools
from backend.tools.payment.paypal.paypal_tool import get_paypal_tools, order_tools
from backend.tools.payment.trigger_payment import trigger_payment_tool

def get_all_tools() -> list[Tool]:
    return (
        cart_tools
        + [
            create_invoice_tool,
            products_tool,
            fedex_tool,
            create_customer_tool,
            create_guest_tool,
            rename_customer_tool,
            validate_customer_tool,
            generate_summary,
            trigger_payment_tool
        ]
        + order_tools
        # + apple_pay_tools
        # + get_paypal_tools()
    )
