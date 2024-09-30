import streamlit as st
import pandas as pd
from st_btn_select import st_btn_select

def wide_space_default():
st.set_page_config(layout="wide")

wide_space_default()

# Title and ID
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Add three line breaks
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Add three line breaks


# Inject Bootstrap CSS
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# Custom CSS to increase the size of the navigation bar
custom_css = """
<style>
    .navbar {
        height: 80px;  /* Adjust the height as needed */
        margin-top: 20px;  /* Adjust the top margin to position the navbar lower */
    }
    .navbar-brand, .nav-link {
        font-size: 24px;  /* Adjust the font size as needed */
    }
    .section {
        padding-top: 100px;  /* Adjust for navbar height */
        margin-top: -100px;  /* Adjust for navbar height */
    }
    .navbar-brand img {
        height: 50px;  /* Adjust the height of the image as needed */
        margin-right: 10px;  /* Adjust the space between the image and the text */
        border-radius: 50%;  /* Make the image circular */
    }
</style>
"""

# Inject the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Navigation bar HTML with image and link to Home section
st.markdown("""
<nav class="navbar navbar-expand-lg navbar-dark" style="background-color: black;">
  <a class="navbar-brand" href="#">
    <img src="https://raw.githubusercontent.com/manubindra/TrueRender3D/main/TRUE%20RENDER%20LOGO%20(1).png" alt="Logo">  <!-- Replace with your image URL -->
    TrueRender 3D
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ml-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#home">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#gallery">Gallery</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#about">About</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#pricing">Pricing</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;font-weight: bold; color: black;'>TrueRender 3D - I.D - Aishwarya Jadhav</h2>", unsafe_allow_html=True)


# JavaScript for smooth scrolling
st.markdown("""
<script>
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
</script>
""", unsafe_allow_html=True)

st.markdown('<div id="home" class="section"></div>', unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;font-weight: bold; color: black;'>Welcome to TrueRender 3D</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: left;font-weight: bold; color: black;'>OUR AIM</h2>", unsafe_allow_html=True)
st.write(
        "Our aim is to transform spaces into personalized havens that reflect our clients' unique tastes and lifestyles. "
        "Through our website, we strive to showcase our design expertise, inspire creativity, and provide a seamless experience "
        "for potential clients to explore our services and initiate their design journey with us. We are committed to delivering "
        "exceptional design solutions that enhance the functionality and aesthetics of every space we touch, building lasting "
        "relationships based on trust, innovation, and excellence."
    )
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Add three line breaks
st.markdown("<h2 style='text-align: left;font-weight: bold; color: black;'>WHAT WE DO BEST!</h2>", unsafe_allow_html=True)
st.write(
        "At TrueRender 3D, we specialize in creating beautiful, functional spaces that reflect the "
        "unique tastes and lifestyles of our clients. Our comprehensive range of interior design services "
        "ensures that every project, big or small, receives the attention to detail and creativity it "
        "deserves. Here’s how we can help transform your space: "
    )
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Add three line breaks
st.markdown("<h2 style='text-align: left;font-weight: bold; color: black;'>TOOLS WE USE</h2>", unsafe_allow_html=True)
image_urls = [
        "https://pbs.twimg.com/profile_images/1328769637643812864/1pa8mRKe.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Adobe_Photoshop_CC_icon.svg/512px-Adobe_Photoshop_CC_icon.svg.png",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQagU12wCXT3Nlj4IlrDI0q_wv0w6xnm6TzWQ&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLFfeF-ODNgOa0DL9uzxLinBUj_Me7Ho_TVQ&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcU_d-agfQE38Jxj_tCmk9q1_SXoQuchm21w&s"
    ]
    # Create a row with 5 columns
cols = st.columns(10)
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Add three line breaks
# Display each image in its respective column
for col, image_url in zip(cols, image_urls):
        col.image(image_url, use_column_width=True)

cols = st.columns(10)
image_url1 = [
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0h9Ms_n5xkJP9ZzL3q8dZDPztiPsy_ztU8w&s',
        'https://findvectorlogo.com/wp-content/uploads/2022/04/enscape-vector-logo-2022.png',
        'https://tse1.mm.bing.net/th/id/OIP.bKAgJy25H1l6ivvF9Ov2gQHaJZ?rs=1&pid=ImgDetMain'
    ]
    # Display each image in its respective column
for col, image_url in zip(cols, image_url1):
        col.image(image_url, use_column_width=True)



    # Retrieve the environment variable
st.markdown('<div id="gallery" class="section"></div>', unsafe_allow_html=True)

html_content = f"""
    <h2 style='text-align: left;font-weight: bold; color: black;'>Gallery</h2>
    <p>Explore our Gallery</a> to see a collection of our completed projects. Our gallery showcases a variety of design styles and spaces, providing a visual representation of our expertise and creativity.</p>
    """
st.markdown(html_content, unsafe_allow_html=True)


st.markdown('<div id="gallery" class="section"></div>', unsafe_allow_html=True)
st.markdown("<h2 class='centered-subheader'>Gallery</h2>", unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["Interiors", "Exteriors", "Concept"])
with tab1:
        st.header("Interiors")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        st.write("This is the Interiors section.")
with tab2:
        st.header("Exteriors")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        st.write("This is the Exteriors section.")
with tab3:
        st.header("Concept")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
        st.write("This is the Concept section.")


st.markdown('<div id="about" class="section"></div>', unsafe_allow_html=True)
st.markdown("<h2 class='centered-subheader'>About Me</h2>", unsafe_allow_html=True)
st.write('About Me content goes here.')

st.markdown('<div id="pricing" class="section"></div>', unsafe_allow_html=True)
st.markdown("<h2 class='centered-subheader'>Pricing</h2>", unsafe_allow_html=True)
pricing_data = {
        "Plan": ["Basic", "Standard", "Premium"],
        "Price": ["$10/month", "$20/month", "$30/month"],
        "Features": [
            "Feature 1, Feature 2",
            "Feature 1, Feature 2, Feature 3",
            "Feature 1, Feature 2, Feature 3, Feature 4"
        ]
    }
df_pricing = pd.DataFrame(pricing_data)
st.write(df_pricing.to_html(index=False), unsafe_allow_html=True)
