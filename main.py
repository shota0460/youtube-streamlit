import streamlit as st
from PIL import Image

#アプリケーションのタイトルを表示
st.title('streamlit超入門')

st.write('DataFrame')

img = Image.open('イメージ.jpg')

st.image(img, caption='jam')
#マークダウン記法を適応
"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""