import streamlit as st

# モダンなUIデザインのためのCSS
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #f5f5f5;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
    .widget-text input {
        border-radius: 5px;
        border: 1px solid #ccc;
        padding: 8px;
    }
    .widget-select select {
        border-radius: 5px;
        border: 1px solid #ccc;
        padding: 8px;
    }
    .widget-button button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .widget-button button:hover {
        background-color: #45a049;
    }
    .success {
        color: #4CAF50;
        font-weight: bold;
    }
    .error {
        color: #f44336;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("SaaS Account and License Management")

# サービスとライセンスの定義
services = {
    "Service A": ["License A1", "License A2", "License A3"],
    "Service B": ["License B1", "License B2"],
    "Service C": ["License C1", "License C2", "License C3", "License C4"]
}

# ユーザー情報の入力フォーム
with st.form(key='user_info_form'):
    email = st.text_input("メールアドレス")
    service = st.selectbox("サービス", list(services.keys()))
    licenses = st.multiselect("ライセンス", services[service])
    submit_button = st.form_submit_button(label='リクエスト送信')

# 承認プロセスのダミー関数
def dummy_approval(email, service, licenses):
    return True

# アカウント作成のダミー関数
def dummy_create_account(email, service):
    return True

# ライセンス付与のダミー関数
def dummy_assign_licenses(email, service, licenses):
    return True

# 申請ワークフロー
if submit_button:
    st.info(f"{email}からのリクエストを受け付けました。承認プロセスを開始します。")
    
    # ダミーの承認関数を呼び出し
    approved = dummy_approval(email, service, licenses)
    
    if approved:
        st.success("リクエストが承認されました。アカウント作成とライセンス付与を開始します。")
        
        # ダミーのアカウント作成関数を呼び出し
        account_created = dummy_create_account(email, service)
        
        # ダミーのライセンス付与関数を呼び出し
        licenses_assigned = dummy_assign_licenses(email, service, licenses)
        
        if account_created and licenses_assigned:
            st.balloons()
            st.markdown(f"<div class='success'>{email}のアカウントが作成され、{service}の以下のライセンスが付与されました：{', '.join(licenses)}</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='error'>アカウント作成またはライセンス付与に失敗しました。管理者に連絡してください。</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='error'>リクエストが承認されませんでした。再度申請してください。</div>", unsafe_allow_html=True)