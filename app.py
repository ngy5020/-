import streamlit as st

# 1. 페이지 기본 설정 및 스타일 (고대비 및 시인성 강화)
st.set_page_config(page_title="우수봉사자 조회", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    /* 전체 배경색 */
    .reportview-container { 
        background-color: #f8f9fa; 
    }
    
    /* 1. 메인 제목 스타일 (가장 진한 검은색, 크고 굵게) */
    .main-title {
        text-align: center; 
        color: #000000 !important; 
        font-size: 28px !important; 
        font-weight: 800 !important;
        margin-bottom: 25px;
    }
    
    /* 2. 입력창 윗쪽 안내 문구 스타일 */
    .stTextInput label {
        color: #111111 !important;
        font-size: 18px !important;
        font-weight: 700 !important;
    }
    
    /* 3. 입력창 내부 글자 스타일 (진한 검은색, 굵게) */
    .stTextInput > div > div > input { 
        font-size: 18px !important; 
        color: #000000 !important; 
        font-weight: bold !important; 
        background-color: #ffffff !important;
        border: 2px solid #333333 !important;
    }
    
    /* 결과 카드 디자인 */
    .result-card { 
        background-color: #ffffff; 
        padding: 25px; 
        border-radius: 15px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.15); 
        margin-top: 20px; 
        margin-bottom: 30px;
        text-align: center; 
    }
    .success-text { 
        color: #155724 !important; 
        font-size: 19px !important; 
        font-weight: bold !important; 
        line-height: 1.6; 
    }
    .fail-text { 
        color: #333333 !important; 
        font-size: 17px !important; 
        font-weight: bold !important; 
        line-height: 1.6; 
    }
    </style>
""", unsafe_allow_html=True)

# [위치 변경 1] 글씨 제목이 가장 위로 배치됩니다.
st.markdown("<h1 class='main-title'>우수봉사자 인증서 조회</h1>", unsafe_allow_html=True)

# 2. Secrets에서 명단 가져와 전처리
volunteer_raw = st.secrets.get("volunteer_list", "")
volunteer_raw = volunteer_raw.replace("\n", "").replace(" ", "")
volunteer_list = [name.strip() for name in volunteer_raw.split(",") if name.strip()]

# [위치 변경 2] 성명 입력창이 두 번째로 배치됩니다.
search_name = st.text_input("봉사자 성명을 입력해 주세요:").strip()

# [위치 변경 3] 결과 창이 세 번째로 배치됩니다.
if search_name:
    alt_name = "I" + search_name[1:] if search_name.startswith("이") else search_name
    
    if (search_name in volunteer_list) or (alt_name in volunteer_list):
        st.balloons()
        st.markdown(f"""
            <div class="result-card" style="border-top: 6px solid #28a745;">
                <p class="success-text">
                    ✨ 축하합니다! ✨<br>
                    <strong>{search_name}</strong>님은 우수봉사자 명단에 포함되어 있습니다.<br>
                    따뜻한 헌신에 진심으로 감사드립니다.
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="result-card" style="border-top: 6px solid #6c757d;">
                <p class="fail-text">
                    내년에는 우수봉사자로 만나요!<br>
                    보내주신 따뜻한 마음에 감사드리며<br>
                    앞으로의 활동을 늘 응원하겠습니다.
                </p>
            </div>
        """, unsafe_allow_html=True)

st.write("")
st.write("")

# [위치 변경 4] 센터 로고 이미지가 가장 아래에 배치됩니다.
try:
    st.image("logo.png", use_container_width=True)
except:
    pass
