import base64
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="محلل النصوص والشيفرات البسيط", page_icon="🔍", layout="centered"
)

st.title("🔍 محلل النصوص والشيفرات (Reverse & Analysis)")
st.write(
    "أهلاً بك يا يونس! هذا تطبيق بسيط يفهم مبدأ تحليل النصوص والترميز تماماً مثل أدوات الهندسة العكسية الأولية."
)

# صندوق لإدخال النص المشفر أو العادي
user_input = st.text_area(
    "أدخل النص أو الكود هنا للفحص والتحليل:",
    placeholder="اكتب أي نص أو كود مشفر...",
)

if user_input:
  st.markdown("---")
  st.subheader("📊 نتائج التحليل الأساسي:")

  # حساب بعض الإحصائيات البسيطة عن النص
  char_count = len(user_input)
  word_count = len(user_input.split())
  lines_count = len(user_input.splitlines())

  col1, col2, col3 = st.columns(3)
  col1.metric("عدد الحروف", char_count)
  col2.metric("عدد الكلمات", word_count)
  col3.metric("عدد الأسطر", lines_count)

  st.markdown("---")
  st.subheader("⚙️ عمليات التحليل وفك التشفير التفاعلية:")

  # 1. عكس النص (Reverse Text) - أبسط صور العكس
  reversed_text = user_input[::-1]
  with st.expander("1️⃣ النص المعكوس (Reverse Engineering View)"):
    st.code(reversed_text, language="text")
    st.caption("هذه طريقة بسيطة لرؤية النص مقلوباً من الخلف لليسار.")

  # 2. فحص ترميز Base64 (غالباً تستخدم لإخفاء النصوص)
  try:
    # محاولة فك الترميز إذا كان النص مسجلاً بصيغة Base64
    decoded_base64 = base64.b64decode(user_input.encode("utf-8")).decode(
        "utf-8"
    )
    is_base64 = True
  except Exception:
    is_base64 = False

  with st.expander("2️⃣ فحص الترميز (Base64 Decode)"):
    if is_base64:
      st.success("تم اكتشاف وفك ترميز Base64 بنجاح!")
      st.code(decoded_base64, language="text")
    else:
      st.info(
          "النص المدخل ليس مشفراً بصيغة Base64، لكن يمكنك تجربة إدخال نص مشفر"
          " لاحقاً لاختباره."
      )
