mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
base='light'\n\
primaryColor='#832d2d'\n\
backgroundColor='#d2bebe'\n\
secondaryBackgroundColor='#d5d8dc'\n\
" > ~/.streamlit/config.toml
