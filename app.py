import streamlit as st

st.set_page_config(
    page_title="Nellis Phone Tool",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Nellis Phone Flipping Tool")
st.caption("Quick helper for finding better phone lots on Nellis Auction")

st.markdown("---")

# ========== BEST SEARCH LINKS ==========
st.subheader("1. Best Search Links")
st.write("Tap these to open the best filtered searches:")

st.markdown("""
**iPhones**  
[Open iPhone Search](https://www.nellisauction.com/search?q=iphone&Taxonomy+Level+1=Electronics&Taxonomy+Level+2=Cell+Phones%2C+Chargers+%26+Accessories&sortBy=current_price_asc)

**Samsung Galaxy**  
[Open Samsung Search](https://www.nellisauction.com/search?q=samsung+galaxy&Taxonomy+Level+1=Electronics&Taxonomy+Level+2=Cell+Phones%2C+Chargers+%26+Accessories&sortBy=current_price_asc)

**Google Pixel**  
[Open Pixel Search](https://www.nellisauction.com/search?q=pixel&Taxonomy+Level+1=Electronics&Taxonomy+Level+2=Cell+Phones%2C+Chargers+%26+Accessories&sortBy=current_price_asc)
""")

st.markdown("---")

# ========== MARGIN CALCULATOR ==========
st.subheader("2. Cost Calculator")
st.write("Enter the current bid to see your real cost after the 15% buyer’s premium:")

current_bid = st.number_input("Current Bid ($)", min_value=0.0, value=50.0, step=1.0)

buyers_premium = current_bid * 0.15
total_cost = current_bid + buyers_premium

col1, col2 = st.columns(2)
col1.metric("Buyer’s Premium (15%)", f"${buyers_premium:.2f}")
col2.metric("Total Cost", f"${total_cost:.2f}")

st.markdown("---")

# ========== WHAT TO AVOID ==========
st.subheader("3. What to Avoid")
st.write("Skip any lot that has these words in the title or notes:")

st.markdown("""
- Locked / Carrier Locked  
- Password / Has a password  
- Parts Only / For Parts  
- Not Functional  
- Major Damage  
- Untested  
- Missing Parts  
""")

st.success("Prefer lots that say **Unlocked** or have clean notes.")

st.markdown("---")

# ========== QUICK NOTES ==========
st.subheader("4. Quick Notes")
st.write("Jot down any lots you’re watching:")

notes = st.text_area("Your notes", height=120, placeholder="Example: iPhone 14 Pro 128GB - $187 - looks clean - ends in 3 hours")

if notes:
    st.info("Notes saved on this device for now (they will clear if you refresh).")

st.markdown("---")
st.caption("First version • We can improve this later")
