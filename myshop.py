import streamlit as pd
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Ethnic Thread - Kurti Boutique",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Sample Data (Replace these image URLs with your own actual Kurti images or local paths)
KURTI_CATALOG = [
    {
        "id": 1,
        "name": "Classic Chikankari Kurti",
        "price": 1499,
        "category": "Daily Wear",
        "image": "https://unsplash.com",
        "description": "Handcrafted pure cotton Georgette Kurti with detailed shadow work.",
    },
    {
        "id": 2,
        "name": "Anarkali Festive Kurta",
        "price": 2499,
        "category": "Festive Wear",
        "image": "https://unsplash.com",
        "description": "Elegant rayon floor-length Anarkali with gold foil prints.",
    },
    {
        "id": 3,
        "name": "Indigo A-Line Kurti",
        "price": 1299,
        "category": "Office Wear",
        "image": "https://unsplash.com",
        "description": "Natural dyed indigo cotton A-line kurti with side pockets.",
    },
    {
        "id": 4,
        "name": "Pastel Silk Straight Kurta",
        "price": 1999,
        "category": "Festive Wear",
        "image": "https://unsplash.com",
        "description": "Tussar silk blend with subtle zari border embroidery.",
    },
]

# 3. Sidebar for Navigation & Filters
st.sidebar.title("👗 Ethnic Thread Boutique")
st.sidebar.write("Welcome! Find your perfect custom fit here.")

page = st.sidebar.radio("Go to:", ["Browse Catalog", "Place Custom Order"])

# Business Contact details
WHATSAPP_NUMBER = "916361120962"  # Replace with your actual WhatsApp business number (include country code)

# 4. Main App Pages
if page == "Browse Catalog":
    st.title("✨ Our Exclusive Kurti Collection")
    st.write("Browse our designs and click the button to chat with us to purchase.")

    # Filters
    categories = ["All"] + list(set([k["category"] for k in KURTI_CATALOG]))
    selected_cat = st.sidebar.selectbox("Filter by Category", categories)

    # Filtered Catalog
    filtered_catalog = (
        KURTI_CATALOG
        if selected_cat == "All"
        else [k for k in KURTI_CATALOG if k["category"] == selected_cat]
    )

    # Grid Display
    cols = st.columns(2)
    for i, kurti in enumerate(filtered_catalog):
        col = cols[i % 2]
        with col:
            st.image(kurti["image"], use_container_width=True)
            st.subheader(kurti["name"])
            st.write(f"**Price:** ₹{kurti['price']}")
            st.write(kurti["description"])

            # Create custom WhatsApp text link
            msg = f"Hi! I'm interested in buying the *{kurti['name']}* (Price: ₹{kurti['price']}). Is it available?"
            encoded_msg = msg.replace(" ", "%20")
            wa_link = f"https://wa.me{WHATSAPP_NUMBER}?text={encoded_msg}"

            st.markdown(
                f'<a href="{wa_link}" target="_blank" style="text-decoration:none;"><button style="background-color:#25D366; color:white; border:none; padding:8px 16px; border-radius:5px; cursor:pointer; font-weight:bold;">💬 Inquire on WhatsApp</button></a>',
                unsafe_allow_html=True,
            )
            st.write("---")

elif page == "Place Custom Order":
    st.title("🪡 Custom Stitching & Design Order")
    st.write("Have a unique idea or specific body measurements? Submit them below.")

    with st.form("custom_order_form", clear_on_submit=True):
        client_name = st.text_input("Your Full Name")
        client_email = st.text_input("Your Email Address")
        fabric_choice = st.selectbox(
            "Preferred Fabric", ["Cotton", "Rayon", "Silk Blend", "Georgette", "Linen"]
        )

        st.write("##### **Provide Your Measurements (Inches)**")
        col1, col2, col3 = st.columns(3)
        with col1:
            bust = st.number_input("Bust Size", min_value=20, max_value=60, value=36)
        with col2:
            waist = st.number_input("Waist Size", min_value=20, max_value=60, value=32)
        with col3:
            length = st.number_input(
                "Desired Kurti Length", min_value=25, max_value=60, value=42
            )

        design_notes = st.text_area(
            "Special Requests / Neckline & Sleeve Preferences"
        )

        submitted = st.form_submit_button("Submit Custom Request")

        if submitted:
            if not client_name or not client_email:
                st.error("Please fill in your name and email so we can reach you.")
            else:
                st.success(
                    f"Thank you, {client_name}! Your custom request has been captured."
                )

                # Format WhatsApp Text for custom order redirection
                custom_msg = (
                    f"Hi, I just submitted a custom Kurti design request!\n"
                    f"*Name:* {client_name}\n"
                    f"*Fabric:* {fabric_choice}\n"
                    f"*Bust/Waist/Length:* {bust}/{waist}/{length} inches\n"
                    f"*Notes:* {design_notes}"
                )
                encoded_custom_msg = custom_msg.replace(" ", "%20").replace(
                    "\n", "%0A"
                )
                custom_wa_link = (
                    f"https://wa.me{WHATSAPP_NUMBER}?text={encoded_custom_msg}"
                )

                st.markdown(
                    f'<br><a href="{custom_wa_link}" target="_blank" style="text-decoration:none;"><button style="background-color:#075E54; color:white; border:none; padding:12px 24px; border-radius:5px; cursor:pointer; font-weight:bold; width:100%;">🚀 Send Measurement Summary to Designer on WhatsApp</button></a>',
                    unsafe_allow_html=True,
                )
