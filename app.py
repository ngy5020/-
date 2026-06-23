import streamlit as st

# 1. 페이지 기본 설정 및 스타일
st.set_page_config(page_title="우수봉사자 조회", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    .reportview-container { background-color: #f5f7fa; }
    .stTextInput > div > div > input { font-size: 16px !important; color: #2c3e50 !important; font-weight: bold !important; }
    .result-card { background-color: #ffffff; padding: 25px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-top: 20px; text-align: center; }
    .success-text { color: #1e7e34 !important; font-size: 18px !important; font-weight: bold !important; line-height: 1.6; }
    .fail-text { color: #495057 !important; font-size: 16px !important; font-weight: 500 !important; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)

# 2. 센터 로고 이미지 배치
try:
    st.image("logo.png", use_container_width=True)
except:
    pass

st.markdown("<h3 style='text-align: center; color: #343a40;'>우수봉사자 인증서 조회</h3>", unsafe_allow_html=True)
st.write("")

# 3. [핵심 수정] Secrets에서 명단을 가져와 안전하게 쪼개기
volunteer_raw = st.secrets.get("volunteer_list", "")

# 명단 전처리: 줄바꿈이나 공백을 없애고 쉼표로 완벽하게 분리
volunteer_raw = volunteer_raw.replace("\n", "").replace(" ", "")
volunteer_list = [name.strip() for name in volunteer_raw.split(",") if name.strip()]

# 4. 이름 입력창
search_name = st.text_input("봉사자 성명을 입력해 주세요:").strip()

if search_name:
    # '이'씨 성을 위한 안전장치도 유지
    alt_name = "I" + search_name[1:] if search_name.startswith("이") else search_name
    
    # 쪼개진 명단 리스트에 입력한 이름이 존재하는지 확인
    if (search_name in volunteer_list) or (alt_name in volunteer_list):
        st.balloons()
        st.markdown(f"""
            <div class="result-card" style="border-top: 5px solid #28a745;">
                <p class="success-text">
                    ✨ 축하합니다! ✨<br>
                    <strong>{search_name}</strong>님은 우수봉사자 명단에 포함되어 있습니다.<br>
                    따뜻한 헌신에 진심으로 감사드립니다.
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="result-card" style="border-top: 5px solid #6c757d;">
                <p class="fail-text">
                    내년에는 우수봉사자로 만나요!<br>
                    보내주신 따뜻한 마음에 감사드리며<br>
                    앞으로의 활동을 늘 응원하겠습니다.
                </p>
            </div>
        """, unsafe_allow_html=True)
