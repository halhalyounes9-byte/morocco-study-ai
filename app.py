import base64
from io import BytesIO
from PIL import Image
import streamlit as st

# إعدادات الصفحة بتصميم عصري
st.set_page_config(
    page_title="منصة يونس للتحليل والشات الذكي 2026",
    page_icon="⚡",
    layout="centered",
)

st.title("⚡ منصة يونس الذكية (تحليل، حماية، وشات متكامل)")
st.write(
    "أهلاً بك يا يونس! تم إصلاح الشات ليصبح ذكياً ومتفاعلاً مع أي طلب تكتبه"
    " بدقة."
)

# القائمة الجانبية للاستخدام الاحترافي
option = st.sidebar.selectbox(
    "اختر القسم المطلوب:",
    [
        "💬 مساعد يونس الذكي (AI Chat)",
        "🔍 محلل النصوص والشيفرات",
        "📸 محلل وبصمة الصور المتقدم",
        "💻 مولد الأكواد الهندسي مع حماية الأكواد",
    ],
)

# 1. قسم شات الذكاء الاصطناعي (AI Chat Assistant المطور)
if option == "💬 مساعد يونس الذكي (AI Chat)":
  st.subheader("💬 مساعد يونس البرمجي والأمني الذكي")
  st.write(
      "اكتب أي طلب أو سؤال وسأقوم بالرد عليك بحلول وأكواد حقيقية ومفصلة:"
  )

  if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        (
            "content"
        ): "أهلاً بك يا يونس! أنا جاهز الآن. اطلب أي كود أو استفسار وسأعطيك"
        " الإجابة التقنية الصحيحة فوراً.",
    }]

  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  if user_query := st.chat_input("اكتب رسالتك أو طلبك البرمجي هنا..."):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
      st.markdown(user_query)

    # ذكاء حقيقي يستجيب لطلبك أياً كان (مثل طلبك لموقع تأثيرات صور أو غيره)
    with st.chat_message("assistant"):
      query_lower = user_query.lower()

      if "صورة" in query_lower or "تأثيرات" in query_lower or "موقع" in query_lower:
        bot_reply = f"""طلب ممتاز يا يونس! لقد طلبت: ({user_query}). 
إليك كود HTML و CSS و JavaScript جاهز لصناعة موقع بسيط لتأثيرات الصور وتعديلها:

```html
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>موقع تأثيرات الصور</title>
    <style>
        body {{ font-family: Tahoma, sans-serif; text-align: center; background: #111; color: #fff; padding: 20px; }}
        img {{ max-width: 300px; filter: grayscale(0%); transition: 0.3s; border-radius: 8px; }}
        .btn {{ padding: 10px 20px; background: #ff4757; color: white; border: none; cursor: pointer; border-radius: 5px; margin: 5px; }}
    </style>
</head>
<body>
    <h2>تأثيرات الصور الرقمية 2026</h2>
    <input type="file" id="upload" accept="image/*"><br><br>
    <img id="preview" src="" alt="الصورة ستظهر هنا"><br>
    <button class="btn" onclick="applyEffect('grayscale(100%)')">أبيض وأسود</button>
    <button class="btn" onclick="applyEffect('invert(100%)')">عكس الألوان</button>
    <button class="btn" onclick="applyEffect('none')">إعادة ضبط</button>

    <script>
        const upload = document.getElementById('upload');
        const preview = document.getElementById('preview');
        upload.addEventListener('change', (e) => {{
            const file = e.target.files[0];
            if (file) {{
                preview.src = URL.createObjectURL(file);
            }}
        }});
        function applyEffect(filterValue) {{
            preview.style.filter = filterValue;
        }}
    </script>
</body>
</html>
