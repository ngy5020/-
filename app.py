import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="우수봉사자 조회", page_icon="✨", layout="centered")

# [강력 수정] 모든 스타일 요소를 무조건 새까만 검은색(#000000)으로 강제 적용
st.markdown("""
    <style>
    /* 1. 메인 제목 글씨 (제일 위) */
    .main-title {
        text-align: center !important; 
        color: #000000 !important; 
        font-size: 32px !important; 
        font-weight: 900 !important;
        margin-top: 10px !important;
        margin-bottom: 30px !important;
    }
    
    /* 2. 입력창 바로 위 안내 문구 ("봉사자 성명을 입력해 주세요") */
    .stTextInput label p {
        color: #000000 !important;
        font-size: 20px !important;
        font-weight: 800 !important;
    }
    
    /* 3. 입력창 안에 사용자가 타이핑하는 글씨 */
    .stTextInput input { 
        font-size: 20px !important; 
        color: #000000 !important; 
        font-weight: 900 !important; 
        background-color: #ffffff !important;
        border: 3px solid #000000 !important; /* 테두리도 새까맣고 두껍게 */
        border-radius: 10px !important;
    }
    
    /* 결과 카드 스타일 */
    .result-card { 
        background-color: #ffffff !important; 
        padding: 30px !important; 
        border-radius: 15px !important; 
        box-shadow: 0 6px 15px rgba(0,0,0,0.2) !important; 
        margin-top: 30px !important; 
        margin-bottom: 40px !important;
        text-align: center !important; 
    }
    
    /* 결과 카드 내부 글씨들 */
    .success-text { 
        color: #0b5115 !important; /* 아주 진한 초록색 */
        font-size: 22px !important; 
        font-weight: 900 !important; 
        line-height: 1.7 !important; 
    }
    .fail-text { 
        color: #000000 !important; /* 새까만 검은색 */
        font-size: 20px !important; 
        font-weight: 800 !important; 
        line-height: 1.7 !important; 
    }
    </style>
""", unsafe_allow_html=True)

# [순서 1] '우수봉사자 조회' 제목이 무조건 맨 위에 진하게 나옵니다.
st.markdown("<h1 class='main-title'>🌟 우수봉사자 명단 조회 🌟</h1>", unsafe_allow_html=True)

# 2. Secrets 명단 로드 및 쪼개기
volunteer_raw = st.secrets.get("volunteer_list", "")
volunteer_raw = volunteer_raw.replace("\n", "").replace(" ", "")
volunteer_list = [name.strip() for name in volunteer_raw.split(",") if name.strip()]

# [순서 2] 성명 입력창 (글씨 완전 선명하게 교정)
search_name = st.text_input("봉사자 성명을 입력해 주세요:")

# [순서 3] 결과 확인 카드
if search_name:
    name = search_name.strip()
    alt_name = "I" + name[1:] if name.startswith("이") else name
    
    if (name in volunteer_list) or (alt_name in volunteer_list):
        st.balloons()
        st.markdown(f"""
            <div class="result-card" style="border-top: 8px solid #28a745;">
                <p class="success-text">
                    ✨ 축하합니다! ✨<br><br>
                    <strong>{name}</strong>님은 우수봉사자 명단에 포함되어 있습니다.<br>
                    따뜻한 헌신에 진심으로 감사드립니다.
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="result-card" style="border-top: 8px solid #dc3545;">
                <p class="fail-text">
                    내년에는 우수봉사자로 만나요!<br><br>
                    보내주신 따뜻한 마음에 감사드리며<br>
                    앞으로의 활동을 늘 응원하겠습니다.
                </p>
            </div>
        """, unsafe_allow_html=True)

st.write("")
st.write("")

# [순서 4] 로고 이미지가 가장 아래에 배치됩니다.
try:
    st.image("logo.png", use_container_width=True)
except:
    pass
