import streamlit as st
import time

# 1. 페이지 설정
st.set_page_config(page_title="이천시 우수봉사자 조회", page_icon="❤️")

# 2. 보안된 명단 불러오기 (Secrets 사용)
@st.cache_data
def get_names():
    try:
        # 이따가 설정할 비밀 저장소에서 명단을 가져옵니다.
        raw_names = st.secrets["volunteer_list"]
        return set([n.strip() for n in raw_names.split(",")])
    except:
        return {"테스트"}

volunteers = get_names()

# 3. 디자인 (CSS)
st.markdown("""
    <style>
    .card { background: white; padding: 50px 20px; border-radius: 30px; text-align: center; border: 3px solid #ff4b4b; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
    .name-tag { font-size: 60px; font-weight: 900; color: #ff4b4b; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 4. 화면 구성
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.png", use_container_width=True)

st.markdown("<h3 style='text-align: center;'>2026 우수봉사자 조회</h3>", unsafe_allow_html=True)
name_input = st.text_input("", placeholder="성함을 입력하세요")

if name_input:
    name = name_input.strip()
    if name in volunteers:
        st.balloons()
        st.markdown(f'<div class="card"><div class="name-tag">{name}</div><h2>우수봉사자님 감사합니다!</h2><p>이천시를 따뜻하게 만들어주셔서 고맙습니다.</p></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="card" style="border-color:#ccc"><div class="name-tag" style="color:#777">{name}님</div><h2>내년에는 우수봉사자로 만나요!</h2><p>따뜻한 관심에 늘 감사드립니다.</p></div>', unsafe_allow_html=True)
