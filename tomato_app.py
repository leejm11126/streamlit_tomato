import streamlit as st
import pandas as pd
import joblib

# 페이지 설정
st.set_page_config(
    page_title="토마토 착과율 예측",
    page_icon="🍅",
    layout="centered"
)

# 모델 불러오기
rf_model = joblib.load("tomato_model.pkl")

# 스타일
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fc;
    }

    .stButton>button {
        width: 100%;
        height: 50px;
        border-radius: 12px;
        background-color: #ff4b4b;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border: none;
    }

    .stButton>button:hover {
        background-color: #ff2e2e;
    }

    .result-box {
        padding: 20px;
        border-radius: 15px;
        background-color: #fff3f3;
        border: 2px solid #ff4b4b;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #d90429;
    }
    </style>
""", unsafe_allow_html=True)

# 제목
st.title("🍅 토마토 착과율 예측 시스템")
st.write("환경 데이터를 조절하여 예상 착과율을 확인하세요.")

st.divider()

# 슬라이더 입력
flower_group = st.slider(
    "🌸 개화군",
    min_value=0.0,
    max_value=20.0,
    value=5.0,
    step=1.0
)

fruit = st.slider(
    "🍅 열매수",
    min_value=0.0,
    max_value=100.0,
    value=30.0,
    step=1.0
)

humidity = st.slider(
    "💧 내부습도 (%)",
    min_value=0.0,
    max_value=100.0,
    value=60.0,
    step=1.0
)

temp = st.slider(
    "🌡️ 내부온도 (℃)",
    min_value=0.0,
    max_value=50.0,
    value=25.0,
    step=0.1
)

ground_temp = st.slider(
    "🌱 지온 (℃)",
    min_value=0.0,
    max_value=40.0,
    value=20.0,
    step=0.1
)

st.divider()

# 예측 버튼
if st.button("📈 착과율 예측하기"):

    # 입력 데이터 생성
    input_data = pd.DataFrame(
        [[flower_group, fruit, humidity, temp, ground_temp]],
        columns=['개화군', '열매수', '내부습도', '내부온도', '지온']
    )

    # 예측
    predicted = rf_model.predict(input_data)

    # 결과 출력
    st.markdown(
        f"""
        <div class="result-box">
            예상 착과율<br>
            {predicted[0]:.1f} %
        </div>
        """,
        unsafe_allow_html=True
    )

    # 상태 메시지
    if predicted[0] >= 80:
        st.success("매우 좋은 환경입니다 skrrrrr 👍")
    elif predicted[0] >= 60:
        st.info("양호한 환경입니다 히히🙂")
    else:
        st.warning("환경 개선이 필요합니다 ㅜㅜㅜㅜㅜ ⚠️")
    
#py -m streamlit run tomato_app.py 
#py -m pip install streamlit
#py -m pip install joblib
#python -m pip install scikit-learn