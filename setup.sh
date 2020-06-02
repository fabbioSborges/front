mkdir -p ~ / .streamlit /
eco "\ 
[geral] \ n \ 
email = \" fabbioanderson@gmail.com \ "\ n \ 
"> ~ / .streamlit / credentials.toml
eco "\ 
[servidor] \ n \ 
headless = true \ n \ 
enableCORS = false \ n \ 
porta = $ PORT \ n \ 
"> ~ / .streamlit / config.toml