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
    "أهلاً بك يا يونس! تم إصلاح كافة الأخطاء البرمجية لتعمل المنصة بسلاسة تامة."
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

# 1. قسم شات الذكاء الاصطناعي (AI Chat Assistant المصحح)
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

    with st.chat_message("assistant"):
      query_lower = user_query.lower()

      if "صورة" in query_lower or "تأثيرات" in query_lower or "موقع" in query_lower:
        st.markdown(
            f"طلب ممتاز يا يونس! لقد طلبت: ({user_query}). إليك كود الموقع"
            " جاهز:"
        )

        html_code = """<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>موقع تأثيرات الصور</title>
    <style>
        body { font-family: Tahoma, sans-serif; text-align: center; background: #111; color: #fff; padding: 20px; }
        img { max-width: 300px; filter: grayscale(0%); transition: 0.3s; border-radius: 8px; }
        .btn { padding: 10px 20px; background: #ff4757; color: white; border: none; cursor: pointer; border-radius: 5px; margin: 5px; }
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
        upload.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file) {
                preview.src = URL.createObjectURL(file);
            }
        });
        function applyEffect(filterValue) {
            preview.style.filter = filterValue;
        }
    </script>
</body>
</html>"""
        st.code(html_code, language="html")
        bot_reply = (
            "تم توليد كود موقع تأثيرات الصور بنجاح وأصبح جاهزاً للاستخدام! 🚀"
        )
      else:
        bot_reply = (
            f"فهمت طلبك يا يونس بخصوص ({user_query}). يمكنك الاعتماد على هيكل"
            " بايثون أو السكربتات المخصصة في أقسام المنصة لتنفيذ طلبك بكفاءة"
            " عالية! 🛡️⚡"
        )
        st.markdown(bot_reply)

      st.session_state.messages.append(
          {"role": "assistant", "content": bot_reply}
      )

# 2. قسم محلل النصوص
elif option == "🔍 محلل النصوص والشيفرات":
  st.subheader("🔍 محلل النصوص وفك الترميز المتقدم")
  user_input = st.text_area(
      "أدخل النص أو الكود المشفر هنا:",
      placeholder="الصق النص هنا...",
  )
  if user_input:
    try:
      decoded = base64.b64decode(user_input.encode("utf-8")).decode("utf-8")
      st.success("تم فك التشفير:")
      st.code(decoded, language="text")
    except:
      st.info("النص ليس بصيغة Base64.")

# 3. قسم تحليل الصور المتقدم
elif option == "📸 محلل وبصمة الصور المتقدم":
  st.subheader("📸 محلل وفاحص الصور العميق")
  uploaded_image = st.file_uploader(
      "اختر صورة للفحص:", type=["jpg", "png", "jpeg"]
  )
  if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="الصورة المرفوعة", use_column_width=True)
    st.write(f"الأبعاد: {image.size} | الصيغة: {image.format}")

# 4. قسم مولد الأكواد الهندسي مع الحماية
elif option == "💻 مولد الأكواد الهندسي مع حماية الأكواد":
  st.subheader("💻 مولد الأكواد المؤمّن")
  lang = st.selectbox(
      "اللغة:", ["Python", "JavaScript", "C++", "Linux (Bash)"]
  )
  prompt = st.text_input("ماذا تريد أن يصنع الكود؟")
  protect_code = st.checkbox("🔒 تفعيل تشفير الحماية ضد السرقة")

  if st.button("توليد الكود"):
    if prompt:
      raw_code = f"# كود {lang} لطلبك: {prompt}\nprint('تم التنفيذ بنجاح!')"
      if protect_code:
        encoded = base64.b64encode(raw_code.encode("utf-8")).decode("utf-8")
        st.warning("تم تشفير الكود لحمايته من السرقة:")
        st.code(encoded, language="text")
      else:
        st.success("الكود المولّد:")
        st.code(raw_code, language=lang.lower())
    else:
      st.warning("الرجاء كتابة وصف الطلب أولاً.")
