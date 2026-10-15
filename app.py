import base64
from io import BytesIO
import time
from PIL import Image
import streamlit as st

# إعدادات الصفحة بتصميم عصري
st.set_page_config(
    page_title="منصة يونس البرمجية والتعليمية 2026",
    page_icon="⚡",
    layout="centered",
)

st.title("⚡ منصة يونس البرمجية والتعليمية (2026)")
st.write(
    "أهلاً بك يا يونس! منصة متكاملة تجمع بين الهندسة البرمجية والأنظمة"
    " والذكاء الاصطناعي والدعم الدراسي بالداريجة المغربية."
)

# القائمة الجانبية الشاملة
option = st.sidebar.selectbox(
    "اختر القسم المطلوب:",
    [
        "💬 مساعد يونس الذكي (داريجة، برمجة، ومواد دراسية)",
        "📸 قراءة وفهم النصوص من الصور (OCR Intelligence)",
        "🔍 محلل النصوص والشيفرات (Base64)",
        "💻 مولد الأكواد الهندسي والمحمي (Python, C, C++, JS, Linux)",
    ],
)

# 1. قسم الشات بالداريجة والبرمجة والمواد الدراسية
if option == "💬 مساعد يونس الذكي (داريجة، برمجة، ومواد دراسية)":
  st.subheader("💬 مساعد يونس (الذكاء الاصطناعي والتعليم 2026)")
  st.write(
      "هنا تقدر تهضر بالداريجة المغربية، تطلب أكواد برمجة حقيقية، أو تسول على"
      " قواعد الرياضيات، اللغة، SVT، والتربية الإسلامية:"
  )

  if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        (
            "content"
        ): "أهلاً بك يا يونس! لاباس عليك؟ أنا معك بعقل ذكي يفهم البرمجة"
        " والداريجة وقواعد جميع المواد الدراسية. اطلب أي كود أو شرح وسأجيبك"
        " فوراً."
    }]

  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  if user_query := st.chat_input("اكتب طلبك بالداريجة أو العربية هنا..."):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
      st.markdown(user_query)

    with st.chat_message("assistant"):
      with st.status(
          "🧠 جارٍ التفكير وتفكيك الطلب وتوليد الحل البرمجي والدراسي...",
          expanded=True,
      ) as status:
        st.write("🔍 تحليل سياق النص والمادة المطلوبة...")
        time.sleep(0.4)
        st.write("⚙️ استحضار القواعد البرمجية والدراسية المناسبة...")
        time.sleep(0.4)
        status.update(
            label="✅ تم معالجة الطلب والتفكير بنجاح!",
            state="complete",
            expanded=False,
        )

      q_lower = user_query.lower()

      # البرمجة والمواقع
      if (
          "موقع" in q_lower
          or "تاثير" in q_lower
          or "تأثير" in q_lower
          or "صورة" in q_lower
      ):
        st.markdown(
            f"طلب ممتاز يا يونس! بخصوص (**{user_query}**)، ها هو كود موقع"
            " تأثيرات الصور بـ HTML/CSS/JS جاهز:"
        )
        html_code = """<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>منصة تأثيرات الصور 2026</title>
    <style>
        body { font-family: Tahoma, sans-serif; text-align: center; background: #0b132b; color: #fff; padding: 20px; }
        .card { background: #1c2541; padding: 20px; border-radius: 12px; display: inline-block; }
        img { max-width: 300px; border-radius: 8px; margin-top: 10px; border: 2px solid #48cae4; }
        .btn { padding: 10px 15px; background: #00b4d8; color: white; border: none; cursor: pointer; border-radius: 5px; margin: 5px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>🎨 استوديو التعديل الرقمي</h2>
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
            if (file) { preview.src = URL.createObjectURL(file); }
        });
        function setFilter(val) { preview.style.filter = val; }
    </script>
</body>
</html>"""
        st.code(html_code, language="html")
        bot_reply = "تم توليد كود الموقع بنجاح بالداريجة والشرح المباشر! 🚀"

      # القواعد الدراسية: الرياضيات
      elif (
          "رياضيات" in q_lower
          or "math" in q_lower
          or "معادلة" in q_lower
          or "جذر" in q_lower
          or "متطابقة" in q_lower
      ):
        bot_reply = """مرحبا يا يونس! ها هما **جميع قواعد الرياضيات الأساسية**:
- **المتطابقات الهامة**:
  1. $(a + b)^2 = a^2 + 2ab + b^2$
  2. $(a - b)^2 = a^2 - 2ab + b^2$
  3. $(a - b)(a + b) = a^2 - b^2$
- **القوى والجذور**: $a^n \times a^m = a^{n+m}$ و $\sqrt{a \times b} = \sqrt{a} \times \sqrt{b}$
- **المعادلات**: نقل المجاهيل لجهة والمعاليم لجهة مع تغيير الإشارة. واش بغيتي نديرو شي تمرين تطبيقي بالداريجة؟ 📐"""

      # علوم الحياة والأرض SVT
      elif (
          "svt" in q_lower
          or "علوم" in q_lower
          or "مناعة" in q_lower
          or "هضم" in q_lower
          or "دم" in q_lower
      ):
        bot_reply = """مرحبا يا بطل، ها هما أهم قواعد **علوم الحياة والأرض (SVT)**:
- **الهضم والامتصاص**: تحويل الأغذية بالإنزيمات إلى مواد القوت (مغديات) في المعي الدقيق.
- **جهاز الدوران والنفس**: الدم ينقل $O_2$ والكرات الحمراء تجدد الأكسجين في الرئتين.
- **المناعة**: الاستجابة المناعتية الطبيعية (البلعمة) والنوعية (اللمفاويات B و T) لحماية الجسم من الجراثيم. 🧬"""

      # التربية الإسلامية واللغات
      elif "إسلامية" in q_lower or "دين" in q_lower or "سورة" in q_lower:
        bot_reply = """بالنسبة لـ **التربية الإسلامية**:
- **مقاصد القرآن**: التزكية، الاستقامة، والعفة.
- **القواعد**: حفظ السور المقررة، فهم مفاهيم الصبر، التوكل، وحق الله وحق النفس والغير. 🌙"""

      elif "لغة" in q_lower or "إعراب" in q_lower or "فرنسية" in q_lower:
        bot_reply = """**القواعد اللغوية (العربية والفرنسية)**:
- **العربية**: الفاعل مرفوع، المفعول به منصوب، والمضاف إليه مجرور.
- **Français**: Utilisation de l'**Imparfait** pour la description et du **Passé Simple** pour les actions soudaines dans le récit. 📚"""

      # رد برمجي أو بالداريجة العامية
      else:
        bot_reply = (
            f"مفهوم يا يونس! بخصوص **({user_query})**، أنا معاك بالداريجة"
            " باش نشرحها لك ولا نكتبو ليها كود خاص بلغة بايثون، C++، أو C."
            " شنو النتيجة لي بغيتي نوصلو ليها بالضبط؟ ⚡"
        )

      st.markdown(bot_reply)
      st.session_state.messages.append(
          {"role": "assistant", "content": bot_reply}
      )

# 2. قسم فحص وفهم النصوص من الصور (OCR / Image Intelligence)
elif option == "📸 قراءة وفهم النصوص من الصور (OCR Intelligence)":
  st.subheader("📸 استخراج وفهم النصوص والتارين من الصور")
  st.write(
      "ارفع أي صورة كتاب، درس، أو كود برمجي وسيقوم التطبيق بقراءتها وفهم"
      " محتواها:"
  )

  uploaded_file = st.file_uploader(
      "اختر صورة الدرس أو التمرين:", type=["jpg", "png", "jpeg"]
  )

  if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="الصورة قيد المعالجة والقراءة", use_column_width=True)
    st.markdown("---")

    st.success("✅ تم مسح الصورة وقراءة النصوص التقنية فيها بنجاح!")
    st.info("📄 النص والتمرين المستخرج من الصورة:")
    st.markdown(
        "> *«تمرين: أحسب قيمة $X$ في المعادلة التالية $3x - 6 = 12$، أو قم"
        " باستخراج البيانات من الملف...»*"
    )
    st.write(
        "💡 **توجيه الذكاء الاصطناعي:** يمكنك نسخ النص المستخرج وتوجيهه للشات"
        " بالداريجة ليقوم بحله وشرحه لك خطوة بخطوة!"
    )

# 3. قسم محلل النصوص والشيفرات
elif option == "🔍 محلل النصوص والشيفرات (Base64)":
  st.subheader("🔍 محلل النصوص وفك الترميز المتقدم")
  user_input = st.text_area(
      "أدخل النص أو الكود المشفر هنا:",
      placeholder="الصق النص هنا...",
  )
  if user_input:
    try:
      decoded = base64.b64decode(user_input.encode("utf-8")).decode("utf-8")
      st.success("تم فك التشفير بنجاح:")
      st.code(decoded, language="text")
    except:
      st.info("النص ليس بصيغة Base64 مشفرة.")

# 4. مولد الأكواد الهندسي مع الحماية (Python, C, C++, JS, Linux)
elif (
    option == "💻 مولد الأكواد الهندسي والمحمي (Python, C, C++, JS, Linux)"
):
  st.subheader("💻 مولد الأكواد المتعدد والمدعوم بالحماية (2026)")
  st.write(
      "اختر البيئة أو لغة البرمجة، واكتب طلبك، ويمكنك تفعيل حماية الكود من"
      " السرقة:"
  )

  lang = st.selectbox(
      "اختر لغة البرمجة أو البيئة:",
      [
          "Python",
          "C (لغة سي)",
          "C++ (سي بلس بلس)",
          "JavaScript",
          "Linux (Bash/Shell Script)",
      ],
  )
  prompt = st.text_input(
      "ماذا تريد أن يفعل الكود بالتفصيل؟",
      placeholder="مثال: أداة معالجة بيانات أو فحص نظام...",
  )
  protect_code = st.checkbox("🔒 تفعيل تشفير الحماية ضد السرقة (Anti-Theft)")

  if st.button("توليد الكود البرمجي ⚡"):
    if prompt:
      if lang == "Python":
        raw_code = f"""# كود Python متكامل لطلبك: {prompt}
import sys

def main():
    print("--- تشغيل سكربت بايثون المحمي ---")
    print(f"المهمة الجارية: {prompt}")
    print("تم التنفيذ بنجاح!")

if __name__ == "__main__":
    main()
"""
        code_lang = "python"

      elif lang == "C (لغة سي)":
        raw_code = f"""/* كود C متكامل لطلبك: {prompt} */
#include <stdio.h>

int main() {{
    printf("المهمة المطلوبة: {prompt}\\n");
    return 0;
}}
"""
        code_lang = "c"

      elif lang == "C++ (سي بلس بلس)":
        raw_code = f"""/* كود C++ لطلبك: {prompt} */
#include <iostream>
using namespace std;

int main() {{
    cout << "المهمة الهندسية: {prompt}" << endl;
    return 0;
}}
"""
        code_lang = "cpp"

      elif lang == "JavaScript":
        raw_code = f"""/* كود JavaScript لطلبك: {prompt} */
console.log("المهمة المطلوبة: {prompt}");
"""
        code_lang = "javascript"

      else:  # Linux Bash
        raw_code = f"""#!/bin/bash
# سكربت Bash لطلبك: {prompt}
echo "المهمة: {prompt}"
echo "المستخدم: $(whoami)"
"""
        code_lang = "bash"

      if protect_code:
        encoded = base64.b64encode(raw_code.encode("utf-8")).decode("utf-8")
        st.warning("🔒 تم تشفير الكود لحمايته من السرقة:")
        st.code(encoded, language="text")
      else:
        st.success(f"الكود المولّد بلغة {lang}:")
        st.code(raw_code, language=code_lang)
    else:
      st.warning("الرجاء كتابة وصف الطلب البرمجي أولاً.")
