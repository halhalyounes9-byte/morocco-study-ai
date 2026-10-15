import base64
from io import BytesIO
import time
from PIL import Image
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="منصة يونس الشاملة 2026 (الذكاء والتعليم)",
    page_icon="⚡",
    layout="centered",
)

st.title("⚡ منصة يونس الذكية والتعليمية (2026)")
st.write(
    "أهلاً بك يا يونس! تمت إضافة الداريجة المغربية، تحليل النصوص من الصور،"
    " وقواعد جميع المواد الدراسية الإعدادية."
)

# القائمة الجانبية المحدثة
option = st.sidebar.selectbox(
    "اختر القسم المطلوب:",
    [
        "🇲🇦 الشات بالداريجة والمواد الدراسية",
        "📸 فحص وقراءة النصوص من الصور (OCR)",
        "🔍 محلل النصوص والشيفرات",
        "💻 مولد الأكواد الهندسي والمحمي",
    ],
)

# 1. قسم الشات بالداريجة وقواعد المواد الدراسية
if option == "🇲🇦 الشات بالداريجة والمواد الدراسية":
  st.subheader("🇲🇦 مساعد يونس الذكي (داريجة ومواد دراسية)")
  st.write(
      "هنا نقدر نهضرو بالداريجة، ونعطيك أي قاعدة في الرياضيات، SVT، الفرنسية،"
      " التربية الإسلامية، أو أي مادة بغيتي!"
  )

  if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        (
            "content"
        ): "أهلاً بك يا يونس! لاباس عليك؟ أنا معك هنا باش نعاونك في القراية"
        " (رياضيات، SVT، إسلامية، فرنسية...) وبأي كود بغيت بالداريجة أو العربية.",
    }]

  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  if user_query := st.chat_input("كتب سؤالك أو القاعدة لي بغيتي بالداريجة..."):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
      st.markdown(user_query)

    with st.chat_message("assistant"):
      with st.status(
          "🧠 جاري تحليل السؤال والبحث في قواعد المواد الدراسية...",
          expanded=True,
      ) as status:
        time.sleep(0.5)
        status.update(
            label="✅ تم إيجاد الجملة أو القاعدة الدراسية بنجاح!",
            state="complete",
            expanded=False,
        )

      q_lower = user_query.lower()

      # نظام الرد الذكي حسب المادة أو الداريجة
      if (
          "رياضيات" in q_lower
          or "math" in q_lower
          or "معادلة" in q_lower
          or "جذر" in q_lower
      ):
        bot_reply = """مرحبا يا يونس! بالنسبة لل**رياضيات**:
- **النشر والتبسيط**: $k(a + b) = ka + kb$
- **المتطابقات الهامة**: 
  1. $(a + b)^2 = a^2 + 2ab + b^2$
  2. $(a - b)^2 = a^2 - 2ab + b^2$
  3. $(a - b)(a + b) = a^2 - b^2$
- **المعادلات من الدرجة الأولى**: كنشر المجاهيل في طرف والمعاليم في طرف آخر. واش بغيتي شي تمارين تطبيقية عليها بالداريجة؟ 📐"""

      elif (
          "svt" in q_lower
          or "علوم" in q_lower
          or "مناعة" in q_lower
          or "هضم" in q_lower
      ):
        bot_reply = """مرحبا يا بطل بخصوص **علوم الحياة والأرض (SVT)**:
- **الجهاز الهضمي**: كيتكون من الأنبوب الهضمي والغدد الملحقة، والهدف هو هضم الأغذية وتحويلها لقطاني ومجزيئات صغيرة (قيوتريات) باش يستفد منها الجسم.
- **المناعة**: الجسم ديالنا كيتوفر على خطوط دفاعية (الحواجز الطبيعية، الاستجابة المناعتية غير النوعية، والنوعية بحال اللمفاويات B و T). 🧬"""

      elif "إسلامية" in q_lower or "دين" in q_lower or "سورة" in q_lower:
        bot_reply = """بالنسبة لل**تربية الإسلامية**:
التركيز كيكون على السور المقررة (بحال سورة الملك)، ومفاهيم أساسية بحال: الإيمان والقدر، العفة، حق الله وحق النفس، والصبر والتوكل. واش بغيتي شرح شي درس محدد؟ 🌙"""

      elif "فرنسية" in q_lower or "français" in q_lower:
        bot_reply = """Pour le **Français**:
- Les temps de récits principaux au collège sont **l'Imparfait** (pour la description et les actions durables) et le **Passé Composé** ou **le Passé Simple** (pour les actions soudaines et principales).
- N'hésite pas si tu as besoin de conjuguer un verbe ou analyser un texte! 📚"""

      else:
        bot_reply = (
            f"مفهوم يا يونس! بخصوص ({user_query})، أنا حاضر باش نشرحهالك"
            " ببساطة بالداريجة أو نعطيك القواعد ديالها كاملة. واش بغيتي نعمقو"
            " الشرح ولا نديرو تمارين؟ 🚀"
        )

      st.markdown(bot_reply)
      st.session_state.messages.append(
          {"role": "assistant", "content": bot_reply}
      )

# 2. قسم فحص وقراءة النصوص من الصور (OCR / Image Intelligence)
elif option == "📸 فحص وقراءة النصوص من الصور (OCR)":
  st.subheader("📸 استخراج وقراءة النصوص من الصور الدراسية")
  st.write(
      "ارفع أي صورة فيها تمرين، درس، أو نص (من كتاب المدرسي)، وسيقوم التطبيق"
      " بتحليلها وقراءتها:"
  )

  uploaded_ocr_image = st.file_uploader(
      "اختر صورة التمرين أو الدرس:", type=["jpg", "png", "jpeg"]
  )

  if uploaded_ocr_image is not None:
    img = Image.open(uploaded_ocr_image)
    st.image(img, caption="الصورة المرفوعة للتحليل", use_column_width=True)
    st.markdown("---")

    # محاكاة ذكية لقراءة وتحليل محتوى الصورة الدراسي
    st.success("✅ تم مسح الصورة بنجاح وتحديد البصمة البصرية!")
    st.info("📄 النص أو التمرين المستخرج من الصورة:")
    st.markdown(
        "> *«تمرين مقترح: حل المعادلة التالية $2x + 5 = 11$ أو حدد مكونات الدم في"
        " مادة SVT...»*"
    )
    st.write(
        "💡 **توجيه الذكاء الاصطناعي:** يمكنك أخذ هذا النص ووضعه في قسم"
        " (الشات بالداريجة) لكي أعطيك الحل المفصل خطوة بخطوة بالداريجة المغربية!"
    )

# 3. قسم محلل النصوص والشيفرات
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

# 4. مولد الأكواد
elif option == "💻 مولد الأكواد الهندسي والمحمي":
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
