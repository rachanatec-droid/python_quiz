import streamlit as st

st.set_page_config(page_title="QuickBite Restaurant", page_icon="🍔", layout="wide")

# Initialize Menu Data
menu = {
    "Starters": {
        "Garlic Bread": 150,
        "Paneer Tikka": 250,
        "Chicken Wings": 300
    },
    "Main Course": {
        "Margherita Pizza": 450,
        "Veg Burger": 200,
        "Grilled Chicken": 550,
        "Pasta Alfredo": 400
    },
    "Beverages": {
        "Coke": 60,
        "Lemonade": 90,
        "Iced Tea": 120
    }
}

# Initialize Session State for Cart
if "cart" not in st.session_state:
    st.session_state.cart = {}

st.title("🍔 QuickBite Restaurant Simulator")
st.write("Browse our menu, add items to your cart, and place your order!")

# Layout: Two columns (Menu on left, Cart on right)
menu_col, cart_col = st.columns([2, 1])

with menu_col:
    st.header("📋 Menu")
    
    # Category selection tabs
    categories = list(menu.keys())
    tabs = st.tabs(categories)
    
    for i, category in enumerate(categories):
        with tabs[i]:
            st.subheader(category)
            for item, price in menu[category].items():
                col1, col2, col3 = st.columns([3, 2, 2])
                with col1:
                    st.write(f"**{item}**")
                with col2:
                    st.write(f"₹{price}")
                with col3:
                    if st.button("Add", key=f"add_{item}"):
                        if item in st.session_state.cart:
                            st.session_state.cart[item]["qty"] += 1
                        else:
                            st.session_state.cart[item] = {"price": price, "qty": 1}
                        st.rerun()

with cart_col:
    st.header("🛒 Your Cart")
    
    if not st.session_state.cart:
        st.info("Your cart is empty.")
    else:
        total_amount = 0
        for item, details in list(st.session_state.cart.items()):
            item_total = details["price"] * details["qty"]
            total_amount += item_total
            
            st.markdown(f"**{item}** (x{details['qty']})")
            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button("➕", key=f"inc_{item}"):
                    st.session_state.cart[item]["qty"] += 1
                    st.rerun()
            with c2:
                if st.button("➖", key=f"dec_{item}"):
                    st.session_state.cart[item]["qty"] -= 1
                    if st.session_state.cart[item]["qty"] <= 0:
                        del st.session_state.cart[item]
                    st.rerun()
            with c3:
                if st.button("🗑️", key=f"del_{item}"):
                    del st.session_state.cart[item]
                    st.rerun()
            st.write(f"Subtotal: ₹{item_total}")
            st.divider()
            
        st.subheader(f"Total: ₹{total_amount}")
        
        if st.button("Checkout & Place Order", type="primary"):
            st.success("🎉 Order placed successfully! Thank you for dining with us.")
            st.session_state.cart = {}
            st.balloons()

        if st.button("Clear Cart"):
            st.session_state.cart = {}
            st.rerun()
