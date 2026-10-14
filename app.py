import random
import google.generativeai as genai
from PIL import Image
import streamlit as st

# ==========================================
# 1. إعدادات الصفحة وتصميم الخلفيات العشوائية
# ==========================================
st.set_page_config(
    page_title="المساعد الدراسي الذكي - VIP", page_icon="🎓", layout="wide"
)

# قائمة التدرجات اللونية الفخمة لتتغير عشوائياً في كل تحديث
background_gradients = [
    "linear-gradient(135deg, #0f172a, #1e293b)",  # أزرق داكن كلاسيكي
    "linear-gradient(135deg, #18181b, #27272a)",  # رمادي فخم (Zinc)
    "linear-gradient(135deg, #09090b, #18181b)",  # أسود فحمـي عميق
    "linear-gradient(135deg, #1e1b4b, #312e81)",  # بنفسجي داكن أنيق
    "linear-gradient(135deg, #064e3b, #022c22)",  # أخضر زمردي داكن
    "linear-gradient(135deg, #451a03, #78350f)",  # برونزي دافئ فاخر
]

# اختيار خلفية عشوائية بشكل ديناميكي
current_bg = random.choice(background_gradients)

st.markdown(
    f"""
    <style>
    .main {{
        background: {current_bg};
        color: #f8fafc;
        background-attachment: fixed;
    }}
    .stButton>button {{
        width: 100%;
        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-weight: bold;
    }}
    .stButton>button:hover {{
        background-color: #1d4ed8;
    }}
    .vip-box {{
        background: linear-gradient(135deg, #1e293b, #3b82f6);
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        color: white;
        font-weight: bold;
        margin-bottom: 20px;
        border: 1px solid #60a5fa;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# 2. إعداد الذكاء الاصطناعي مع البحث في الويب
# ==========================================
API_KEY = st.secrets.get("GEMINI_API_KEY", "ضع_مفتاح_API_الخاص_بك_هنا")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    tools="google_search",  # للبحث في جميع مواقع الإنترنت
)

# ==========================================
# 3. إدارة نظام المحادثات والسجل في الشريط الجانبي
# ==========================================
if "chats" not in st.session_state:
  st.session_state.chats = {"محادثة 1": []}

if "current_chat" not in st.session_state:
  st.session_state.current_chat = "محادثة 1"

with st.sidebar:
  st.markdown(
      """
        <div class="vip-box">
            ✨ رصيد السوبر شات: غير محدود (VIP)<br>
            <span style="font-size: 12px; color: #e2e8f0;">نسخة يونس الخاصة 🚀</span>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.title("📂 سجل المحادثات")

  if st.button("➕ محادثة جديدة"):
    new_name = f"محادثة {len(st.session_state.chats) + 1}"
    st.session_state.chats[new_name] = []
    st.session_state.current_chat = new_name
    st.rerun()

  st.markdown("---")
  st.write("💬 **اختر محادثة سابقة:**")

  chat_names = list(st.session_state.chats.keys())
  selected_chat = st.radio(
      "المحادثات:",
      chat_names,
      index=chat_names.index(st.session_state.current_chat),
      label_visibility="collapsed",
  )

  if selected_chat != st.session_state.current_chat:
    st.session_state.current_chat = selected_chat
    st.rerun()

  st.markdown("---")
  st.subheader("⚙️ إعدادات الذكاء")
  super_mode = st.checkbox(
      "⚡ تفعيل وضع السوبر شات الخارق (Deep Think)", value=True
  )
  st.caption("برمجة وتطوير: يونس 🚀")

# ==========================================
# 4. واجهة التطبيق الرئيسية
# ==========================================
st.title("🎓 المساعد الدراسي المغربي الذكي (سوبر شات)")

tab1, tab2 = st.tabs(["📸 حل التمارين بالصور", "💬 السوبر شات والبحث الشامل"])

# --- التبويب الأول: تحليل الصور ---
with tab1:
  st.subheader("📸 رفع صورة التمرين للحل الفوري")
  uploaded_file = st.file_uploader(
      "اختر صورة التمرين:", type=["jpg", "png", "jpeg"]
  )

  if uploaded_file is not None:
    col1, col2 = st.columns([1, 1])
    with col1:
      image = Image.open(uploaded_file)
      st.image(image, caption="الصورة المرفوعة", use_column_width=True)
    with col2:
      if st.button("🚀 استخراج الحل الشامل (سوبر)"):
        with st.spinner("جاري قراءة التمرين وتحليله بعمق..."):
          prompt = (
              "أنت أستاذ ومساعد دراسي خبير جداً بالمناهج المغربية. حلل التمرين"
              " الموجود في الصورة واكتب الحل بالتفصيل الممل خطوة بخطوة مع"
              " التعليل والقوانين المستخدمة."
          )
          response = model.generate_content([prompt, image])
          st.success("تم الحل بنجاح!")
          st.markdown(response.text)

# --- التبويب الثاني: السوبر شات المفتوح ---
with tab2:
  st.subheader(f"⚡ نافذة السوبر شات: {st.session_state.current_chat}")
  if super_mode:
    st.info(
        "💡 **وضع السوبر شات الخارق مفعل:** سيقوم الذكاء الاصطناعي بالبحث في"
        " الإنترنت وتقديم إجابات تحليلية دقيقة ومتقدمة."
    )

  current_messages = st.session_state.chats[st.session_state.current_chat]

  # عرض الرسائل السابقة
  for message in current_messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  # خانة الكتابة للسوبر شات
  if user_query := st.chat_input(
      "اكتب سؤالك أو اطلب بحثاً شاملاً (سوبر شات)..."
  ):
    current_messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
      st.markdown(user_query)

    with st.chat_message("assistant"):
      with st.spinner(
          "⚡ جاري تفعيل السوبر شات والبحث في شبكة الإنترنت..."
      ):
        try:
          full_prompt = (
              (
                  "أنت مساعد أكاديمي خبير ومستشار دراسي متقدم. أجب بدقة وعمق"
                  " مع جلب أحدث وأدق المعلومات من الويب: "
              )
              + user_query
              if super_mode
              else user_query
          )

          chat_history = [
              {"role": m["role"], "parts": [m["content"]]}
              for m in current_messages[:-1]
          ]
          chat = model.start_chat(history=chat_history)
          response = chat.send_message(full_prompt)
          bot_reply = response.text
        except Exception:
          response = model.generate_content(user_query)
          bot_reply = response.text

        st.markdown(bot_reply)
        current_messages.append({"role": "assistant", "content": bot_reply})
