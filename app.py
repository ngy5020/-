import streamlit as st
import time

# 1. 페이지 설정
st.set_page_config(page_title="이천시 우수봉사자 조회", page_icon="❤️")

# 2. 고대비(High Contrast) 디자인 적용
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');
    
    html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
    
    /* 배경은 깨끗한 흰색 */
    .stApp { background-color: #ffffff; }

    /* 카드 스타일 */
    .card {
        background: white;
        padding: 50px 20px;
        border-radius: 30px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.15); /* 그림자 더 진하게 */
    }

    /* 우수봉사자 당첨 카드 (빨간색 테두리) */
    .success-card { border: 4px solid #e74c3c; }
    .success-name { font-size: 65px; font-weight: 900; color: #e74c3c; margin-bottom: 10px; }
    
    /* 명단에 없을 때 카드 (진한 남색/검정 테두리) */
    .fail-card { border: 4px solid #2c3e50; }
    .fail-name { font-size: 55px; font-weight: 900; color: #2c3e50; margin-bottom: 10px; }

    /* 메시지 글자색 수정 (흐린 회색 -> 진한 검정) */
    .main-msg { 
        font-size: 32px; 
        font-weight: 800; 
        color: #111111; /* 아주 진한 검정 */
        margin-bottom: 20px; 
        line-height: 1.3;
    }
    
    .sub-msg { 
        font-size: 20px; 
        font-weight: 600; 
        color: #333333; /* 명확한 다크 그레이 */
        line-height: 1.6; 
    }

    /* 애니메이션 */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .card { animation: fadeInUp 0.5s ease-out; }
    </style>
    """, unsafe_allow_html=True)

# 3. 보안된 명단 로드 (Secrets 사용)
@st.cache_data
def load_volunteers():
    try:
        raw_data = st.secrets["volunteer_list"]
        return set([name.strip() for name in raw_data.split(",")])
    except:
        return {"홍길동", "이천시", "자원봉사"}

volunteers = load_volunteers()

# 4. 화면 레이아웃
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h2 style='text-align: center; color: #e74c3c;'>❤️ 이천시자원봉사센터</h2>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: #333; margin-top: -10px;'>2024 우수봉사자 명예의 전당</h4>", unsafe_allow_html=True)

# 검색창 (글씨 크기 키움)
name_input = st.text_input("", placeholder="성함을 입력하고 엔터를 치세요")

if name_input:
    name = name_input.strip()
    if name in volunteers:
        st.balloons()
        st.markdown(f"""
            <div class="card success-card">
                <p style="color: #e74c3c; font-weight: 900; font-size: 20px; letter-spacing: 2px;">CERTIFICATE</p>
                <div class="success-name">{name}</div>
                <div class="main-msg">우수봉사자님 감사합니다!</div>
                <div class="sub-msg">당신의 헌신적인 활동이<br>이천시를 더 행복하게 만들었습니다.</div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="card fail-card">
                <div class="fail-name">{name}님</div>
                <div class="main-msg">내년에는 우수봉사자로 만나요!</div>
                <div class="sub-msg">보내주신 따뜻한 마음에 감사드리며<br>앞으로의 활동을 늘 응원하겠습니다.</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #555; font-size: 13px; margin-top: 50px; font-weight:bold;'>© (재)이천시자원봉사센터</p>", unsafe_allow_html=True)
