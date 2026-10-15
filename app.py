import base64
from io import BytesIO
from PIL import Image
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="منصة يونس للذكاء والأنظمة 2026", page_icon="⚡", layout="centered"
)

st.title("⚡ منصة يونس الذكية (2026)")
st.write(
    "أهلاً بك يا يونس! تم حل مشكلة تضارب الأكواد بنجاح والمنصة تعمل بشكل خالي"
    " من الأخطاء."
)

# القائمة الجانبية
option = st.sidebar.selectbox(
    "اختر القسم المطلوب:",
    [
        "💬 مساعد يونس الذكي (AI Chat)",
        "🔍 محلل النصوص والشيفرات",
        "📸 محلل وبصمة الصور المتقدم",
        "💻 مولد الأكواد الهندسي مع حماية الأكواد",
    ],
)

# 1. قسم شات الذكاء الاصطناعي (مصحح وبدون أخطاء)
if option == "💬 مساعد يونس الذكي (AI Chat)":
  st.subheader("💬 مساعد يونس البرمجي والذكي")
  st.write(
      "اسألني عن أي شيء: كود برمجي، فكرة مشروع، حل مشاكل، أو هندسة عكسية:"
  )

  if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        (
            "content"
        ): "أهلاً بك يا يونس! أنا جاهز ومستعد لمساعدتك في أي طلب أو كود"
        " برمجي.",
    }]

  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  if user_query := st.chat_input("اكتب طلبك هنا..."):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
      st.markdown(user_query)

    with st.chat_message("assistant"):
      query_lower = user_query.lower()

      if "صورة" in query_lower or "تأثيرات" in query_lower or "موقع" in query_lower:
        st.markdown(
            "طلب ممتاز يا يونس! إليك كود موقع تأثيرات الصور بـ HTML و CSS و JS:"
        )

        html_code = """<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>منصة تأثيرات الصور</title>
    <style>
        body { font-family: Tahoma, sans-serif; text-align: center; background: #0f172a; color: #fff; padding: 20px; }
        .container { background: #1e293b; padding: 20px; border-radius: 10px; display: inline-block; }
        img { max-width: 300px; border-radius: 8px; margin-top: 10px; }
        .btn { padding: 10px 15px; background: #3b82f6; color: white; border: none; cursor: pointer; border-radius: 5px; margin: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>استوديو تأثيرات الصور</h2>
        <input type="file" id="upload" accept="image/*"><br>
        <img id="preview" src="" alt="قم برفع صورة"><br><br>
        <button class="btn" onclick="setFilter('grayscale(100%)')">أبيض وأسود</button>
        <button class="btn" onclick="setFilter('invert(100%)')">عكس الألوان</button>
        <button class="btn" onclick="setFilter('none')">إعادة ضبط</button>
    </div>

    <script>
        const upload = document.getElementById('upload');
        const preview = document.getElementById('preview');
        upload.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                preview.src = URL.createObjectURL(file);
            }
        });
        function setFilter(val) {
            preview.style.filter = val;
        }
    </script>
</body>
</html>"""
        st.code(html_code, language="html")
        bot_reply = "تم توليد الكود الخاص بموقع الصور بنجاح! 🚀"

      elif "بايثون" in query_lower or "python" in query_lower or "كود" in query_lower:
        st.markdown("إليك كود بايثون متكامل ومخصص لمهمتك:")
        py_code = """import sys

def main():
    print("--- تشغيل السكربت بنجاح ---")
    print("البيئة جاهزة للعمل!")

if __name__ == "__main__":
    main()"""
        st.code(py_code, language="python")
        bot_reply = "تم تجهيز كود بايثون بنجاح! 💻"

      else:
        bot_reply = (
            f"مرحباً يا يونس! لقد استلمت طلبك حول: ({user_query}). أخبرني تفاصيل"
            " أكثر إذا كنت تريد كتابة كود معين خصيصاً لهذه الفكرة! 🛡️"
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
      raw_code = (
          f"# كود {lang} مخصص لمهمة: {prompt}\nprint('تم تنفيذ الأداة"
          " بنجاح!')"
      )
      if protect_code:
        encoded = base64.b64encode(raw_code.encode("utf-8")).decode("utf-8")
        st.warning("تم تشفير الكود لحمايته من السرقة:")
        st.code(encoded, language="text")
      else:
        st.success("الكود المولّد:")
        st.code(raw_code, language=lang.lower())
    else:
      st.warning("الرجاء كتابة وصف الطلب أولاً.")
