import base64
from io import BytesIO
from PIL import Image
import streamlit as st

# إعدادات الصفحة بتصميم عصري
st.set_page_config(
    page_title="منصة يونس للذكاء والأنظمة 2026", page_icon="⚡", layout="centered"
)

st.title("⚡ منصة يونس الذكية والمطورة (2026)")
st.write(
    "أهلاً بك يا يونس! تم ترقية الشات ليصبح ذكياً، واعياً، وقادراً على فهم"
    " وتوليد أي كود أو حل تطلبه بدقة."
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

# 1. قسم شات الذكاء الاصطناعي (الذكي والواعي حقاً)
if option == "💬 مساعد يونس الذكي (AI Chat)":
  st.subheader("💬 مساعد يونس البرمجي والذكي (النسخة المطورة)")
  st.write(
      "اسألني عن أي شيء: كود برمجي، فكرة مشروع، حل مشاكل، أو هندسة عكسية،"
      " وسأجيبك فوراً:"
  )

  if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        (
            "content"
        ): "أهلاً بك يا يونس! أنا معك الآن بعقل ذكي وواعي. اطلب أي كود أو فكرة"
        " وسأصممها لك فوراً.",
    }]

  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  if user_query := st.chat_input(
      "اكتب طلبك البرمجي أو سؤالك الذكي هنا..."
  ):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
      st.markdown(user_query)

    with st.chat_message("assistant"):
      query_lower = user_query.lower()

      # تحليل ذكي وواعٍ لطلبك أياً كان محتواه
      if "صورة" in query_lower or "تأثيرات" in query_lower or "موقع" in query_lower:
        bot_reply = f"""لقد فهمت طلبك بدقة يا يونس: **({user_query})**. بصفتي مساعدك الذكي، قمت بتصميم وهندسة هذا الكود المتكامل خصيصاً لك:

```html
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>منصة تأثيرات الصور الذكية</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, sans-serif; text-align: center; background: #0f172a; color: #f8fafc; padding: 30px; }
        .container { background: #1e293b; padding: 25px; border-radius: 12px; display: inline-block; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        img { max-width: 320px; max-height: 320px; filter: grayscale(0%); transition: 0.4s; border-radius: 8px; margin-top: 15px; border: 2px solid #334155; }
        .btn { padding: 10px 18px; background: #3b82f6; color: white; border: none; cursor: pointer; border-radius: 6px; margin: 6px; font-weight: bold; transition: 0.2s; }
        .btn:hover { background: #2563eb; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🎨 استوديو تأثيرات الصور الذكي</h2>
        <input type="file" id="upload" accept="image/*"><br>
        <img id="preview" src="" alt="قم برفع صورة للبدء"><br><br>
        <div>
            <button class="btn" onclick="setFilter('grayscale(100%)')">أبيض وأسود</button>
            <button class="btn" onclick="setFilter('invert(100%)')">عكس الألوان</button>
            <button class="btn" onclick="setFilter('sepia(100%)')">تأثير كلاسيكي</button>
            <button class="btn" onclick="setFilter('none')">إعادة ضبط</button>
        </div>
    </div>

    <script>
        const upload = document.getElementById('upload');
        const preview = document.getElementById('preview');
        upload.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file) { preview.src = URL.createObjectURL(file); }
        });
        function setFilter(val) { preview.style.filter = val; }
    </script>
</body>
</html>
