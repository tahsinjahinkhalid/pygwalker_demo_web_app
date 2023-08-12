import streamlit as st
import streamlit.components.v1 as components
import pygwalker as pyg
import pandas as pd
import warnings

st.set_page_config(layout="wide",
                   initial_sidebar_state="expanded",
                   page_title="PyGWalker Demo",
                   page_icon=":alembic:")

warnings.filterwarnings("ignore")


# load data function
@st.cache_data
def load_data(url):
    """
    Load Data as a Pandas Dataframe
    Note: we use Pandas and not polars
    Since PyGWalker has not adjusted to Polars...yet
    :param url: the csv file URL
    :return: Pandas dataframe of the CSV
    """
    df = pd.read_csv(url)
    return df


def load_config(file_path):
    """
    :param file_path: the config.json file
    :return: config_str: the file read as a string variable
    """
    with open(file_path, 'r') as config_file:
        config_str = config_file.read()
    return config_str


st.markdown("""
# :alembic: PyGWalker Data Visualisation
### Web App (Demo)
### 💻 By: [Tahsin Jahin Khalid](https://tahsinjahinkhalid.github.io/)
""")
st.subheader('A demonstration of the [PyGWalker](https://docs.kanaries.net/pygwalker) Python library')

# add file upload option to sidebar
# force upload to CSV (cleaned preferably)
with st.sidebar:
    # st.write("Upload (Preprocessed/Cleaned) CSV File")
    uploaded_csv = st.file_uploader(label="Upload CSV File.",
                                    accept_multiple_files=False,
                                    type=["csv"])

if uploaded_csv is not None:
    data = load_data(uploaded_csv)
    config = load_config('config.json')

    # initiate pyg
    pyg_html = pyg.walk(data,
                        env='Streamlit',
                        hideDataSourceConfig=True,
                        spec=config,
                        themeKey="vega",
                        dark="media",
                        return_html=True)

    components.html(pyg_html,
                    height=1000,
                    scrolling=True)
else:
    # load a dummy data frame
    st.write("The Demo will start as soon as you upload a CSV file.")
